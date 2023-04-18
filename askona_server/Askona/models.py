from django.db import models


def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


class Mattress(models.Model):
    title = models.CharField(max_length=511)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    min_height = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    max_height = models.DecimalField(max_digits=4, decimal_places=1, default=300)
    min_weight = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    max_weight = models.DecimalField(max_digits=4, decimal_places=1, default=300)
    photo = models.ImageField(upload_to=nameFile, blank=True)
    is_curvature = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title
