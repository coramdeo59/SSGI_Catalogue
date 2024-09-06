from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from .models import UserFeedbacks
from .models import User

# @admin.register(Feedbacks)
# class YourModelAdmin(admin.ModelAdmin):
#     # Customize the model's appearance and behavior in the admin interface
#     pass

class FeedbackAdmin(admin.ModelAdmin):
  list_display = ("name", "email","message")

# admin.site.register(UserFeedbacks,FeedbackAdmin)

admin.site.register(User)