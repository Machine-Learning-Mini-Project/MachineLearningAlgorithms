from django.urls import path
from . import views

urlpatterns = [
    path('copyleaks/completed', views.copyleaksComp),
    path('copyleaks/error', views.copyleaksErr),
    path('copyleaks/creditschecked', views.copyleaksCheck)
]