from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=("pk","user","phone_number","website","picture")

    list_display_links =("pk","user","phone_number")

    search_fields=('user__email',)

    fieldsets = (
        ('Profile',{
            'fields':(('user','picture'),),
        }),
        ('Extra info',{
            'fields':(
                ('website','phone_number'),
                ('biography')
                ),
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        }),
    )

    readonly_fields = ('created','modified')
#     class Meta:
#         model = Profile

# admin.site.register(Profile, ProfileAdmin)

class ProfileInline(admin.StackedInline):

    model= Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)