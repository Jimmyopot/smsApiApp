from django.urls import path

from . import views

app_name = 'credit'

urlpatterns = [
    path('credits/my-python-credentials/', views.create_cemanet_view, name='credentials'),
    path('safaricom_report/', views.safaricom_report, name='safaricom_report'),
    
    path('api/callback/', views.CemanetViewSet.as_view({'get': 'list'}), name='api_callback'),
]
