import os
from celery import shared_task
from .services import CloudDinaryService
from .models import Image

@shared_task()
def cloudinary_process(file_path, image_id, title, folder):
    cloud_service = CloudDinaryService()
    response = cloud_service.upload_asset(file_path, title, folder)
    if os.path.exists(file_path):
        os.remove(file_path)
    image = Image.objects.get(pk=image_id)
    image.cloud_info = response
    image.save()
