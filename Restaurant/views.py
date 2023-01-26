from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu
from .serializers import MenuItemSerializer

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