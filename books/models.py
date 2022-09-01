from email.policy import default
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))

    name = models.CharField(max_length=150, blank=False, default='')
    address = models.CharField(max_length=250, blank=True)
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, default=MALE)
    age = models.IntegerField(default=1, validators=[
                              MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f"Author name is {self.name}"


class Book(models.Model):
    name = models.CharField(max_length=150, blank=False,
                            unique=True, default='', error_messages={
                                'required': "Please enter the field name"
                            })
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)
    publishDate = models.DateTimeField()
    NoOfPages = models.IntegerField(
        default=1, validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return f"Book name is {self.name} and is written by {self.author.name}"
