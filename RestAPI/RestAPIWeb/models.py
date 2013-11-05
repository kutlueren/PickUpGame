from django.db import models

	
class Results(models.Model):
    name = models.CharField(max_length=200)
    point = models.DecimalField(max_digits=11, decimal_places=2)
	
	#def __unicode__(self):
    #    return self.choice_text
