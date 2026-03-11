from django.test import TestCase
from django.db import IntegrityError
from datetime import date
from projects.models import TravelProject, Place


class TravelProjectModelTests(TestCase):

    def test_create_travel_project(self):
        project = TravelProject.objects.create(
            name="Trip to Paris",
            description="Holidays in France",
            start_date=date(2024, 6, 15)
        )
        self.assertEqual(project.name, "Trip to Paris")
        self.assertEqual(project.description, "Holidays in France")
        self.assertEqual(project.start_date, date(2024, 6, 15))
        self.assertFalse(project.completed)
        self.assertIsNotNone(project.created_at)

    def test_travel_project_str_method(self):
        project = TravelProject.objects.create(name="Travel to Italy")
        self.assertEqual(str(project), "Travel to Italy")


class PlaceModelTests(TestCase):

    def setUp(self):
        self.project = TravelProject.objects.create(
            name="European tour",
            description="Visiting several European countries"
        )

    def test_create_place(self):
        place = Place.objects.create(
            project=self.project,
            external_id=1,
            title="Eiffel Tower",
            visited=True
        )
        self.assertEqual(place.project, self.project)
        self.assertEqual(place.external_id, 1)
        self.assertEqual(place.title, "Eiffel Tower")
        self.assertTrue(place.visited)

    def test_place_str_method(self):
        place = Place.objects.create(
            project=self.project,
            external_id=2,
            title="Coliseum"
        )
        expected = "Coliseum (European tour)"
        self.assertEqual(str(place), expected)

    def test_unique_external_id_per_project(self):
        Place.objects.create(
            project=self.project,
            external_id=1,
            title="First place"
        )

        with self.assertRaises(IntegrityError):
            Place.objects.create(
                project=self.project,
                external_id=1,
                title="Second place"
            )
