from django.db import models
import uuid
import pycountry


class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    slug = models.SlugField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(null=True, max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Endorsement(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    approved = models.BooleanField(default=False, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.body[:70]


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.body[0:60]


class Question(models.Model):
    TYPES = (
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('Fullstack', 'Fullstack'),
        ('Recruiter', 'Recruiter'),
    )
    answer = models.CharField(max_length=200, choices=TYPES)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.answer


class Country(models.Model):
    TYPES = (
        [(country.name, country.name) for country in pycountry.countries]
    )
    answer = models.CharField(max_length=200, choices=TYPES)
    mapped_answer = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def save(self, *args, **kwargs):

        COUNTRY_NAME_MAPPING = {
            "United States": "United States of America",
            "Korea, Republic of": "South Korea",
            "Russian Federation": "Russia",
        }

        mapped_value = COUNTRY_NAME_MAPPING.get(self.answer, self.answer)
        self.mapped_answer = mapped_value
        self.answer = mapped_value
        super().save(*args, **kwargs)

    def __str__(self):
        return self.answer
