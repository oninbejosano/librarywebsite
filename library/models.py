from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
import datetime

book_type = (
        ('Book', 'Book'),
        ('Magazines', 'Magazines'),
        ('Thesis', 'Thesis'),)
book_status = (
        ('Out', 'Out'),
        ('Reserved', 'Reserved'),
        ('Available', 'Available'),)

book_genre = (
        ('narrative', 'Narrative'),('essays', 'Essays'),
		('biography', 'Biography'),('speech', 'Speech'),
		('nonfiction', 'Nonfiction'),('drama', 'Drama'),
		('poetry', 'Poetry'),('fantasy', 'Fantasy'),
		('humor', 'Humor'),('fable', 'Fable'),
		('fairy_tales', 'Fairy Tales'),('horror', 'Horror'),
		('legend', 'Legend'),('mystery', 'Mystery'),
		('fiction', 'Fiction'),('mythology', 'Mythology'),)

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year


class Book(models.Model):
	location = models.IntegerField(default=000,
        validators=[MaxValueValidator(999), MinValueValidator(1)])
	bookname = models.CharField(max_length = 100)
	authorname = models.CharField(max_length = 100)
	publisher = models.CharField(max_length = 100)
	year_publish = models.IntegerField(('year'), default=current_year)
	booktype = models.CharField(max_length=25,choices=book_type)
	tags= models.CharField(max_length=25,choices=book_genre)
	bookstatus = models.CharField(max_length=25,choices=book_status)

	def __str__(self):
	    return self.bookname
