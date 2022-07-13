from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dolphin.models import Log


@api_view(["POST"])
def add_log(request):
    pass
