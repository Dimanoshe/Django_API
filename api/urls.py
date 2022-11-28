from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bills-list', BillsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('bills-upload/', BillsUploadAPIView.as_view(), name='bills-upload')
]