from django.urls import path

from .import views

app_name = 'rpt'


urlpatterns = [
    path('books/', views.BookView.as_view({'get': 'list'}), name='books'),
    path('callback_report/', views.index, name='callback_report'),
]