from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"


class QuestionSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Question
        fields = [
            "question_text",
            "pub_date",
            "id",
        ]
        expandable_fields = {"choices": (ChoiceSerializer, {"many": True})}
