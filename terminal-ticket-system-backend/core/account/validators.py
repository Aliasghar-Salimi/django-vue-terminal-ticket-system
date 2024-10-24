from django.core.exceptions import ValidationError
import re

def phone_validator(phone):
    if not phone:
        raise ValidationError("شماره تلفن اجباری است")
    phone_regex = r'^((\+98|0)9\d{9})$'
    if not re.search(phone_regex, phone):
        raise ValidationError("یک شماره تلفن معتبر وارد کنید")
    " ".join(phone.split())


def password_validator(password):
    alpha = []
    if not password:
        raise ValidationError("رمز عبور اجباری است")
    if len(password) < 8:
        raise ValidationError("رمز عبور باید از ۸ کاراکتر بیشتر باشد")
    if not re.search(r'\d', password):
        raise ValidationError("رمز عبور باید حداقل حاوی یک عدد باشد")
    if str(password).isupper():
        raise ValidationError("رمز عبور باید حداقل حاوی یک حرف کوچک باشد")
    if str(password).islower():
        raise ValidationError("رمز عبور باید حداقل حاوی یک حرف بزرگ باشد")
    for letter in str(password):
        if letter.isalpha():
            alpha.append(letter)
    if alpha == []:
        raise ValidationError("رمز عبور باید حداقل حاوی یک حرف باشد")
    if not any(not c.isalnum() for c in str(password)):
        raise ValidationError("رمز عبور باید حداقل حاوی یک کاراکتر خاص باشد")
    if any(c==" " for c in str(password)):        
        raise ValidationError("فاصله مجاز نیست")
