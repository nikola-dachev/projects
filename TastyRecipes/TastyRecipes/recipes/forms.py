from django import forms

from TastyRecipes.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author']
        help_texts = {
            'ingredients': "Ingredients must be separated by a comma and space.",
            'cooking_time': "Provide the cooking time in minutes."
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ingredients'].widget.attrs['placeholder'] = "ingredient1, ingredient2, ..."
        self.fields['instructions'].widget.attrs['placeholder'] = "Enter detailed instructions here..."
        self.fields['image_url'].widget.attrs['placeholder'] = "Optional image URL here..."

class UpdateRecipeForm(CreateRecipeForm):
    pass

class DeleteRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
