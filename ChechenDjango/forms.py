from django import forms

from .models import PersonStory, PersonType, Person, Story, Author, AuthorStory


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = "__all__"


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"


class PersonTypeForm(forms.ModelForm):
    class Meta:
        model = PersonType
        fields = "__all__"


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class PersonStoryForm(forms.ModelForm):
    class Meta:
        model = PersonStory
        fields = "__all__"


class AuthorStoryForm(forms.ModelForm):
    class Meta:
        model = AuthorStory
        fields = "__all__"
