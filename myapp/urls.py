from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_page, name='chat_page'),
    path('get-response/', views.get_bot_response, name='get_response'),
]