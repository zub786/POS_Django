from categories.models import Category
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        # widgets = {
        #     'categoryName': forms.TextInput(attrs={'class': 'myfieldclass'}),
        # },
        labels = {
            'categoryName': 'Category Name',
        }
        # help_texts = {
        #     'comment': 'Provide a detailed account of the issue to receive a quick answer'
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': "Name can only be 25 characters in length"
        #     }
        # }
        field_classes = {
                            'categoryName': 'form-control'
                        },
        localized_fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CategoryForm, self).__init__(*args, **kwargs)
            self.fields['categoryName'].widget.attrs.update({'class': 'form-control'})
