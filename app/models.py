from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class PhotoModel(models.Model):
	image = models.ImageField(verbose_name=_("სურათი"),upload_to='photo/', null=True)
	class Meta:
		verbose_name = 'სურათი'
		verbose_name_plural =  'სურათები'