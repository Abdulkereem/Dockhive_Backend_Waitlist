from rest_framework import viewsets
from .models import Waitlist
from .serializers import WaitlistSerializer

class WaitlistViewSet(viewsets.ModelViewSet):
    queryset = Waitlist.objects.all()
    serializer_class = WaitlistSerializer