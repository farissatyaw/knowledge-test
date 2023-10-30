from django.urls import path

from . import views

urlpatterns = [
    path("generate/", views.generate, name="generate"),
    path("download/", views.download, name="download"),
    path("send_mq/", views.send_mq, name="send_mq"),
]