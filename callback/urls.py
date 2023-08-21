from django.urls import path
from . import views


app_name = 'callback_me'


urlpatterns = [
    path('', views.CallbackRequestView.as_view(), name='callback'),
]
