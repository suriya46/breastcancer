from django.urls import path,include
from . import views
urlpatterns = [
    path('predict/',views.hello),
    path('',views.home)
]
