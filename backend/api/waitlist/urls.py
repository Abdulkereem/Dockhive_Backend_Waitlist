from django.urls import path, include
from rest_framework import routers
from .views import WaitlistViewSet

router = routers.DefaultRouter()
router.register(r'waitlist', WaitlistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]