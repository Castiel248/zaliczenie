from django.db import models
from django import forms

class Form(models.Model):

	def __init__(self, wartosc, miara):
		self.wartosc = wartosc
		self.miara = miara




