from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework import permissions

# Create your views here.
# def index(request):
#     return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    queryset= Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    #lookup_fields = ['title']
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    #permission_classes = [permissions.IsAuthenticated] 