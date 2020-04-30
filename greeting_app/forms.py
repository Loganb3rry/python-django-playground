from django import forms
from django.core import validators


# def custom_validation(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name should start with 'Z'")


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']
        if email != verify_email:
            raise forms.ValidationError("Make sure your emails match")

    # bot_catcher = forms.CharField(required=False,
    #                               widget=forms.HiddenInput,
    #                               validators=[validators.MaxLengthValidator(0)])

    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("Gotcha Bot!")
    #     return bot_catcher
