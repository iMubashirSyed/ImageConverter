from django.shortcuts import render, redirect
from .tasks import convert_image_to_png
from django.http import HttpResponse
from django.core.files.storage import default_storage

# Create your views here.
def home(request):
    # image = request.FILES['image']
    # im = Image.open(image).convert("RGB")
    # im.save('output.png',"PNG")
    
    if request.method == 'POST':
        image = request.FILES['image']
        
        if image.content_type not in ['image/jpeg', 'image/jpg']:
            return HttpResponse('Only JPEG and JPG files are supported', status=400)
        
        image_path = default_storage.save(f'uploads/{image.name}', image)
        task = convert_image_to_png.delay(image_path)
        
        return redirect('download_image')
    
    return render(request, 'index.html')

def download_image(request):
    return render(request, 'download_image.html')