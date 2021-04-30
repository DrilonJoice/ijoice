from django.db import models


class Item(models.Model):
	text = models.TextField(default='')

'''
#kay sir 04-13-2021

#class Item(object):
class Item(models.Model)
	#pass
	text = models.TextField(default='')

'''