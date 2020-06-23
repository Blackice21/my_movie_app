from django.urls import path
<<<<<<< HEAD
from .views import home_page, create, edit, delete


urlpatterns = [
    path('', home_page, name='home_page'),
    path('create/', create, name='create'),
    path('edit/<str:movie_id>', edit, name='edit'),
    path('delete/<str:movie_id>', delete, name='delete')
]
=======
from . import views

urlpatterns = [
    path("", views.home_page, name='home_page'),
    path("create/", views.create, name='create'),
    path('edit/<str:movie_id>/', views.edit, name='edit'),
    path('delete/<str:movie_id>/', views.delete, name='delete')
]
>>>>>>> step_0_start
