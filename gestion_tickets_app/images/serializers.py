from .models import Image
from rest_framework import serializers

import cloudinary
import cloudinary.uploader
          
cloudinary.config( 
  cloud_name = "dggisjqqs", 
  api_key = "185955272195195", 
  api_secret = "LgDDb1f2TVVJ8f7Suggf5xhpgC4" 
)


cloudinary.uploader.upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg",
                             public_id="olympic_flag")

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)
    folder = serializers.CharField(write_only=True)#, required=False)
    url_cloud = serializers.URLField(read_only=True)
    class Meta:
        model = Image
        fields = '__all__'

    def create(self, validated_data):
        #import pdb;pdb.set_trace()

        response = cloudinary.uploader.upload(validated_data['image'],
                             public_id=validated_data['tittle'], folder=validated_data['folder'])
        validated_data.pop('image', None)
        validated_data.pop('folder', None)

        ticket = validated_data['ticket_id']
        validated_data['url_cloud'] = response['url']

        if ticket.status != 'COMPLETED':
            ticket.increment_images_count()
        else:
            raise serializers.ValidationError(f'The maximum value of images to upload for the ticket {ticket.id} has been reached')
        
        if ticket.number_of_images > ticket.uploaded_images:
            ticket.status = 'IN_PROCESS'
        elif ticket.number_of_images == ticket.uploaded_images:
            ticket.status = 'COMPLETED'
        ticket.save()
        return super().create(validated_data)
    