from rest_framework import serializers
from .models import TravelProject, Place
from .services import get_artwork


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = [
            "id",
            "project",
            "external_id",
            "title",
            "notes",
            "visited",
        ]
        read_only_fields = ["project", "title"]

    def validate_external_id(self, value):

        artwork = get_artwork(value)

        if not artwork:
            raise serializers.ValidationError("Artwork does not exist")

        return value

    def create(self, validated_data):

        artwork = get_artwork(validated_data["external_id"])

        validated_data["title"] = artwork["title"]

        return super().create(validated_data)


class TravelProjectSerializer(serializers.ModelSerializer):

    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = TravelProject
        fields = [
            "id",
            "name",
            "description",
            "start_date",
            "completed",
            "places",
        ]
