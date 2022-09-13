from django.shortcuts import render, redirect

from petstragram.main_app.forms.profile_form import ProfileForm
from petstragram.main_app.helpers import get_profile
from petstragram.main_app.models import Pet, PetPhoto


def create_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('index')
    else:
        profile_form = ProfileForm(request.GET)
    context = {
        'profile_form': profile_form,
    }
    return render(request, 'profile_create.html', context)


def edit_profile(request):
    return render(request, 'profile_edit.html')


def show_profile(request):
    profile = get_profile()
    pets = Pet.objects.all()

    # Option 1:
    pet_photos = PetPhoto.objects.filter(tagget_pets__in=pets).distinct()

    # Option 1:
    # pet_photos = PetPhoto.objects.filter(tagget_pets__user_profile=profile).all().distinct()
    pet_photos_likes = sum([photo.likes for photo in pet_photos])
    context = {
        'profile': profile,
        'total_images': len(pet_photos),
        'total_likes': pet_photos_likes,
    }
    return render(request, 'profile_details.html', context)


def delete_profile(request):
    return render(request, 'profile_delete.html')
