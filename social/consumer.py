import json
import uuid
from channels.generic.websocket import WebsocketConsumer
from social.models import Review

class WSConsumer(WebsocketConsumer):
    
    def connect(self):

        self.accept()

        self.send(json.dumps({
            'status' : 200,
            'Message' : 'You have successfully established the connection!', 
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(self.scope["user"])
        # review = text_data_json['message']
        review = Review.objects.create(
            user = self.scope["user"],
            movie_id = text_data_json["movie_id"],
            id=str(uuid.uuid4()),
            body = text_data_json["body"]
        )
        # print("New Review: ",  review)