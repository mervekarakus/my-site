from django.urls import path

from . import views

#http://127.0.0.1:8000/             => index.html e yönlendirilebilir.
#http://127.0.0.1:8000/index        => index.html
#http://127.0.0.1:8000/blogs        => blog.html
urlpatterns = [

    path("", views.index),
    path("index", views.index), # her iki url geldiğinde aynı metot çalışsın.
    path("blogs", views.blogs),
    path("blogs/<int:id>",views.blogdetails),

]