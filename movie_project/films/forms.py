from .models import FilmPost
from django.forms import ModelForm, TextInput, Textarea


class FilmPostForm(ModelForm):
    class Meta:
        model = FilmPost
        fields = ['title', 'description', 'review']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название фильма',
                'id': 'id_title'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание фильма',
                'id': 'id_description'
            }),
            "review": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отзыв',
                'id': 'id_review'
            })
        }
