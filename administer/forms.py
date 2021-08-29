from django import forms
from dorm.models import Dormitory


class DormitoryForm(forms.ModelForm):
    class Meta:
        model = Dormitory
        fields = ('name', 'images', 'images_room_plan')

    def __init__(self, *args, **kwargs):
        super(DormitoryForm, self).__init__(*args, **kwargs)
        self.fields['images_room_plan'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['images'].widget.attrs.update({'class': 'form-control'})
        # label
        self.fields['name'].label = 'ชื่อหอพัก'
        self.fields['images'].label = 'รูปหอพัก'
        self.fields['images_room_plan'].label = 'รูปชั้นของหอพัก'

        # required fields
        self.fields['name'].required = True
        self.fields['images'].required = True
