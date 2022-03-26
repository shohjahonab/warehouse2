from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .serializers import CustomUserSerializer
from rest_framework import generics
from .models import StockUser
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class AuthView(APIView):
    authentication_classes = [TokenAuthentication]
    pass



class RegisterView(generics.CreateAPIView):
    queryset = StockUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer