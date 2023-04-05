from enterplatform.settings import SECRET_KEY
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from . import serializers
from typing import Dict

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = authenticate(
            email=request.data.get("email"), password=request.data.get("password")
        )
        if user is not None:
            serializer = serializers.UserSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            max_age = 3 * 60 * 60  # 3 hours in seconds
            res = Response(
                {
                    "status_code": 200,
                    "message": "login success",
                    "user": serializer.data,
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                        "expire": max_age,
                    },
                },
                status=status.HTTP_200_OK,
            )

            res.set_cookie("access", access_token, max_age=max_age, httponly=True)
            res.set_cookie("refresh", refresh_token, max_age=max_age, httponly=True)
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        response = Response(
            {"message": "Logout success"}, status=status.HTTP_202_ACCEPTED
        )
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response




class UserInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        access = request.COOKIES.get('access', None)

        if access is not None:
            try:
                payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
                pk = payload.get('user_id')
                user = get_object_or_404(User, pk=pk)
                serializer = serializers.UserSerializer(instance=user)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except jwt.exceptions.ExpiredSignatureError:
                data: Dict[str, str] = {'refresh': request.COOKIES.get('refresh', None)}
                serializer = TokenRefreshSerializer(data=data) # type: ignore
                if serializer.is_valid(raise_exception=True):
                    access = serializer.data.get('access', None)
                    refresh = serializer.data.get('refresh', None)
                    if access is not None and refresh is not None:
                        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
                        pk = payload.get('user_id')
                        user = get_object_or_404(User, pk=pk)
                        serializer = serializers.UserSerializer(instance=user)
                        res = Response(serializer.data, status=status.HTTP_200_OK)
                        res.set_cookie('access', access)
                        res.set_cookie('refresh', refresh)
                        return res

            except (jwt.exceptions.InvalidTokenError, jwt.exceptions.ExpiredSignatureError):
                return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"detail": "로그인이 필요한 기능입니다."}, status=status.HTTP_200_OK)

        

class Register(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            max_age = 3 * 60 * 60  # 3 hours in seconds
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                        "expire": max_age,
                    },
                },
                status=status.HTTP_200_OK,
            )
            
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access", access_token, max_age=max_age, httponly=True)
            res.set_cookie("refresh", refresh_token, max_age=max_age, httponly=True)
            
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)