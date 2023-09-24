from django.shortcuts import render
from django.contrib.auth import login , logout , authenticate
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListCreateAPIView
from .serializers import *
# Create your views here.

# API App Content...
class CRUD_TwotViewSet(viewsets.ViewSet):
    """
        Test Api....
    """
    throttle_scope = ('question')
    serializers_class = TwitSerializer
    queryset = Twit.objects.all()

    def list(self, request):
        queryset = self.queryset
        srz_data = self.serializers_class(instance=queryset , many = True)
        return Response(data=srz_data.data)

    def create(self, request):
        srz_data = self.serializers_class(data=request.POST)
        if srz_data.is_valid():
            vd = srz_data.validated_data
            Twit.objects.create(
                user = request.user,
                img = vd['img'],
                description = vd['description'],
            )
            return Response(data=srz_data.data)
        return Response(srz_data.errors)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.get(id = pk)
        srz_data = self.serializers_class(instance=queryset)
        return Response(data=srz_data.data)

    def partial_update(self, request, pk=None):
        queryset = self.queryset.get(id = pk)
        srz_data = self.serializers_class(instance=queryset , data= request.POST , partial = True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data = srz_data.data)
        return Response(srz_data.errors)

    def destroy(self, request, pk=None):
        queryset = self.queryset.get(id = pk)
        queryset.delete()
        queryset.save()
        return Response({'Massage':'Twit Deleted...'})
    
class ListCreateCommentTwitAPIView(ListCreateAPIView):
    """
        Test Api....
    """
    throttle_scope = ('question')
    queryset = CommentTwit.objects.all()
    serializer_class = CommentTwitSerializer

class RetrieveUpdateDestroyCommentTwitAPIView(RetrieveUpdateDestroyAPIView):
    """
        Test Api....
    """
    throttle_scope = ('question')
    queryset = CommentTwit.objects.all()
    serializer_class = CommentTwitSerializer

class ListCreateRelationTwitAPIView(ListCreateAPIView):
    """
        Test Api....
    """
    throttle_scope = ('question')
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer

class RetrieveUpdateDestroyRelationTwitAPIView(RetrieveUpdateDestroyAPIView):
    """
        Test Api....
    """
    throttle_scope = ('question')
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer

class ListCreateSaveTwitAPIView(ListCreateAPIView):
    """
        Test Api....
    """
    throttle_scope = ('question')
    queryset = SaveTwit.objects.all()
    serializer_class = SaveTwitSerializer

class RetrieveUpdateDestroySaveTwitAPIView(RetrieveUpdateDestroyAPIView):
    """
        Test Api....
    """
    throttle_scope = ('question')
    queryset = SaveTwit.objects.all()
    serializer_class = SaveTwitSerializer

# API App Accounts...

class LoginAPIView(APIView):
    """
        Test Api....
    """
    throttle_scope = ('question')
    serializer_class = UserLoginSerializer

    def post(self,request):
        srz_data = self.serializer_class(data=request.POST)
        if srz_data.is_valid():
            vd = srz_data.validated_data
            user = authenticate(
                email = vd['email'],
                password = vd['password'],
            )
            if user is not None:
                login(request , user)
                return Response(data = srz_data.data)
        return Response(srz_data.errors)
    
class SinginAPIView(APIView):
    """
        Test Api....
    """
    throttle_scope = ('question')
    serializer_class = UserSinginSerializer

    def post(self,request):
        srz_data = self.serializer_class(data=request.POST)
        if srz_data.is_valid():
            vd = srz_data.validated_data
            User.objects.create_user(
                email= vd ['email'],
                username = vd['username'],
                password = vd['password'],
            )
            return Response(data = srz_data.data)
        return Response(srz_data.errors)
    
class LogoutAPIView(APIView):
    """
        Test Api....
    """
    throttle_scope = ('question')

    def get(self,request):
        logout(request)
        return Response({'Massage':'User Logouted...'})
    
class ListCreateFollwUserAPIView(ListCreateAPIView):
    """
        Test Api....
    """
    throttle_scope = ('question')
    queryset = UserFollw_UnFollw.objects.all()
    serializer_class = UserFollw_UnFollwSerializer

class RetrieveUpdateDestroyFollwUserAPIView(RetrieveUpdateDestroyAPIView):
    """
        Test Api....
    """
    throttle_scope = ('question')
    queryset = UserFollw_UnFollw.objects.all()
    serializer_class = UserFollw_UnFollwSerializer
    