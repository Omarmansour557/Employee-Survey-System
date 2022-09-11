from django.db import models
from employee.models import Employee
# Create your models here

class Questions(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description
class Survey(models.Model):

    SURVEY_TYPE_FOLLOWERS = 'F'
    SURVEY_TYPE_REVERSE = 'R'
    SURVEY_TYPE_GENERAL = 'G'

    SURVEY_TYPE_CHOICES = [
        (SURVEY_TYPE_FOLLOWERS, 'Followers'),
        (SURVEY_TYPE_REVERSE, 'Reverse'),
        (SURVEY_TYPE_GENERAL, 'General'),
    ]

    survey_type = models.CharField(
        max_length=1, choices=SURVEY_TYPE_CHOICES, default=SURVEY_TYPE_FOLLOWERS)
    end_date = models.DateField()
    start_date = models.DateField() 
    description = models.TextField(blank=True, null=True)
    questions = models.ManyToManyField(Questions)
    title = models.CharField(max_length=50)


    @property
    def get_questions(self):
        return self.questions.all()

    @property
    def get_survey_type(self):
        return self.get_survey_type_display()

    def __str__(self):
        return self.title

class Answer(models.Model):
    rating = models.FloatField()
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question}: {self.rating}"

class EmployeeSurvey(models.Model):
    is_submitted =models.BooleanField()
    rater = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='survey_set')
    get_rated = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='get_rated', null=True, blank=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    submited_date = models.DateField(blank=True, null=True)
    answers = models.ManyToManyField(Answer, blank=True)

    @property
    def get_answers(self):
        return self.answers.all()

