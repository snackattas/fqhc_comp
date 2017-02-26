# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.admin import UserAdmin
# from .models import FQHC, UserProfile
# from .choices import CREDENTIALS
# from django import forms
#
# User = get_user_model()
#
#
# class UserProfileCreationForm(UserCreationForm):
#     """
#     An AgentCreationForm with optional password inputs.
#     """
#     fqhc = forms.ModelChoiceField(
#         queryset=FQHC.objects.all(),
#         required=True)
#     credentials = forms.MultipleChoiceField(choices=CREDENTIALS, required=True)
#     full_name = forms.CharField(max_length=100)
#
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#
#     # def save(self):
#     #     user = super(UserCreationForm, self).save()
#     #     # Create the UserProfile now
#     #     fqhc = form.cleaned_data.get('fqhc')
#     #     fqhc = FQHC.objects.get(id=fqhc)
#     #     credentials = form.cleaned_data.get('credentials')
#     #     full_name = form.clean_data.get('full_name')
#     #     UserProfile(user=user, fqhc=fqhc, credentials=credentials).save()
#
# class UserProfileAdminCreate(UserAdmin):
#     add_form = UserProfileCreationForm
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'fqhc', 'credentials', 'full_name'),
#         }),
#     )
#
#     def save_model(self, request, obj, form, change):
#         super(UserAdmin, self).save_model(request, obj, form, change)
#         user = User.objects.get(username=form.cleaned_data.get("username"))
#         fqhc = form.cleaned_data.get('fqhc')
#         # fqhc = FQHC.objects.get(id=fqhc)
#         credentials = form.cleaned_data.get('credentials')
#         full_name = form.cleaned_data.get('full_name')
#         UserProfile(user=user,
#                     fqhc=fqhc,
#                     credentials=credentials,
#                     full_name=full_name).save()
