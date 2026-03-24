from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField("Pergunta")
    pub_date = models.DateTimeField("Data de publicação")