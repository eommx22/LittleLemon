from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from django.contrib.auth.models import User
from .serializers import MenuItemSerializer, BookingSerializer

from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication 
from rest_framework.response import Response
from .serializers import UserSerializer


# Create your views here.
# def index(request):
#     return render(request, 'index.html', {})

@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 

class MenuItemsView(ListCreateAPIView):
    authentication_classes([TokenAuthentication])
    permission_classes =[IsAuthenticated]
    queryset= Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    authentication_classes([TokenAuthentication])
    permission_classes=[IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    #lookup_fields = ['title']
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    #permission_classes = [permissions.IsAuthenticated] 