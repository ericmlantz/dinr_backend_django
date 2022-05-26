from django.db import models

# Create your models here.

class Restaurant(models.Model):
  Chinese = 'Chinese'
  Italian = 'Italian'
  Mexican = 'Mexican/Spanish'
  Japanese = 'Japanese'
  American = 'American'
  Thai = 'Thai'
  Indian = 'Indian'
  French = 'French'
  Greek = 'Greek'
  German = 'German'
  British = 'British'
  Other = 'Other'
  TYPES_OF_FOOD_CHOICES = [
    (None, 'Select Type of Food'),
    (Chinese, 'Chinese'),
    (Italian, 'Italian'),
    (Mexican, 'Mexican/Spanish'),
    (Japanese, 'Japanese'),
    (American, 'American'),
    (Thai, 'Thai'),
    (Indian, 'Indian'),
    (French, 'French'),
    (Greek, 'Greek'),
    (German, 'German'),
    (British, 'British'),
    (Other, 'Other'),
  ]
  rest_name = models.CharField("Restaurant Name", blank=False,max_length=150)
  rest_logo = models.ImageField("Restaurant Logo", upload_to ='uploads/')
  rest_desc = models.TextField("Description and Details")
  food_type = models.CharField("Type of Food", max_length=15, choices=TYPES_OF_FOOD_CHOICES, default='None')
  rest_url = models.URLField("Website URL", blank=True)
  rest_phone = models.CharField("Phone Number", blank=True, max_length=20)
  rest_street = models.CharField('Steet Address',max_length=150)
  rest_apt = models.CharField('Apartment Line', max_length=100, blank=True)
  rest_city = models.CharField('City', max_length=100)
  rest_state = models.CharField('State', max_length=2)
  rest_zip = models.CharField('Zip Code', max_length=10)
  
  def __str__(self):
        return self.rest_name

class User(models.Model):
  firstName = models.CharField('First Name',max_length=50)
  lastName = models.CharField('Last Name', max_length=50, blank=True)
  email = models.CharField("Email", max_length=150)
  username = models.CharField('username', max_length=50, unique=True)
  password = models.CharField('Password', max_length=50)
  street_loc = models.CharField('Steet Address',max_length=150)
  apt_loc = models.CharField('Apartment Line', max_length=100,blank=True)
  city_loc = models.CharField('City', max_length=100)
  state_loc = models.CharField('State', max_length=2)
  zip_loc = models.CharField('Zip Code', max_length=10)
  matches = models.ManyToManyField(Restaurant, blank=True)

  def __str__(self):
        return self.username