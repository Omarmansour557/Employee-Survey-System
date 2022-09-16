from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from .serializers import WebsocketEmployeeSurveySerializer
class SurveyListConsumer(WebsocketConsumer):
    
    def connect(self):
        #Add the channel assosciated with this instance 
        #to a named group so it can be refernced easily later
        async_to_sync(self.channel_layer.group_add)("survey", self.channel_name)
        self.accept()

    

    def new_survey(self, event):
        """
            New survey handler that communicates with the client,
            recieves a list of employee survey objects, selects the ones appropraite
            to the current user and sends them
        """
        new_surveys = event['new_surveys']
        print('new surveys', new_surveys)
        user_surveys = []
        print(self.scope['user'])
        for survey in new_surveys:
            if survey.rater.user.pk == self.scope['user'].pk:
                serialized_survey = WebsocketEmployeeSurveySerializer(survey)
                user_surveys.append(serialized_survey.data)
                ...
            
        self.send(json.dumps(
            {
                'type':'survey.new',
                'surveys':user_surveys
            }
        ))

class SurveyDetailConsumer(WebsocketConsumer):
    
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("survey-detail", self.channel_name)

        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print('text data', text_data)
        async_to_sync(self.channel_layer.group_send)('survey-detail',{
            'type':'new_answers',
            'status':'editing',
            'answers':text_data
        })

    def new_answers(self, event):
        answers = event['answers']
        if type(answers) == str:
            answers = json.loads(answers)
        self.send(json.dumps(
            {
                'type':'answers.new',
                'status':event['status'],
                'answers': answers
            }
        ))
