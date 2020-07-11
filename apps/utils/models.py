from django.db import models

class Timestamps(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta: #esto agrego sino, task toma como id timestamps
        abstract = True