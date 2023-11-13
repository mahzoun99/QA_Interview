from QA.models import Question, Answer
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['text']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question_id = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all(),
        source='question',
        write_only=True
    )

    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'text']
