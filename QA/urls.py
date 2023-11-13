from django.urls import path

from QA.views import QuestionViewSet, AnswerViewSet

questions = QuestionViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
question = QuestionViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

answers = AnswerViewSet.as_view({
    'post': 'create',
})
answer = AnswerViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('questions/', questions, name='questions'),
    path('questions/<int:pk>/', question, name='question'),

    path('answers/', answers, name='answers'),
    path('answers/<int:pk>/', answer, name='answer'),
]
