from rest_framework.response import Response

from QA.models import Question, Answer
from rest_framework import viewsets, status
from QA.serializers import QuestionSerializer, AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(is_deleted=False)
    serializer_class = QuestionSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.answer_set.all().update(is_deleted=True)
        instance.save()


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.filter(is_deleted=False)
    serializer_class = AnswerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        Answer.objects.create(
            text=data["text"],
            question_id=data["question"].id
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


# Used Bullet points and Pycharm debugger for debugging
