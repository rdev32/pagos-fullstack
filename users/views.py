from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignUpSerializer, GetUserSerializer
from .tokens import create_jwt_pair_for_user
from rest_framework import viewsets
from .models import User

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data={
                "status": True,
                "message": "El usuario se creó correctamente",
                "data": serializer.data,
            }, status=status.HTTP_201_CREATED)

        return Response(data={
            "status": False,
            "message": "El usuario no se pudo crear",
            "data": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            idUser = User.objects.get(email=email)

            return Response(data={
                "status": True,
                "message": "Logeado correctamente",
                "data": {
                    "id": idUser.id,
                    "tokens": tokens,
                }
            }, status=status.HTTP_200_OK)

        else:
            return Response(data={
                "status": False,
                "message": "Credenciales incorrectas",
                "data": {}
            }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        return Response(data={
            "status": True,
            "message": "Logeado correctamente",
            "data": {
                "user": str(request.user),
                "auth": str(request.auth)
            }
        }, status=status.HTTP_200_OK)

class GetUsers(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()
