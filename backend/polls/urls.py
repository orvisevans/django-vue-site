from django.urls import path, include
from rest_framework import routers
from .views import (
    IndexView,
    DetailView,
    ResultsView,
    vote,
    QuestionViewSet,
    ChoiceViewSet,
)

router = routers.DefaultRouter()
router.register(r"questions", QuestionViewSet)
router.register(r"choices", ChoiceViewSet)


app_name = "polls"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("<int:pk>/results", ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote", vote, name="vote"),
    path("api/", include(router.urls)),
]
