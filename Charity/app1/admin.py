from django.contrib import admin
from .models import Profile, Donation, Program, Content, Contact, GuestUser


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')


class DonationAdmin(admin.ModelAdmin):
    list_display = ('guest_user', 'user', 'full_name', 'email', 'phone', 'date', 'amount', 'program', 'status')


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'program_description', 'budget', 'start_date', 'end_date')


class ContentAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title', 'description', 'createdAT')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'date')


class GuestUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


admin.site.register(GuestUser, GuestUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Contact, ContactAdmin)

admin.site.index_template = 'admin/index.html'
admin.site.login_template = 'admin/login.html'
