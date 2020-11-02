from django.db import models


class Questions(models.Model):
    question_id = models.IntegerField(primary_key=True, help_text='Unique Question\'s ID.')
    question_title = models.CharField(max_length=50, help_text='Enter Question\'s Title.')
    question_text = models.CharField(max_length=500, help_text='Enter Question\'s Text.')
    question_answer = models.CharField(max_length=300, help_text='Enter Question\'s Right Answer.')

    def __str__(self):
        return self.question_title


class Choices(models.Model):
    choice_question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300, help_text='Enter Choice\'s Text.')


    def __str__(self):
        return self.choice_text


class ScoreBoard(models.Model):
    name = models.CharField(max_length=300, help_text='Enter Your Name.')
    point = models.IntegerField(default=0)


    def __str__(self):
        return self.name


class XValue(models.Model):
    x_id = models.IntegerField(default=0)
    x_point = models.IntegerField(default=0)


    def __str__(self):
        return str(self.x_id)

