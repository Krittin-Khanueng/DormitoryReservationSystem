from django import forms
from dorm.models import Dormitory, Floor, Room
from booking.models import Opening_booking


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


class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FloorForm, self).__init__(*args, **kwargs)
        self.fields['dorm_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['number'].widget.attrs.update({'class': 'form-control'})
        self.fields['dorm_name'].label = 'ชื่อหอพัก'
        self.fields['number'].label = 'เลขชั้น'

        # required fields
        self.fields['dorm_name'].required = True
        self.fields['number'].required = True


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['floor'].widget.attrs.update({'class': 'form-control'})
        self.fields['room_id'].widget.attrs.update({'class': 'form-control'})

        self.fields['room_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        # is_status boolen fields

        # label
        self.fields['floor'].label = 'ชั้น'
        self.fields['room_id'].label = 'เลขห้อง'
        self.fields['room_type'].label = 'ประเภทห้อง'
        self.fields['amount'].label = 'จำนวนคน'
        self.fields['is_status'].label = 'สถานะ'


class Opening_bookingForm(forms.ModelForm):
    opening_day = forms.DateTimeField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}))

    closed_day = forms.DateTimeField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Opening_booking
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Opening_bookingForm, self).__init__(*args, **kwargs)
        self.fields['academic_year'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['group'].widget.attrs.update({'class': 'form-control'})

        # label
        self.fields['academic_year'].label = 'ปีการศึกษา'
        self.fields['group'].label = 'กลุ่ม'
        self.fields['opening_day'].label = 'วันเปิดจอง'
        self.fields['closed_day'].label = 'วันปิดจอง'
