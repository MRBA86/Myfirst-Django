from django.contrib import admin
from website.models import Contact , Newsletter

class ContactAdmin(admin.ModelAdmin):
    ordering = ['created_date']
    list_display = ('name', 'email', 'subject', 'created_date', 'updated_date')
    list_filter = ('email',)
    search_fields = ['name', 'message', 'subject']
    empty_value_display = 'خالی'

admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)

# Register your models here.
