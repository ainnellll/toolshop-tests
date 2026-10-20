import uuid

EXISTING_CUSTOMER = {
    "email": "customer@practicesoftwaretesting.com",
    "password": "welcome01",
}

SECOND_CUSTOMER = {
    "email": "customer2@practicesoftwaretesting.com",
    "password": "welcome01",
}


def unknown_user():
    """Пользователь, которого не существует: новый email при каждом запуске."""
    return {
        "email": f"nobody-{uuid.uuid4().hex[:8]}@example.com",
        "password": "wrong-password",
    }


def new_customer():
    """Новый пользователь для регистрации: email и пароль уникальные при каждом запуске."""
    unique = uuid.uuid4().hex[:8]
    return {
        "first_name": "Test",
        "last_name": "Student",
        "dob": "2000-01-20",
        "country": "KZ",
        "postal_code": "050001",
        "house_number": "01",
        "street": "Abay Avenue",
        "city": "Almaty",
        "state": "Almaty",
        "phone": "123456789",
        "email": f"student-{unique}@example.com",
        "password": f"Aa1!{uuid.uuid4().hex[:12]}Zq",
    
    }
BILLING_ADDRESS = {
    "country": "KZ",
    "postal_code": "050001",
    "house_number": "01",
    "street": "Abay Avenue",
    "city": "Almaty",
    "state": "Almaty",
}