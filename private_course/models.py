from django.db import models

# Create your models here.

COUNTRIES = ('a', 'b')
PAYMENTS = ('1', '2')
CATEGORIES = ('Individual', 'Group')

class PrivateCourse(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  position = models.IntegerField()
  active = models.BooleanField()
  capacity = models.IntegerField()
  hours = models.IntegerField()

  def __unicode__(self):
    return self.title

  class Meta:
    ordering = ['position']
    verbose_name = 'Private Course'
    verbose_name_plural = 'Private Courses'

class MemberShip(models.Model):
  member = models.ForeignKey('Member')
  course = models.ForeignKey(PrivateCourse)
  category = models.CharField(max_length=255)
  
class Member(models.Model):
  name = models.CharField(max_length=255)
  country = models.CharField(max_length=255)
  description = models.TextField()
  dob = models.DateField()
  skype = models.CharField(max_length=255)
  specialization = models.CharField(max_length=255)
  payment = models.CharField(max_length=255)
  courses = models.ManyToManyField(PrivateCourse, through='Membership', related_name='members')

  def __unicode__(self):
    return self.name

