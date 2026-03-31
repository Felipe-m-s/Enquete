from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Question(models.Model):
    question_text = models.CharField("Pergunta")
    pub_date = models.DateTimeField("Data de publicação")
    
    def __str__(self):
        return self.question_text
    
    def get_total_votes(self):
        votes = Choice.objects.filter(question=self).aggregate(total=models.Sum('votes'))
        return votes.get('total')
    
    def get_results(self):
        total_votes = self.get_total_votes()
        votes = []
        for choice in self.choice_set.all():
            percentage = 0
            if choice.votes > 0 and total_votes > 0:
                percentage = (choice.votes / total_votes) * 100
            
            votes.append(
                {
                    'choice_text': choice.choice_text,
                    'votes': choice.votes,
                    'percentage': round(percentage, 2)
                }
            )
        return votes
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
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
    