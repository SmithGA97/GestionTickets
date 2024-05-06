import cloudinary
import cloudinary.uploader

class CloudDinaryService:
    def __init__(self) -> None:
        self.cloud_name = "dggisjqqs"
        self.api_key = "185955272195195"
        self.api_secret = "LgDDb1f2TVVJ8f7Suggf5xhpgC4"
        cloudinary.config( 
            cloud_name = self.cloud_name, 
            api_key = self.api_key, 
            api_secret = self.api_secret 
        )
    def upload_asset(self, validated_data, title, folder):
        response = cloudinary.uploader.upload(validated_data, public_id=title, folder=folder)
        return response
