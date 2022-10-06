from django.db import models

# Create your models here.
class Artist(models.Model):
    stage_name=models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
    )
    social_link=models.URLField(
        null=False,
    )
    def __str__(self):
        return self.stage_name