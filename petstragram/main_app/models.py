import datetime
from django.db import models
from django.core.validators import MinLengthValidator
from petstragram.main_app.validators import validate_only_letters, validate_file_max_size_in_mb


class Profile(models.Model):
    # Constants:
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(c, c) for c in (MALE, FEMALE, DO_NOT_SHOW)]

    # Fields (Columns):
    first_name = models.CharField(
        verbose_name="First Name",
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ]
    )

    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ]
    )

    # has default URLValidator
    picture = models.URLField(
        verbose_name="Link to Profile Picture",
    )

    # The user may provide the following information in their profile:
    # i.e. OPTIONAL Fields (null=True, blank=True)
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    # has built-in validate_email
    email = models.EmailField(
        null=True,
        blank=True,
    )

    #  "Male", "Female", and "Do not show"
    gender = models.CharField(
        max_length=max(len(x) for (x, _) in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True
    )

    # One-to-one relations
    # One-to-many relations
    # Many-to-many relation

    # Properties
    # Methods
    # Dunder methods
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Pet(models.Model):
    # Constants:
    NAME_MAX_LENGTH = 30

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    TYPES = [(c, c) for c in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    # "Cat", "Dog", "Bunny", "Parrot", "Fish", or "Other"
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES
    )

    # The user may provide the following information when adding a pet to their profile:
    # i.e. OPTIONAL Fields
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    # One-to-many relations
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    # Properties
    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    # Methods
    # Dunder methods
    def __str__(self):
        return self.name

    # Meta
    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    # the maximum size of the photo can be 5MB
    photo = models.ImageField(
        validators=[
            validate_file_max_size_in_mb,
        ],
        upload_to='photos'
    )

    tagget_pets = models.ManyToManyField(
        Pet
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    publication_date = models.DateTimeField(
        auto_now_add=True
    )

    likes = models.IntegerField(
        default=0
    )
