from django.core.exceptions import ValidationError
import re

def iran_phone_validator(phone):
    phone_regex = r'^((\+98|0)9\d{9})$'
    if not re.search(phone_regex, phone):
        raise ValidationError("یک شماره تلفن معتبر وارد کنید")

def min_length_validator(value, min):
    if len(value) < min:
        raise ValidationError(f"طول این مقدار نباید کمتر از {min} باشد")

def max_length_validator(value, max):
    if len(value) > max:
        raise ValidationError(f"طول این مقدار نباید بیشتر از {max} باشد")

def just_number_validator(value):
    if re.search(r"\D", value):
        raise ValidationError("این مقدار باید فقط عدد باشد")

def just_letter_validator(value):
    if not re.match(r'^[a-zA-Z\u0600-\u06FF\s]+$', value):
        raise ValidationError('مقدار معتبر وارد کنید')
    
def no_number_validator(value):
    if re.search(r"\d", value):
        raise ValidationError("عدد مجاز نیست")

def no_space_validator(value):
    if any(c==" " for c in str(value)):
        raise ValidationError("فاصله مجاز نیست")

def white_space_handler(value):
    return  " ".join(value.split())

def required_validator(value):
    if not value:
        raise ValidationError("این مقدار اجباری است")

def contain_at_least_one_number(value):
    if re.search(r'\d', str(value)) is None:
        raise ValidationError("رمز عبور باید حداقل حاوی یک عدد باشد")

def contain_at_least_one_uppercase_letter(value):
    if re.search(r"[A-Z]", value) is None:
        raise ValidationError("این مقدار باید حاوی حداقل یک حرف بزرگ باشد")
    
def contain_at_least_one_lowercase_letter(value):
    if re.search(r"[a-z]", value) is None:
        raise ValidationError("این مقدار باید حاوی حداقل یک حرف کوچک باشد")

def contain_at_least_one_symbol(value):
    if re.search(r"[$&+,:;=?@#|'<>.^*()%!-]", value) is None:
        raise ValidationError("رمز عبور باید حداقل حاوی یک کاراکتر خاص باشد")
    
def licence_plate_validator(value):
    iranian_plate_regex = r'^\d{2}[آ-ی]\d{3}-\d{2}$'
    if not re.match(iranian_plate_regex, value):
        raise ValidationError("یک شماره پلاک معتبر وارد کنید")
    
def iranian_national_code_validator(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError('کد ملی باید 10 رقم باشد')
    
    check = int(value[9])
    total_sum = sum(int(value[x]) * (10 - x) for x in range(9)) % 11

    if (total_sum < 2 and check == total_sum) or (total_sum >= 2 and check + total_sum == 11):
        return True
    else:
        raise ValidationError('کد ملی نامعتبر است')