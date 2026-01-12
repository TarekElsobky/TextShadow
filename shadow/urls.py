from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='Landing'),
    path('generate-key', views.generate_key, name='Generate key'),
    path('hide-message', views.hide_message, name='Hide message'),
    path('extract-message', views.extract_message, name='Extract message'),
]