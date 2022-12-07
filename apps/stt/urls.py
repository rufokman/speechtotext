from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("record/", views.record, name="record"),

]