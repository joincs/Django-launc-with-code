from django.urls import path,re_path
from .views import home,share

app_name = 'fist_app'

urlpatterns = [
    path('',home,name='home'),
    path('<str:ref_id>',share,name='share')
]