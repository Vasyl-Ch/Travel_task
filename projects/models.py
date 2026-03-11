from django.db import models


class TravelProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    project = models.ForeignKey(
        TravelProject,
        related_name="places",
        on_delete=models.CASCADE
    )
    external_id = models.IntegerField()
    title = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    visited = models.BooleanField(default=False)

    class Meta:
        unique_together = ("project", "external_id")

    def __str__(self):
        return f"{self.title} ({self.project.name})"
