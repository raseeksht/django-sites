from django.db import models

# Create your models here.


class Laptop(models.Model):
	storageTypeChoice = [
        ('SSD', 'SSD'),
        ('HDD', 'HDD'),
	]
	ssdExpansionChoice = [
    	("available",True),
    	('not available',False),
    ]

	name = models.CharField(max_length=200)
	processor = models.CharField(max_length=200)
	ram = models.CharField(max_length=200)
	storageType = models.CharField(max_length=200,choices=storageTypeChoice)
	storageCapacity = models.CharField(max_length=200)
	display = models.CharField(max_length=200)
	graphics = models.CharField(max_length=200)
	battery = models.CharField(max_length=200)
	ssdExpansion = models.CharField(max_length=200,choices=ssdExpansionChoice,default=True)
	link = models.CharField(max_length=500,default="#")
	price = models.CharField(max_length=20,default="N/A")

	def __str__(self):
		return self.name