from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from projects.models import TravelProject, Place
from projects.serializers import TravelProjectSerializer, PlaceSerializer


class TravelProjectViewSet(viewsets.ModelViewSet):

    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["completed"]

    def destroy(self, request, *args, **kwargs):

        project = self.get_object()

        if project.places.filter(visited=True).exists():

            return Response(
                {"error": "Cannot delete project with visited places"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().destroy(request, *args, **kwargs)


class PlaceViewSet(viewsets.ModelViewSet):

    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["visited"]

    def get_queryset(self):

        project_id = self.kwargs["project_id"]

        return Place.objects.filter(project_id=project_id)

    def perform_create(self, serializer):

        project_id = self.kwargs["project_id"]

        project = TravelProject.objects.get(id=project_id)

        if project.places.count() >= 10:
            raise ValidationError("Project cannot contain more than 10 places")

        serializer.save(project=project)

    def perform_update(self, serializer):
        instance = serializer.save()

        project = instance.project

        if not project.places.filter(visited=False).exists():

            project.completed = True
            project.save()
