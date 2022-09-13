from django.urls import path, include

from petstragram.main_app.views.generic import show_home, show_dashboard
from petstragram.main_app.views.pet_photos import show_photo_details, like_pet_photo, edit_pet_photo, create_pet_photo
from petstragram.main_app.views.pets import create_pet, edit_pet, delete_pet
from petstragram.main_app.views.profile import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = [
    path('', show_home, name='index'),

    path('dashboard/', show_dashboard, name='dashboard'),

    path('photo/details/<int:pk>/', show_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='pet photo like'),

    path('profile/', include([
        path('', show_profile, name='show profile'),
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('pet/', include([
        path('add/', create_pet, name='create pet'),
        path('edit/<int:pk>/', edit_pet, name='edit pet'),
        path('delete/<int:pk>/', delete_pet, name='delete pet'),
    ])),
    path('pet/', include([
        path('add/', create_pet_photo, name='create pet photo'),
        path('edit/<int:pk>/', edit_pet_photo, name='delete pet photo'),
    ])),
]
