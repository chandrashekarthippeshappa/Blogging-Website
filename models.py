from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	published = models.DateField(auto_now=True)
	content = models.TextField(blank=True , null=True)
	status = models.CharField(
		max_length=10,
		choices =(
			('Y','Yes'),
			('N','No'),
			),
			default = ('Y','Yes'),
	
		)
	def __str__(self):
		return self.title


class Other(models.Model):
	blog=models.ForeignKey(Blog,on_delete=models.CASCADE,null=True)
	#blog=models.OneToOneField(Blog,on_delete=models.CASCADE)
	#blog=models.ManyToManyField(Blog)
	published_in = models.CharField(max_length=30)
	def __str__(self):
		return self.blog.title