from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	GENDER_CHOICES = (('none','NONE'),('M', 'Male'),('F', 'Female'))
	MEMBERSHIP_CHIOCES=(('no','NO'),('1 years','1 YEARS'),('5 years','5 YEARS'))
	PRICE_CHIOCES=(('no','NO'),('200','1 YEARS'),('1000','5 YEARS'))

	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	age = models.CharField(max_length=200, null=True)
	gender = models.CharField(default="none",choices=GENDER_CHOICES, max_length=128)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	street = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	code = models.CharField(max_length=200, null=True)
	membership = models.CharField(default="No Membership",choices=MEMBERSHIP_CHIOCES, max_length=128)
	price = models.CharField(default="No",choices=PRICE_CHIOCES, max_length=128)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name
class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name

class Applications(models.Model):
	CATEGORY = (
			('App', 'App'),
			('Web', 'Web'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)
	def __str__(self):
		return self.name

class order(models.Model):
	STATUS = (
			('Published', 'Published'),
			('Working on It', 'Working on It'),
			('Not Published', 'Not Published'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	Applications = models.ForeignKey(Applications, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)
     

	def __str__(self):
		return self.Applications.name

class Question(models.Model):
    customer= models.ForeignKey(Customer,  null=True, on_delete= models.SET_NULL)
    description =models.CharField(max_length=500)
    admin_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.description

class Idea(models.Model):
	customer= models.ForeignKey(Customer,  null=True, on_delete= models.SET_NULL)
	description =models.CharField(max_length=500)
	investor_comment=models.CharField(max_length=200,default='Nothing')
	price = models.CharField(default="No", max_length=128)
	asked_date =models.DateField(auto_now=True)
	def __str__(self):
		return self.description