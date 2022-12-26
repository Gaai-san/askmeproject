from django.contrib import admin
from .models import AskmeModel

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('datecreated',)

admin.site.register(AskmeModel, TodoAdmin)

