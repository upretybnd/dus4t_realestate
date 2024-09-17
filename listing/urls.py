
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing, name='listing'),
    path('<slug:category_slug>/', views.listing, name='posts_by_category'),
    path('<slug:category_slug>/<slug:post_slug>/', views.post_detail, name='post_detail'),
]

