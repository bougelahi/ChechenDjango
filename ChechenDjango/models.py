from django.db import models


class Author(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=255)


class Story(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)


class PersonType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)


class AuthorStory(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    story = models.ForeignKey("Story", on_delete=models.CASCADE)


class PersonStory(models.Model):
    id = models.IntegerField(primary_key=True)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    personType = models.ForeignKey("PersonType", on_delete=models.CASCADE)
    story = models.ForeignKey("Story", on_delete=models.CASCADE)
    subName = models.CharField(max_length=255)
