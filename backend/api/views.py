from api.serializers import UserRegistrationSerializer, UserDetailSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import User
from djoser.views import UserViewSet

class UserDetailView(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        data = serializer.errors
        return Response(data, status=status.HTTP_400_BAD_REQUEST)