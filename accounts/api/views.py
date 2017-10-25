from django.db.models import Q
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate


from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



from rest_framework.authtoken.models import Token

from rest_framework.generics import (
    CreateAPIView,
   )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

User = get_user_model()


from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    )

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]




class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        import pdb;pdb.set_trace()
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            token = Token.objects.get_or_create(user=serializer)
            new_data['token'] = token.key
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


