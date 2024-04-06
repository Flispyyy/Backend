from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answer_type = models.CharField(max_length=10)  # 'text', 'radio', 'checkbox'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    response = models.CharField(max_length=200)

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()

# Create your models here.
