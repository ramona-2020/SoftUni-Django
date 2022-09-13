from django.contrib import admin

from petstragram.main_app.models import Profile, Pet, PetPhoto


# Inline admin:
class PetInlineAdmin(admin.StackedInline):
    model = Pet


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [PetInlineAdmin]

    list_display = ('id', 'first_name', 'last_name', 'picture', 'description',
                    'date_of_birth', 'email', 'gender')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'date_of_birth', 'user_profile')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo',  'description', 'publication_date', 'likes')
