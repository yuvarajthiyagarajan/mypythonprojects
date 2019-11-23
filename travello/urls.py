from django.urls import path

from . import views

urlpatterns = [
      path('',views.index, name ="index"),
      path('dest_redirect/<destname>/',views.dest_redirect,name = "destination")
]