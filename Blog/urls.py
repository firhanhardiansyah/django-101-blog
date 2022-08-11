from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_blog, name='index-blog'),
    path('create/', views.create_blog, name='create-blog'),
    path('update/<int:pk>', views.update_blog, name='update-blog'),
    path('delete/<int:pk>', views.delete_blog, name='delete-blog'),
]
