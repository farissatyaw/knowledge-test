from django.urls import path

from . import views

urlpatterns = [
    path("", views.prometheus_metrics, name="prometheus_metrics"),

]