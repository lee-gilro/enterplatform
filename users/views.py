from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from enterplatform.settings import SECRET_KEY
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User
from . import serializers

class Auth(APIView):
    # 유저 정보 확인
   
    def get(self, request):
        access = request.COOKIES.get('access', None)

        if access is not None:
            try:
                # access token을 decode 해서 유저 id 추출 => 유저 식별
                payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
                pk = payload.get('user_id')
                user = get_object_or_404(User, pk=pk)
                serializer = serializers.UserSerializer(instance=user)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except(jwt.exceptions.ExpiredSignatureError):
                # 토큰 만료 시 토큰 갱신
                data = {'refresh': request.COOKIES.get('refresh', None)}
                serializer = TokenRefreshSerializer(data=data) # type: ignore
                if serializer.is_valid(raise_exception=True):
                    access = serializer.data.get('access', None)
                    refresh = serializer.data.get('refresh', None)
                    payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256']) # type: ignore
                    pk = payload.get('user_id')
                    user = get_object_or_404(User, pk=pk)
                    serializer = serializers.UserSerializer(instance=user)
                    res = Response(serializer.data, status=status.HTTP_200_OK)
                    res.set_cookie('access', access) # type: ignore
                    res.set_cookie('refresh', refresh) # type: ignore
                    return res
                raise jwt.exceptions.InvalidTokenError

            except(jwt.exceptions.InvalidTokenError):
                # 사용 불가능한 토큰일 때
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            # 로그인하지 않은 사용자의 경우, 이 부분을 실행합니다.
            # 예를 들어, 로그인하지 않은 사용자에게는 비어있는 데이터를 반환할 수 있습니다.
            return Response({"detail": "로그인이 필요한 기능입니다."}, status=status.HTTP_200_OK)

    # 로그인
    def post(self, request):
    	# 유저 인증
        user = authenticate(
            email=request.data.get("email"), password=request.data.get("password")
        )
        # 이미 회원가입 된 유저일 때
        if user is not None:
            serializer = serializers.UserSerializer(user)
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "status_code":200,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            max_age = 3 * 60 * 60  # 3 hours in seconds
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access", access_token, max_age=max_age, httponly=True)
            res.set_cookie("refresh", refresh_token, max_age=max_age, httponly=True)
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # 로그아웃
    def delete(self, request):
        # 쿠키에 저장된 토큰 삭제 => 로그아웃 처리
        response = Response({
            "message": "Logout success"
            }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
        

class Register(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            max_age = 3 * 60 * 60  # 3 hours in seconds
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access", access_token, max_age=max_age, httponly=True)
            res.set_cookie("refresh", refresh_token, max_age=max_age, httponly=True)
            
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)