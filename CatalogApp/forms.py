from categories.models import Category
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        # widgets = {
        #     'name': models.CharField(max_length=25),
        #     'comment': forms.Textarea(attrs={'cols': 100, 'rows': 40})
        # }
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
        # field_classes = {
        #                     'email': EmailCoffeehouseFormField
        #                 },
        localized_fields = '__all__'
