from django.contrib import admin
from .models import ssgi

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("date", "folder",)

admin.site.register(ssgi,MemberAdmin)