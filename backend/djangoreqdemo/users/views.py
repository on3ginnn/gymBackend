from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import get_user_model

from users.serializer import UserSerializer


class UserRegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        # Проверка обязательных полей
        if not username or not password or not email:
            return Response({"message": "Все поля обязательны для заполнения."}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка уникальности username
        if User.objects.filter(username=username).exists():
            return Response({"message": "Пользователь с таким ником уже существует."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Создание пользователя
        user = User.objects.create_user(username=username, email=email, password=password)
               
        return Response({"message": "Пользователь успешно создан"}, status=status.HTTP_201_CREATED)


class UserLoginAPIView(jwt_views.TokenObtainPairView):
    
    def post(self, request, *args, **kwargs):
        # посмотреть как все работает внутри, мозможно это Token.for_user() -> тогда для верификации verify()
        response = super().post(request, *args, **kwargs)
        print(response.__dict__)

        return Response({"tokens": response.data}, status=response.status_code)


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_200_OK)
    

class UserListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    


class UserSearchAPIView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    
    def retrieve(self, request, *args, **kwargs):
        self.kwargs = {"username":request.GET.get("username")}

        return super().retrieve(request, *args, **kwargs)
