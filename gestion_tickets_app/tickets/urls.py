from rest_framework import routers
from .views import TicketListCreateAPIViewset

router = routers.DefaultRouter()
router.register(r'', TicketListCreateAPIViewset, basename='ticket')

urlpatterns = [
]
urlpatterns += router.urls
