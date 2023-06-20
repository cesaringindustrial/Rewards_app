import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse 

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """Was_publised_recently returns False for questions whose pub_date is the future"""
        time= timezone.now() + datetime.timedelta(days=30)
        future_question= Question(question_text="Quien es el mejor CD de platzi",pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

def create_question(question_text,days):
    time= timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text= question_text,pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])

    def test_future_question(self):
        create_question("Future question", days= 30)
        response= self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])

    def test_past_question(self): 
        question= create_question("Past question", days= -10)
        response= self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[question])


    def test_future_question_and_past_question(self):
        """
        even if both past and future question exist, only past questions are displayed
        """
        past_question= create_question(question_text="past question", days=-30)
        future_question= create_question(question_text="future question", days=30)
        response= self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[past_question])


    def test_two_past_questions(self):
        """
        The question index page may display multiple question.
        """
        past_question1= create_question(question_text="past question 1", days=-30)
        past_question2= create_question(question_text="past question2", days=-40)
        response= self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[past_question1,past_question2])
