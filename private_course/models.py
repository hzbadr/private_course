from django.db import models

# Create your models here.


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
