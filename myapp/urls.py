from django.urls import path
from.views import*

urlpatterns = [
    path('', index, name="index"),
    path('pages_blank/', pages_blank, name="pages_blank"),
    path('pages_contact/', pages_contact, name="pages_contact"),
    path('pages_error/', pages_error, name="pages_error"),
    path('pages_faq/', pages_faq, name="pages_faq"),
    path('pages_login/', pages_login, name="pages_login"),
    path('pages_register/', pages_register, name="pages_register"),
    path('tables_data/', tables_data, name="tables_data"),
    path('tables_general/', tables_general, name="tables_generals"),
    path('users_profile/', users_profile, name="users_profile"),
]