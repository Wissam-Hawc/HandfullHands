from channels.layers import get_channel_layer
from django.contrib import admin
from django.db.models import F, Sum

from .models import Donation, Program, Content, Contact, GuestUser


class DonationAdmin(admin.ModelAdmin):
    list_display = ('guest_user', 'user', 'full_name', 'email', 'phone', 'date', 'amount', 'program', 'status')

    def delete_model(self, request, obj):
        program = obj.program
        amount = obj.amount
        status = obj.status

        obj.delete()

        if program and status == 'success':
            Program.objects.filter(pk=program.pk).update(raised=F('raised') - amount)

    def delete_queryset(self, request, queryset):
        program_totals = queryset.filter(status='success').values('program').annotate(total_amount=Sum('amount'))

        for program_total in program_totals:
            program_id = program_total['program']
            total_amount = program_total['total_amount']
            Program.objects.filter(pk=program_id).update(raised=F('raised') - total_amount)

        queryset.delete()


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'program_description', 'budget', 'start_date', 'end_date')


class ContentAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title', 'description', 'createdAT')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'date')


class GuestUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


admin.site.register(GuestUser, GuestUserAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Contact, ContactAdmin)

admin.site.index_template = 'admin/index.html'
admin.site.login_template = 'admin/login.html'
