from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Page1(models.Model):
  name = models.CharField(max_length=20)
  question1 = models.CharField(max_length=50,default='')
  likes = models.ManyToManyField(User, related_name='likes', blank=True)
  EVENT_CHOICES = (
        ('E', 'Excellent'),
        ('G', 'Good'),
        ('A', 'Average'),
        ('P', 'Poor'),
  )
  question = models.CharField(
        max_length=10,
        choices=EVENT_CHOICES,
        default='G',
        blank=False,
  )
  # DIRECTION_UP ='M'
  # DIRECTION_DOWN ='F'
  # DIRECTION_CHOICES = (
  #     (DIRECTION_UP, 'Male'),
  #     (DIRECTION_DOWN, 'Female'),
  # )  
    
  # gender = models.CharField(max_length=1, choices=DIRECTION_CHOICES,default='M')
  
   	
  CARD_CHOICES = (
        ('V', 'Visa'),
        ('M', 'MasterCard'),
        ('P', 'Paypal'),
  )
  card = models.CharField(
        max_length=10,
        choices=CARD_CHOICES,
        default='V',
        blank=False,
  )
  

  def total_likes(self):
    return self.likes.count()



  def __str__(self):
    return self.name

class Question(models.Model):
  question = models.TextField(max_length=200,default="")
  option1 = models.CharField(max_length=50,default="")
  option2 = models.CharField(max_length=50, default="")
  option3 = models.CharField(max_length=50, default="")
  option4 = models.CharField(max_length=50, default="")

  def __str__(self):
    return self.question


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name= models.CharField(max_length=50)
#     email_id = models.EmailField(max_length=50)
#     contact_no = models.CharField(max_length=10)


#     def __str__(self):
#         return "Profile of user {}".format(self.user.username)

class vcet(models.Model):
  #user = models.OneToOneField(User, on_delete=models.CASCADE)
  review = models.CharField(max_length=50,null=True,blank=True)
  EVENT_CHOICES = (
        ('E', 'Excellent'),
        ('G', 'Good'),
        ('A', 'Average'),
        ('P', 'Poor'),
  )
  question = models.CharField(
        max_length=10,
        choices=EVENT_CHOICES,
        default='G',
        blank=False,
  )
  EVENT_CHOICES1 = (
        ('E1', 'Excellent'),
        ('G1', 'Good'),
        ('A1', 'Average'),
        ('P1', 'Poor'),
  )
  question1 = models.CharField(
        max_length=10,
        choices=EVENT_CHOICES1,
        default='G1',
        blank=False,
  )
  EVENT_CHOICES2 = (
        ('E2', 'Excellent'),
        ('G2', 'Good'),
        ('A2', 'Average'),
        ('P2', 'Poor'),
  )
  question2 = models.CharField(
        max_length=10,
        choices=EVENT_CHOICES2,
        default='G2',
        blank=False,
  )
  EVENT_CHOICES3 = (
        ('E3', 'Excellent'),
        ('G3', 'Good'),
        ('A3', 'Average'),
        ('P3', 'Poor'),
  )
  question3 = models.CharField(
        max_length=10,
        choices=EVENT_CHOICES3,
        default='G3',
        blank=False,
  )

  def __str__(self):
    return self.question