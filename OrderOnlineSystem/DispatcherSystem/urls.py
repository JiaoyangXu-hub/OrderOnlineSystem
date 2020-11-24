from django.urls import path

from . import views

urlpatterns = [
    path('', views.base_view),
    path('getCash/',views.getCash_view),
    path('dealItem/',views.dealItem_view)
]