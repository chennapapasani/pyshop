from django.urls import path
from .import views
urlpatterns=[

    path('',views.index),
    path('travel',views.travel),
]