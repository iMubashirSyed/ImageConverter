from celery import shared_task
from PIL import Image
from django.core.files.storage import default_storage

@shared_task
def convert_image_to_png(image_path):
    
    f = default_storage.open(image_path,'rb')
    im = Image.open(f).convert('RGB')
    f.close()
    
    # replace() is used twice cause if the image is in jpg/jpeg it will convert into png
    convert_image = image_path.replace('.jpg', '.png').replace('.jpeg', '.png')
    
    output_image = default_storage.open(convert_image, 'wb')
    im.save(output_image, format='png')
    output_image.close()
    
    return convert_image
    