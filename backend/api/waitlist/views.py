from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Waitlist
from .serializers import WaitlistSerializer
import threading
from .send_mail import send_email

class WaitlistViewSet(viewsets.ModelViewSet):
    queryset = Waitlist.objects.all()
    serializer_class = WaitlistSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')  # Assuming 'email' is the unique identifier

        if email and Waitlist.objects.filter(email=email).exists():
            return Response({"detail": "User with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)
        background_thread = threading.Thread(target=send_email, args=(email, request.data.get('full_name')))
        background_thread.start()

        return super(WaitlistViewSet, self).create(request, *args, **kwargs)
