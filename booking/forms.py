
from django import forms
from account.models import Account


# Create your forms here.
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('image_profile', 'image_bill')
    # get current account

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['image_profile'].required = True
        self.fields['image_bill'].required = True
        self.fields['image_profile'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['image_bill'].widget.attrs.update(
            {'class': 'form-control'})
        # lable
        self.fields['image_profile'].label = 'รูปตัวเอง'
        self.fields['image_bill'].label = 'รูปบิล'
