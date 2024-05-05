from .serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer