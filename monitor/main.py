import uuid
import time
import json
import platform
from datetime import datetime
from pathlib import Path

from appdirs import user_data_dir
import psutil
import requests


API_ENDPOINT = "https://dolphin.hulse.app/log/"
SLEEP_PERIOD = 10
UUID_DIRPATH = Path(user_data_dir("Dolphin", "Hulse"))
UUID_FILENAME = ".uuid"
UUID_FILEPATH = UUID_DIRPATH / UUID_FILENAME
DOLPHIN_VERSION = "0.0.1"

if not UUID_DIRPATH.is_dir():
    UUID_DIRPATH.mkdir(parents=True, exist_ok=True)

if not UUID_FILEPATH.is_file():
    MACHINE_ID = str(uuid.uuid4())
    with open(UUID_FILEPATH, "w") as f:
        f.write(MACHINE_ID)
else:
    with open(UUID_FILEPATH, "r") as f:
        MACHINE_ID = f.read()


def transform_to_dict(namedtuple):
    return {k: v for k, v in zip(namedtuple._fields, namedtuple)}


def dict_to_dict(namedtuple):
    return {key: transform_to_dict(namedtuple.__getitem__(key)) for key in namedtuple}


transform = lambda x: list(map(transform_to_dict, x))
generate_idx = lambda x: {idx: v for idx, v in enumerate(x)}


def get_telemetry():
    telemetry_data = {
        "dolphin_version": DOLPHIN_VERSION,
        "date_measured": str(datetime.now()),
        "machine_id": MACHINE_ID,
        "boot_time": psutil.boot_time(),
        "cpu_times": transform(psutil.cpu_times(percpu=True)),
        "cpu_percent_global": psutil.cpu_percent(),
        "cpu_percent": generate_idx(psutil.cpu_percent(percpu=True)),
        "cpu_times_percent": transform(psutil.cpu_times_percent(percpu=True)),
        "cpu_physical_count": psutil.cpu_count(logical=False),
        "cpu_logical_count": psutil.cpu_count(),
        "cpu_freq": transform(psutil.cpu_freq(percpu=True)),
        "disk_partitions": transform(psutil.disk_partitions()),
        "all_disk_partitions": transform(psutil.disk_partitions(all=True)),
        "disk_io_counters_per_disk": dict_to_dict(
            psutil.disk_io_counters(perdisk=True)
        ),
        "network_io_counters_per_nic": dict_to_dict(
            psutil.net_io_counters(pernic=True)
        ),
    }
    telemetry_data.update(get_platform_info())

    cpu_times_keys = [
        "cpu_times_user",
        "cpu_times_system",
        "cpu_times_idle",
        "cpu_times_nice",
        "cpu_times_iowait",
        "cpu_times_irq",
        "cpu_times_softirq",
        "cpu_times_steal",
        "cpu_times_guest",
        "cpu_times_guest_nice",
        "cpu_times_interrupt",
        "cpu_times_dpc",
    ]
    cpu_times = psutil.cpu_times()
    cpu_times_dict = {
        k: v
        for k, v in zip(
            [k for k in cpu_times_keys if k.split("_")[-1] in cpu_times._fields],
            cpu_times,
        )
    }
    telemetry_data.update(cpu_times_dict)

    cpu_times_percent = psutil.cpu_times_percent()
    cpu_times_percent_keys = [
        k.replace("times", "times_percent") for k in cpu_times_keys
    ]
    cpu_times_percent_dict = {
        k: v
        for k, v in zip(
            [
                k
                for k in cpu_times_percent_keys
                if k.split("_")[-1] in cpu_times_percent._fields
            ],
            cpu_times_percent,
        )
    }
    telemetry_data.update(cpu_times_percent_dict)

    cpu_stats_keys = [
        "cpu_stats_ctx_switches",
        "cpu_stats_interrupts",
        "cpu_stats_soft_interrupts",
        "cpu_stats_syscalls",
    ]
    cpu_stats = psutil.cpu_stats()
    cpu_stats_dict = {k: v for k, v in zip(cpu_stats_keys, cpu_stats)}
    telemetry_data.update(cpu_stats_dict)

    if (
        psutil.LINUX
        or psutil.MACOS
        or psutil.WINDOWS
        or psutil.FREEBSD
        or psutil.OPENBSD
    ):
        cpu_freq_keys = ["cpu_freq_current", "cpu_freq_min", "cpu_freq_max"]
        cpu_freq = psutil.cpu_freq()
        cpu_freq_dict = {k: v for k, v in zip(cpu_freq_keys, cpu_freq)}
        telemetry_data.update(cpu_freq_dict)

        disk_load_keys = [
            "disk_load_avg_1min",
            "disk_load_avg_5min",
            "disk_load_avg_15min",
        ]
        disk_load_avg = psutil.getloadavg()
        disk_load_dict = {k: v for k, v in zip(disk_load_keys, disk_load_avg)}
        telemetry_data.update(disk_load_dict)

    virtual_memory_keys = [
        "virtual_memory_total",
        "virtual_memory_available",
        "virtual_memory_used",
        "virtual_memory_free",
        "virtual_memory_active",
        "virtual_memory_inactive",
        "virtual_memory_buffers",
        "virtual_memory_cached",
        "virtual_memory_shared",
        "virtual_memory_slab",
        "virtual_memory_wired",
    ]
    virtual_memory = psutil.virtual_memory()
    virtual_memory_dict = {
        k: v
        for k, v in zip(
            [
                k
                for k in virtual_memory_keys
                if k.split("_")[-1] in virtual_memory._fields
            ],
            virtual_memory,
        )
    }
    telemetry_data.update(virtual_memory_dict)

    swap_memory_keys = [
        "swap_memory_total",
        "swap_memory_used",
        "swap_memory_free",
        "swap_memory_percent",
        "swap_memory_sin",
        "swap_memory_sout",
    ]
    swap_memory = psutil.swap_memory()
    swap_memory_dict = {k: v for k, v in zip(swap_memory_keys, swap_memory)}
    telemetry_data.update(swap_memory_dict)

    disk_io_keys = [
        "disk_io_read_count",
        "disk_io_write_count",
        "disk_io_read_bytes",
        "disk_io_write_bytes",
        "disk_io_read_time",
        "disk_io_write_time",
        "disk_io_busy_time",
        "disk_io_read_merged_counts",
        "disk_io_write_merged_counts",
    ]
    disk_io_counters = psutil.disk_io_counters()
    disk_io_dict = {
        k: v
        for k, v in zip(
            [
                k
                for k in disk_io_keys
                if "_".join(k.split("_")[2:]) in disk_io_counters._fields
            ],
            disk_io_counters,
        )
    }
    telemetry_data.update(disk_io_dict)

    network_io_counters_keys = [
        "network_io_bytes_sent",
        "network_io_bytes_recv",
        "network_io_packets_sent",
        "network_io_packets_recv",
        "network_io_errin",
        "network_io_errout",
        "network_io_dropin",
        "network_io_dropout",
    ]
    network_io_counters = psutil.net_io_counters()
    network_io_dict = {
        k: v for k, v in zip(network_io_counters_keys, network_io_counters)
    }
    telemetry_data.update(network_io_dict)

    if psutil.LINUX or psutil.FREEBSD:
        telemetry_data["sensors_temperatures"] = psutil.sensors_temperatures()

    if psutil.LINUX:
        telemetry_data["sensors_fans"] = psutil.sensors_fans()

    if psutil.LINUX or psutil.WINDOWS or psutil.MACOS or psutil.FREEBSD:
        percent, secsleft, power_plugged = psutil.sensors_battery()
        if secsleft == psutil.POWER_TIME_UNLIMITED:
            secsleft = 86400  # set to a high number
        elif secsleft == psutil.POWER_TIME_UNKNOWN:
            secsleft = -2
        telemetry_data["sensors_battery_percent"] = percent
        telemetry_data["sensors_battery_secsleft"] = secsleft
        telemetry_data["sensors_battery_power_plugged"] = power_plugged

    return telemetry_data


def get_platform_info():
    architecture_bits, architecture_linkage = platform.architecture()
    platform_info = {
        "architecture_bits": architecture_bits,
        "machine": platform.machine(),
        "platform": platform.platform(),
        "node": platform.node(),
        "processor": platform.processor(),
        "system": platform.system(),
        "system_version": platform.version(),
        "system_release": platform.release(),
        "win32_is_iot": platform.win32_is_iot(),
    }
    if architecture_linkage:
        platform_info["architecture_linkage"] = architecture_linkage

    # TODO: update script to include additional platform info
    # if psutil.WINDOWS:
    #    platform_info["win32_edition"] = platform.win32_edition()
    #    win32_ver_keys = [
    #        "win32_ver_release",
    #        "win32_ver_version",
    #        "win32_ver_csd",
    #        "win32_ver_ptype",
    #    ]
    #    win32_ver = {k: v for k, v in zip(win32_ver_keys, platform.win32_ver())}
    #    platform_info.update(win32_ver)
    #
    # if psutil.MACOS:
    #    mac_ver_keys = ["release", "versioninfo", "machine"]
    #    mac_ver = {k: v for k, v in zip(mac_ver_keys, platform.mac_ver())}
    #    versioninfo_keys = ["mac_version", "mac_dev_stage", "mac_non_release_version"]
    #    platform_info.update(mac_ver)
    #
    # if psutil.LINUX or psutil.OPENBSD or psutil.FREEBSD:
    #    libc_ver_keys = ["libc_lib", "libc_version"]
    #    libc_ver = {k: v for k, v in zip(libc_ver_keys, platform.libc_ver())}
    #    platform_info.update(libc_ver)

    return platform_info


def send_telemetry(telemetry_data):
    resp = requests.post(API_ENDPOINT, json=telemetry_data)


def main():
    while True:
        start_ts = time.time()
        telemetry_data = get_telemetry()
        print(json.dumps(telemetry_data, indent=4))
        print(f"took {time.time()-start_ts:.2f}")
        # send_telemetry(telemetry_data)
        break
        time.sleep(SLEEP_PERIOD)


if __name__ == "__main__":
    main()
