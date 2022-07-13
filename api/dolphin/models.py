from platform import win32_edition, win32_is_iot
import uuid

from django.db import models

from dolphin.main import DOLPHIN_VERSION


class Log(models.Model):
    # standard data fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # general & complex data fields
    dolphin_version = models.CharField(max_length=10)
    date_measured = models.DateTimeField()
    machine_id = models.UUIDField()
    boot_time = models.FloatField()
    cpu_times = models.JSONField()
    cpu_percent_global = models.FloatField()
    cpu_percent = models.JSONField()
    cpu_times_percent = models.JSONField()
    cpu_physical_count = models.IntegerField()
    cpu_logical_count = models.IntegerField()
    cpu_freq = models.JSONField()
    disk_partitions = models.JSONField()
    all_disk_partitions = models.JSONField()
    disk_io_counters_per_disk = models.JSONField()
    network_io_counters_per_nic = models.JSONField()

    # platform data fields
    architecture_bits = models.CharField()
    architecture_linkage = models.CharField()
    machine = models.CharField()
    platform = models.CharField()
    node = models.CharField()
    processor = models.CharField()
    system = models.CharField()
    system_version = models.CharField()
    system_release = models.CharField()
    win32_edition = models.CharField()
    win32_is_iot = models.BooleanField()
    win32_ver_release = models.CharField()
    win32_ver_version = models.CharField()
    win32_ver_csd = models.CharField()
    win32_ver_ptype = models.CharField()
    release = models.CharField()
    versioninfo = models.JSONField()
    libc_lib = models.CharField()
    libc_version = models.CharField()

    # cpu times data fields
    cpu_times_user = models.FloatField()
    cpu_times_system = models.FloatField()
    cpu_times_idle = models.FloatField()
    cpu_times_nice = models.FloatField(null=True, default=None)
    cpu_times_iowait = models.FloatField(null=True, default=None)
    cpu_times_irq = models.FloatField(null=True, default=None)
    cpu_times_softirq = models.FloatField(null=True, default=None)
    cpu_times_steal = models.FloatField(null=True, default=None)
    cpu_times_guest = models.FloatField(null=True, default=None)
    cpu_times_guest_nice = models.FloatField(null=True, default=None)
    cpu_times_interrupt = models.FloatField(null=True, default=None)
    cpu_times_dpc = models.FloatField(null=True, default=None)

    cpu_stats_ctx_switches = models.IntegerField()
    cpu_stats_interrupts = models.IntegerField()
    cpu_stats_soft_interrupts = models.IntegerField()
    cpu_stats_syscalls = models.IntegerField()

    cpu_freq_current = models.FloatField(null=True, default=None)
    cpu_freq_min = models.FloatField(null=True, default=None)
    cpu_freq_max = models.FloatField(null=True, default=None)

    # disk load data fields
    disk_load_avg_1min = models.FloatField(null=True, default=None)
    disk_load_avg_5min = models.FloatField(null=True, default=None)
    disk_load_avg_15min = models.FloatField(null=True, default=None)

    disk_io_read_count = models.BigIntegerField()
    disk_io_write_count = models.BigIntegerField()
    disk_io_read_bytes = models.BigIntegerField()
    disk_io_write_bytes = models.BigIntegerField()
    disk_io_read_time = models.BigIntegerField(null=True, default=None)
    disk_io_write_time = models.BigIntegerField(null=True, default=None)
    disk_io_busy_time = models.BigIntegerField(null=True, default=None)
    disk_io_read_merged_count = models.BigIntegerField(null=True, default=None)
    disk_io_write_merged_count = models.BigIntegerField(null=True, default=None)

    # memory data fields
    virtual_memory_total = models.BigIntegerField()
    virtual_memory_available = models.BigIntegerField()
    virtual_memory_used = models.FloatField(null=True, default=None)
    virtual_memory_free = models.BigIntegerField(null=True, default=None)
    virtual_memory_active = models.BigIntegerField(null=True, default=None)
    virtual_memory_inactive = models.BigIntegerField(null=True, default=None)
    virtual_memory_wired = models.BigIntegerField(null=True, default=None)
    virtual_memory_buffers = models.BigIntegerField(null=True, default=None)
    virtual_memory_cached = models.BigIntegerField(null=True, default=None)
    virtual_memory_slab = models.BigIntegerField(null=True, default=None)

    swap_memory_total = models.BigIntegerField()
    swap_memory_used = models.BigIntegerField()
    swap_memory_free = models.BigIntegerField()
    swap_memory_percent = models.FloatField()
    swap_memory_sin = models.BigIntegerField()
    swap_memory_sout = models.BigIntegerField()

    # network data fields
    network_io_bytes_sent = models.BigIntegerField()
    network_io_bytes_recv = models.BigIntegerField()
    network_io_packets_sent = models.BigIntegerField()
    network_io_packets_recv = models.BigIntegerField()
    network_io_errin = models.BigIntegerField()
    network_io_errout = models.BigIntegerField()
    network_io_dropin = models.BigIntegerField()
    network_io_dropout = models.BigIntegerField()

    # sensors data fields
    sensors_battery_percent = models.FloatField(null=True, default=None)
    sensors_battery_secsleft = models.FloatField(null=True, default=None)
    sensors_battery_power_plugged = models.BooleanField(null=True, default=None)

    def __str__(self):
        return self.machine_id

    class Meta:
        ordering = ["created"]
