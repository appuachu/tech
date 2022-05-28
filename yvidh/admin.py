from django.contrib import admin
from . models import *
# Register your models here.

class admi(admin.ModelAdmin):
    list_display = ['disc','discc']
admin.site.register(gal,admi)

class conadmin(admin.ModelAdmin):
    list_display = ['location','time','Phone','Email']
    list_editable = ['location','time','Phone','Email']
admin.site.register(contact)

admin.site.register(event)


admin.site.register(font)