from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def user_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='user_login'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_user,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def employee_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='employee_login'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_employee,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
