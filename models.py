# chatbot/models.py
from django.db import models
from django.contrib.auth.models import User


class AyurvedicQuestion(models.Model):
    question = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.question


class AyurvedicOptions(models.Model):
    option = models.CharField(max_length=255)
    question = models.ForeignKey(
        AyurvedicQuestion, on_delete=models.CASCADE, related_name="options"
    )
    dosha = models.CharField(max_length=255)
    

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # question = models.ManyToManyField(AyurvedicQuestion)
    dosha_prediction = models.CharField(max_length= 10, blank= True, null= True )
    option = models.ManyToManyField(AyurvedicOptions)
