from rest_framework import serializers

from apps.problems.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title']
