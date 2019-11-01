from django.shortcuts import render, redirect, get_object_or_404

from . import models, forms


def index(request):
    stories = models.Story.objects.all()
    persons = models.Person.objects.all()
    personTypes = models.PersonType.objects.all()
    authors = models.Author.objects.all()
    personStories = models.PersonStory.objects.all()
    authorStories = models.AuthorStory.objects.all()
    return render(request, 'index.html',
                  {'stories': stories,
                   'persons': persons,
                   'personTypes': personTypes,
                   'authors': authors,
                   'personStories': personStories,
                   'authorStories': authorStories})


def authorSave(request):
    if request.method == "POST":
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.id = request.POST['id']
            author.name = request.POST['name']
            author.save()
            return redirect('index')
    else:
        form = forms.AuthorForm()
    return render(request, 'form.html', {'form': form})


def authorEdit(request, id):
    author = get_object_or_404(models.Author, id=id)
    if request.method == "POST":
        form = forms.AuthorForm(request.POST, instance=author)
        if form.is_valid():
            post = form.save(commit=False)
            post.id = request.POST['id']
            post.name = request.POST['name']
            post.save()
            return redirect('index')
    else:
        form = forms.AuthorForm(instance=author)
    return render(request, 'form.html', {'form': form})


def authorDelete(request, id):
    models.Author.objects.filter(id=id).delete()
    return redirect('index')


def storySave(request):
    if request.method == "POST":
        form = forms.StoryForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.id = request.POST['id']
            author.name = request.POST['name']
            author.save()
            return redirect('index')
    else:
        form = forms.StoryForm()
    return render(request, 'form.html', {'form': form})


def storyEdit(request, id):
    story = get_object_or_404(models.Story, id=id)
    if request.method == "POST":
        form = forms.StoryForm(request.POST, instance=story)
        if form.is_valid():
            post = form.save(commit=False)
            post.id = request.POST['id']
            post.name = request.POST['name']
            post.text = request.POST['text']
            post.save()
            return redirect('index')
    else:
        form = forms.StoryForm(instance=story)
    return render(request, 'form.html', {'form': form})


def storyDelete(request, id):
    models.Story.objects.filter(id=id).delete()
    return redirect('index')


def personSave(request):
    if request.method == "POST":
        form = forms.PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.id = request.POST['id']
            person.name = request.POST['name']
            person.save()
            return redirect('index')
    else:
        form = forms.PersonForm()
    return render(request, 'form.html', {'form': form})


def personEdit(request, id):
    person = get_object_or_404(models.Person, id=id)
    if request.method == "POST":
        form = forms.PersonForm(request.POST, instance=person)
        if form.is_valid():
            post = form.save(commit=False)
            post.id = request.POST['id']
            post.name = request.POST['name']
            post.save()
            return redirect('index')
    else:
        form = forms.PersonForm(instance=person)
    return render(request, 'form.html', {'form': form})


def personDelete(request, id):
    models.Person.objects.filter(id=id).delete()
    return redirect('index')


def personTypeSave(request):
    if request.method == "POST":
        form = forms.PersonTypeForm(request.POST)
        if form.is_valid():
            personType = form.save(commit=False)
            personType.id = request.POST['id']
            personType.name = request.POST['name']
            personType.save()
            return redirect('index')
    else:
        form = forms.PersonTypeForm()
    return render(request, 'form.html', {'form': form})


def personTypeEdit(request, id):
    person = get_object_or_404(models.PersonType, id=id)
    if request.method == "POST":
        form = forms.PersonTypeForm(request.POST, instance=person)
        if form.is_valid():
            post = form.save(commit=False)
            post.id = request.POST['id']
            post.name = request.POST['name']
            post.save()
            return redirect('index')
    else:
        form = forms.PersonTypeForm(instance=person)
    return render(request, 'form.html', {'form': form})


def personTypeDelete(request, id):
    models.PersonType.objects.filter(id=id).delete()
    return redirect('index')


def authorStorySave(request):
    if request.method == "POST":
        form = forms.AuthorStoryForm(request.POST)
        if form.is_valid():
            personType = form.save(commit=False)
            personType.id = request.POST['id']
            personType.author = models.Author(id=request.POST['author'])
            personType.story = models.Story(id=request.POST['story'])
            personType.save()
            return redirect('index')
    else:
        form = forms.AuthorStoryForm()
    return render(request, 'form.html', {'form': form})


def authorStoryEdit(request, id):
    person = get_object_or_404(models.AuthorStory, id=id)
    if request.method == "POST":
        form = forms.AuthorStoryForm(request.POST, instance=person)
        if form.is_valid():
            post = form.save(commit=False)
            post.id = request.POST['id']
            post.name = request.POST['name']
            post.save()
            return redirect('index')
    else:
        form = forms.AuthorStoryForm(instance=person)
    return render(request, 'form.html', {'form': form})


def authorStoryDelete(req, id):
    models.AuthorStory.objects.filter(id=id).delete()
    return redirect('index')


def personStorySave(request):
    if request.method == "POST":
        form = forms.PersonStoryForm(request.POST)
        if form.is_valid():
            personType = form.save(commit=False)
            personType.id = request.POST['id']
            personType.person = models.Person(id=request.POST['person'])
            personType.personType = models.PersonType(id=request.POST['personType'])
            personType.story = models.Story(id=request.POST['story'])
            personType.subName = request.POST['subName']
            personType.save()
            return redirect('index')
    else:
        form = forms.PersonStoryForm()
    return render(request, 'form.html', {'form': form})


def personStoryEdit(request, id):
    person = get_object_or_404(models.PersonStory, id=id)
    if request.method == "POST":
        form = forms.PersonStoryForm(request.POST, instance=person)
        if form.is_valid():
            post = form.save(commit=False)
            post.id = request.POST['id']
            post.name = request.POST['name']
            post.save()
            return redirect('index')
    else:
        form = forms.PersonStoryForm(instance=person)
    return render(request, 'form.html', {'form': form})


def personStoryDelete(req, id):
    models.PersonStory.objects.filter(id=id).delete()
    return redirect('index')
