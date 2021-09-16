# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# from .models import Account


# class AccountInline(admin.StackedInline):
#     model = Account
#     can_delete = False
#     verbose_name_plural = 'Accounts'
#     # serarch
#     list_filter = ('user__username',)
#     search_fields = ['user__motorcycle_registration']


# class CustomizedUserAdmin(UserAdmin):
#     inlines = (AccountInline,)
#     search_fields = ('username', 'email',)


# admin.site.unregister(User)
# admin.site.register(User, CustomizedUserAdmin)


# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'first_name_en',
        'last_name_en',
        'birthday',
        'address',
        'phone_number',
        'bank_account_number',
        'bank_account',
        'bill_number',
        'motorcycle_registration',
        'car_registration',
        'gender',
        'image_profile',
        'image_bill',
        'current_state',
        'is_booking_state',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'user',
        'birthday',
        'is_booking_state',
        'created_at',
        'updated_at',
    )
    date_hierarchy = 'created_at'
    search_fields = ('first_name_en', 'last_name_en', 'birthday',
                     'address', 'motorcycle_registration', 'car_registration')
