from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eee', views.index, name='index'),
    path('saveAuthor', views.authorSave, name="saveAuthor"),
    path('editAuthor/<int:id>', views.authorEdit, name="editAuthor"),
    path('deleteAuthor/<int:id>', views.authorDelete, name="deleteAuthor"),

    path('saveStory', views.storySave, name="saveStory"),
    path('editStory/<int:id>', views.storyEdit, name="editStory"),
    path('deleteStory/<int:id>', views.storyDelete, name="deleteStory"),

    path('savePerson', views.personSave, name="savePerson"),
    path('editPerson/<int:id>', views.personEdit, name="editPerson"),
    path('deletePerson/<int:id>', views.personDelete, name="deletePerson"),

    path('savePersonType', views.personTypeSave, name="savePersonType"),
    path('editPersonType/<int:id>', views.personTypeEdit, name="editPersonType"),
    path('deletePersonType/<int:id>', views.personTypeDelete, name="deletePersonType"),

    path('savePersonStory', views.personStorySave, name="savePersonStory"),
    path('editPersonStory/<int:id>', views.personStoryEdit, name="editPersonStory"),
    path('deletePersonStory/<int:id>', views.personStoryDelete, name="deletePersonStory"),

    path('saveAuthorStory', views.authorStorySave, name="saveAuthorStory"),
    path('editAuthorStory/<int:id>', views.authorStoryEdit, name="editAuthorStory"),
    path('deleteAuthorStory/<int:id>', views.authorStoryDelete, name="deleteAuthorStory"),
]
