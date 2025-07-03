from django.contrib import admin

# UserAdmin is a prebuilt admin class provided by Django that defines how the default User model appears and behaves in the Django admin panel.
# We extend and customize it to work with your custom model.

from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):

    list_display =['email', 'username', 'last_login', 'date_joined', 'is_active']           # which field is to be displayed on admin panel
    list_display_links = ('email', 'username')                                              # to open the record by clicking on username and email
    readonly_fields = ('date_joined', 'date_joined')                                        # UserAdmin already treated password as hashed and read only no need to add password explicitly
    # readonly_fields = ('password', 'date_joined', 'date_joined')
    ordering = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)






#                ***** admin panel reset password option is available