from django import forms

from .models import Student


# class StudentForm(forms.Form):
#     name = forms.CharField(label='姓名', max_length=128)
#     sex = forms.ChoiceField(label='性別', choices=Student.SEX_ITEMS)
#     profession = forms.CharField(label='職業', max_length=128)
#     email = forms.EmailField(label='郵箱', max_length=128)
#     qq = forms.CharField(label='QQ', max_length=128)
#     phone = forms.CharField(label='手機', max_length=128)

class StudentForm(forms.ModelForm):
    # def clean_qq(self):
    #     cleaned_data = self.clean_qq['qq']
    #     if not cleaned_data.isdigit():
    #         raise forms.ValidationError('Must be interger!')
    #
    #     return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            'id', 'name', 'sex', 'profession',
            'email', 'qq', 'phone', 'status',
        )
