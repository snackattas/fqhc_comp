from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import FQHC, UserProfile, Requirement, SubRequirement, Response


class FQHCAdmin(admin.ModelAdmin):
    fields = ('name', 'address', 'phone_number')
    list_display = ('name', 'phone_number')

class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'full_name', 'fqhc', 'credentials')
    list_display = ('user', 'full_name', 'fqhc')

class RequirementAdmin(admin.ModelAdmin):
    fields = ('step', 'name', 'text')
    list_display = ('step', 'name')

class SubRequirementAdmin(admin.ModelAdmin):
    fields = ('step', 'name', 'text', 'requirement')
    list_display = ('step', 'name', 'requirement')

class ResponseAdmin(admin.ModelAdmin):
    fields = ('fqhc', 'subrequirement', 'response', 'expiration', 'signed')
    list_display = ('fqhc', 'subrequirement', 'response','pdf', 'expiration', 'signed')

admin.site.register(FQHC, FQHCAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Requirement, RequirementAdmin)
admin.site.register(SubRequirement, SubRequirementAdmin)
admin.site.register(Response, ResponseAdmin)
