from django.db import models
from artists.models import Artist
# Create your models here.
class Album(models.Model):
    artist=models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
    )
    name=models.CharField(
        max_length=100,
        default="New Album",
    )
    creation_time=models.DateTimeField(
        auto_now_add=True,
    )
    release_time=models.DateTimeField(
        null=False,
        blank=False
    )
    cost=models.DecimalField(
        decimal_places=10,
        max_digits=20
    )
    def __str__(self):
        return self.name