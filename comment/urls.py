from django.urls import path

app_name = 'comment'

urlpatterns = [
    path('', home, name='home'),
]