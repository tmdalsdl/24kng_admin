# videoupload/forms.py
from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=[
            ('animation', '애니메이션'),
            ('movie', '영화'),
            ('custom', '직접입력')
        ],
        required=True
    )
    custom_category = forms.CharField(required=False)
    file_name = forms.CharField(required=True)
    country = forms.ChoiceField(
        choices=[
            ('kr', '한국'),
            ('en', '영어')
        ],
        required=True
    )

    class Meta:
        model = Video
        fields = ['title', 'description', 'thumbnail', 'video', 'category', 'custom_category', 'file_name', 'country']
