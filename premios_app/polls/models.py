from django.db import models

## Model Question DB no include id because per default include PK
class Question(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date= models.DateTimeField("date published")

## Model Choices DB no include id because per default include PK
## on_delete=models.CASCADE >>> When pass to next question this delete all answers in cascade.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes= models.IntegerField(default=0)


