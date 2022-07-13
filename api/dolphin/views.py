from django.shortcuts import render
from rest_framework import status


@api_view(["POST"])
def add_log(request):
    if (
        "name" not in request.data
        or "description" not in request.data
        or "cluster_id" not in request.data
    ):
        return Response(
            data={"error": "incomplete request"}, status=status.HTTP_400_BAD_REQUEST
        )

    cluster = Cluster.objects.filter(id=request.data["cluster_id"]).first()
    if not cluster or request.user != cluster.admin:
        return Response(
            data={"error": "user does not have the rights to edit cluster"},
            status=status.HTTP_403_FORBIDDEN,
        )

    cluster.name = request.data["name"]
    cluster.description = request.data["description"]
    cluster.save()

    return Response(data={"edited": True}, status=status.HTTP_200_OK)
