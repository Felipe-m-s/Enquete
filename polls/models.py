from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create your models here.
class Deputado(models.Model):
    name = models.CharField(max_length=150)
    imagem = models.FileField(upload_to='images/deputados/', null=True, blank=True)
    partido = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField("Pergunta")
    pub_date = models.DateTimeField("Data de publicação")
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    deputados_relacionados = models.ManyToManyField('Deputado')
    
    def __str__(self):
        return self.choice_text
    
    def save(self, user = None, *args, **kwargs):
        if self.id is not None and user is not None:
            question_user = QuestionUser.objects.filter(question=self.question, user=user).count()
            
            if question_user > 0:
                raise ValidationError("Não é permitido votar mais de uma vez.")
            
            question_user = QuestionUser(question=self.question, user=user)
            question_user.save()
        super(Choice, self).save(*args, **kwargs)

class QuestionUser(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
