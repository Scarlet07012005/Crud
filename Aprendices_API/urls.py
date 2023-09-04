from django.urls import path
from .views import AprendicesView

urlpatterns = [
    path('aprendices/', AprendicesView.as_view(), name = 'aprendices_list'),
    path('aprendices/<int:id>', AprendicesView.as_view())
]