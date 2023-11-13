from django.test import TestCase
from rest_framework.reverse import reverse

from QA.models import Question, Answer


class AnimalTestCase(TestCase):
    def test_questions_get_list(self):
        response = self.client.get(reverse('questions'))
        self.assertEqual(response.status_code, 200)

    def test_questions_get(self):
        Question.objects.create(text="new?")
        response = self.client.get(reverse('question', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_questions_create(self):
        url = reverse('questions')
        data = {
            "text": "test question?"
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Question.objects.first().text, "test question?")
