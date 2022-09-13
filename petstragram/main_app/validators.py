from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

MAX_FILE_SIZE = 5


def validate_only_letters(value: str):
    if not value.isalpha():
        raise ValidationError('Only letters are allowed')


def validate_file_max_size_in_mb(value):
    filesize = value.file.size
    if filesize > MAX_FILE_SIZE * 1024 * 1024:
        raise ValidationError(f'Max file size is {MAX_FILE_SIZE}')


@deconstructible
class ValidateFileMaxSizeInMb:

    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        pass
