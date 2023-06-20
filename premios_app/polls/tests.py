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

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])