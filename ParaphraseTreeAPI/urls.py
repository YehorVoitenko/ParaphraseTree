from django.urls import path

from ParaphraseTreeAPI import views

urlpatterns = [
    path("paraphrase/", views.Paraphrase.as_view()),
]
