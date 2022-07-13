from rest_framework.decorators import api_view
from rest_framework.response import Response

from dolphin.serializers import LogSerializer, MachineSerializer


@api_view(["POST"])
def add_log(request):
    log_serializer = LogSerializer(data=request.data)
    machine_serializer = MachineSerializer(data=request.data)
    if log_serializer.is_valid() and machine_serializer.is_valid():
        log_serializer.save()
        machine_serializer.save()
        return Response(status=201)
    else:
        return Response(status=400)
