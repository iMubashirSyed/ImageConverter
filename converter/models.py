from django.db import models

# Create your models here.
from django.db import models

class ImageUpload(models.Model):
    original_image = models.ImageField(upload_to='uploads/originals/')
    converted_image = models.ImageField(null=True, blank=True)
    conversion_task_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image {self.id}"
