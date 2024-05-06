from rest_framework import serializers
from .models import Image
from .helpers import save_file_tpm
from .tasks import cloudinary_process


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)
    folder = serializers.CharField(write_only=True)
    url_cloud = serializers.URLField(read_only=True)

    class Meta:
        model = Image
        fields = "__all__"

    def create(self, validated_data):
        ticket = validated_data["ticket_id"]
        if ticket.status != "COMPLETED":
            ticket.increment_images_count()
        else:
            raise serializers.ValidationError(
                f"The maximum value of images to upload for the ticket {ticket.id} has been reached"
            )

        file_path = save_file_tpm(validated_data["image"])
        title = validated_data["tittle"]
        folder = validated_data.get("folder")
        validated_data.pop("image", None)
        validated_data.pop("folder", None)
        image = Image.objects.create(**validated_data)
        image_id = image.pk
        cloudinary_process.delay(file_path, image_id, title, folder)

        if ticket.number_of_images > ticket.uploaded_images:
            ticket.status = "IN_PROCESS"
        elif ticket.number_of_images == ticket.uploaded_images:
            ticket.status = "COMPLETED"
        ticket.save()
        return validated_data
