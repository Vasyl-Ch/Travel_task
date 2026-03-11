from django.urls import path
from rest_framework.routers import DefaultRouter
from projects.views import TravelProjectViewSet, PlaceViewSet

router = DefaultRouter()
router.register("projects", TravelProjectViewSet, basename="projects")

urlpatterns = router.urls + [
    path(
        "projects/<int:project_id>/places/",
        PlaceViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="place-list",
    ),
    path(
        "projects/<int:project_id>/places/<int:pk>/",
        PlaceViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="place-detail",
    ),
]
