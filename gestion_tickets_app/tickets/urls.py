from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'', TicketListCreateAPIViewset, basename='ticket')

urlpatterns = [
]
urlpatterns += router.urls