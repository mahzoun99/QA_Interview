from django.db import models


class BaseModel(models.Model):
    date_created = models.DateTimeField("created", auto_now_add=True)
    date_updated = models.DateTimeField("updated", auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Question(BaseModel):
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)

    def __str__(self):
        return f'(Q{self.question_id}): {self.text}'
