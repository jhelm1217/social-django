from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import *
from .serializers import *
# Create your views here.


@api_view (['POST'])
@permission_classes([])
def create_user(request):

    user = User.objects.create(
        username = request.data['username'],
    )
    user.set_password(request.data['password'])

    user.save()
    profile = Profile.objects.create(
        user = user, 
        first_name = request.data['first_name'],
        last_name = request.data['last_name']
    )
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_message(request):
    # user = User.objects.get(username=request.data['username']) 
    user = request.user
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!! ", request.data)
    message = Message.objects.create(
        user=user,
        content=request.data['content'],
        image=request.data['image'],
    )
    message.save()
    message_serialized = MessageSerializer(message)
    return Response(message_serialized.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_image(request):
  image_serialized = ImageSerializer(data=request.data)
  if image_serialized.is_valid():
    image_serialized.save()
    return Response(image_serialized.data, status=status.HTTP_201_CREATED )
  return Response(image_serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_message(request):
  message = Message.objects.get(id=request.data['id'])
  message.delete()
  return Response()

   

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_message(request, message_id):
    message = Message.objects.filter(id=message_id).first()
    
    message.content = request.data.get('content', message.content)
    message.save()
    message_serialized = MessageSerializer(message)
    return Response(message_serialized.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serialized_profile = ProfileSerializer(profile, many=False)
    return Response(serialized_profile.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request):
    user = request.user
    messages = Message.objects.all()
    serialized_messages = MessageSerializer(messages, many=True)
    return Response(serialized_messages.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_images(request):
  images = Image.objects.all()
  images_serialized = ImageSerializer(images, many=True)
  return Response(images_serialized.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class MessageViewSet(viewsets.ModelViewSet):
   queryset = Message.objects.all()
   serializer_class = MessageSerializer


class ImageViewSet(viewsets.ModelViewSet):
   queryset = Image.objects.all()
   serializer_class = ImageSerializer



