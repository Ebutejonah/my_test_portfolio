from django.db import models

class Home(models.Model):
    introduction=models.TextField()
    body=models.TextField()
    web_design=models.TextField(blank=True)
    sites=models.TextField(blank=True)
    machineLearning=models.TextField(blank=True)
    android_ios=models.TextField(blank=True)

class Review(models.Model):
    feedback=models.TextField(blank=False)