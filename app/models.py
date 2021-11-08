from django.db import models
from django.contrib.auth.models import User

from django_quill.fields import QuillField
from django.template.defaultfilters import slugify
    

# Create your models here.
class Group(models.Model):
	class Meta:
		ordering = ['-updated','-created']
	name = models.CharField(max_length=100)
	description = models.TextField(null = True , blank = True)
	created = models.DateTimeField(auto_now_add = True , editable = False)
	updated = models.DateTimeField(auto_now = True , editable = False)
	user = models.ForeignKey(User , on_delete = models.CASCADE ,null = True)	
	slug = models.SlugField(null=True, unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Group, self).save(*args, **kwargs) 


	def __str__(self):
		return f"{self.name}"

class Post(models.Model):
	class Meta:
		ordering = ['-updated','-created']

	title = models.CharField(max_length=500 , null = True)
	summary = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	content = QuillField()
	slug = models.SlugField(null=False, unique=True) 

	user = models.ForeignKey(User , on_delete = models.CASCADE)	
	group = models.ForeignKey(Group , on_delete =models.CASCADE)

	def __str__(self):
		return f"{self.title}"