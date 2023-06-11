from django.contrib import admin
from .models import Profile, Donation, Program, Content, Contact


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')


class DonationAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_Name', 'last_Name', 'email', 'phone', 'date', 'amount', 'program')


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'program_description', 'budget', 'start_date', 'end_date')


class ContentAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title', 'description', 'createdAT')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'date')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Contact, ContactAdmin)
