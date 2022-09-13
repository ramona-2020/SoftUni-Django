from django.shortcuts import render, redirect

from petstragram.main_app.models import PetPhoto


def show_photo_details(request, pk):
    # get pet photo by primary key (pk) = id (picture id)
    pet_photo = PetPhoto.objects.get(pk=pk)
    context = {
        'pet_photo': pet_photo,
        'tagged_pets': PetPhoto.objects.prefetch_related('tagget_pets__petphoto_set__tagget_pets').all(),
    }
    return render(request, 'photo_details.html', context)


def like_pet_photo(request, pk):
    # Like pet photo with pk
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1

    pet_photo.save()

    # redirects to pet photo detail page with same 'pk'
    return redirect('pet photo details', pk)


def create_pet_photo(request):
    return render(request, 'photo_create.html')


def edit_pet_photo(request, pk):
    pass
