from django.db import models
from django.utils import timezone
import datetime
## Model Question DB no include id because per default include PK
class Question(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date= models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
##esta def es para definir cual fue el ultimo publicado    
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)



## Model Choices DB no include id because per default include PK
## on_delete=models.CASCADE >>> When pass to next question this delete all answers in cascade.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes= models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

