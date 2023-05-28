from django.core.exceptions import ValidationError


def phone_number_validator(value):
    if len(value) != 11:
        raise ValidationError("شماره موبایل بایستی 11 رقم باشد")
