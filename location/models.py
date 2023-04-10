from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=32)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"
