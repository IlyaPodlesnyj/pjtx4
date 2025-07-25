from django.db import models

class DynamicFormData(models.Model):
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.data)




# Create your models here.
