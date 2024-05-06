# Create your views here.
from rest_framework import authentication, permissions, viewsets, mixins
from .serializers import ImageSerializer
from .models import Image


# Create your views here.
class ImageCreateAPIViewset(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
