from django.shortcuts import render

from petstragram.main_app.helpers import get_profile
from petstragram.main_app.models import PetPhoto


# Generic views

def show_home(request):
    return render(request, 'home_page.html')


def show_dashboard(request):
    profile = get_profile()
    pet_photos = PetPhoto.objects.filter(tagget_pets__user_profile=profile).all().distinct()

    context = {
        'hide_additional_nav_items': True,
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)
