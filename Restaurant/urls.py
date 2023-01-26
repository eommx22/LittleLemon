#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    
    #path('', views.index, name='index')
    path('menu-items/', views.MenuItemsView.as_view()),
    path('meni-items/<int:pk>', views.SingleMenuItemView.as_view()),
    
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]