from .models import FilmPost
from django.forms import ModelForm, TextInput, Textarea


class FilmPostForm(ModelForm):
    class Meta:
        model = FilmPost
        fields = ['title', 'description', 'review']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название фильма'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание фильма'
            }),
            "review": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв'
            })
        }
