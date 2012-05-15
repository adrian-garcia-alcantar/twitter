from django.contrib import admin
from main.models import Profile, Tweet


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'head_shot', 'birth_date', 'location',)


class TweetAdmin(admin.ModelAdmin):
    list_display = ('owner', 'status', 'created_at',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tweet, TweetAdmin)
