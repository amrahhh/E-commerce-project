from django.contrib.auth import authenticate, login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from account.api.serializers import UserLoginSerializer

class CustomAuthToken(APIView):
    # permission_classes = [AnonPermissionOnly]
    def post(self, request, *args, **kwargs):   
        if request.user.is_authenticated:
            return Response({
                'success': False,
                'message': "You are already authenticated",
            }, status=400)
        data = request.data
        username = data.get('username', False)
        password = data.get('password', False)
        if username and password:
            user = authenticate(username=username, password=password, )
            if user:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                serializer = UserLoginSerializer(user)
                return Response({
                    'id': user.id,
                    'success': True,
                    'message': "Success",
                    'token': token.key,
                    "data": serializer.data
                }, status=200)
        return Response({
            'success': False,
            'message': "Invalid credentials",
        }, status=401)