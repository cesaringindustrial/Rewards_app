from django.urls import path

from . import views

app_name= "polls"


urlpatterns = [
     #ex:/polls/
    path("",views.index, name="index"),
    #ex:/polls/5/
    path("<int:question_id>/detail/platzi/cuestionario",views.detail, name="detail"),
     #ex:/polls/5/results/
    path("<int:question_id>/results/",views.result, name="results"),
     #ex:/polls/5/vote/
    path("<int:question_id>/vote/",views.vote, name="vote")
]
