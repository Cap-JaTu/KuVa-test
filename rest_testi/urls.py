from django.urls import path, re_path
from rest_framework.versioning import URLPathVersioning
from . import views

urlpatterns = [
    re_path(
        r'^tree',
        views.tree.API.as_view(),
        name='tree'
    ),
]
