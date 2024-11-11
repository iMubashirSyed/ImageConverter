from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import ImageUpload
from .tasks import convert_image_to_png
from celery.result import AsyncResult

def home(request):
    if request.method == 'POST':
        image = request.FILES['image']
        
        if image.content_type not in ['image/jpeg', 'image/jpg']:
            return HttpResponse('Only JPEG and JPG files are supported', status=400)

        # Save the original image to the database
        image_instance = ImageUpload.objects.create(original_image=image)
        # call the celery worker for converting the image
        task = convert_image_to_png.delay(image_instance.id)

        # Save the task ID to track conversion progress
        image_instance.conversion_task_id = task.id
        image_instance.save()
        
        return redirect('download_image', task_id=task.id)

    return render(request, 'index.html')

def download_image(request, task_id):
    # AsyncResult is a Celery class used to track the status and result of an asynchronous task
    result = AsyncResult(task_id)
    image_instance = ImageUpload.objects.get(conversion_task_id=task_id)

    if result.ready() and image_instance.converted_image:
        return render(request, 'download_image.html', {
            'converted_image_url': image_instance.converted_image.url,
            'task_ready': True,
            'task_id': task_id
        })
    else:
        return render(request, 'download_image.html', {
            'task_ready': False,
            'task_id': task_id
        })
        
def progress(request, task_id):
    image_instance = ImageUpload.objects.filter(conversion_task_id=task_id).first()
    
    # Checks if an ImageUpload instance exists and if it has a converted image.
    if image_instance and image_instance.converted_image:
        return JsonResponse({
            'status': 'completed',
            'converted_image_url': image_instance.converted_image.url
        })
    # if the image is still processing return status processing.
    else:
        return JsonResponse({'status': 'processing'})
