from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import AuthTokenSerializer
# Create your views here.

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
