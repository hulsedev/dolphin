import json

from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from dolphin.models import Machine
from dolphin.serializers import LogSerializer, MachineSerializer


@api_view(["POST"])
@parser_classes([JSONParser])
def add_log(request):
    machine = Machine.objects.get(machine_id=request.data.get("machine_id"))
    if not machine:
        machine_serializer = MachineSerializer(data=request.data)
        if not machine_serializer.is_valid():
            print(machine_serializer.errors)
            return Response(status=400, data=machine_serializer.errors)
        machine_serializer.save()

    log_serializer = LogSerializer(data=request.data)
    if not log_serializer.is_valid():
        print(log_serializer.errors)
        return Response(status=400, data=log_serializer.errors)

    log_serializer.save()
    return Response(status=200)
