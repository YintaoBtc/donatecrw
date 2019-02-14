from django.urls import path
from . import views
from .views import ServiceDetailView, ServiceListView, ServiceCompletedListView

urlpatterns = [
    #path('', views.services, name="services"),
    path('', ServiceListView.as_view(), name='services'),
    path('completed/', ServiceCompletedListView.as_view(), name='completed'),
    path('category/<int:category_id>/', views.category, name = "category"),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service'),
]