from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'', ImageCreateAPIViewset, basename='image')

urlpatterns = [
]
urlpatterns += router.urls