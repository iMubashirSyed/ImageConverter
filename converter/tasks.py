from celery import shared_task
from PIL import Image
from django.core.files.storage import default_storage
from .models import ImageUpload
import io

@shared_task
def convert_image_to_png(image_id):
    image_instance = ImageUpload.objects.get(id=image_id)

    # Open the original image
    with image_instance.original_image.open('rb') as f:
        im = Image.open(f).convert('RGB')
    
    # Convert and save the image in memory
    output_image = io.BytesIO()
    im.save(output_image, format='PNG')
    output_image.seek(0)

    # Save the converted image to the model
    image_instance.converted_image.save(f'{image_id}_converted.png', output_image)
    image_instance.save()
