import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        me = self.scope['user']
        print(me)
        self.user_id = self.scope['url_route']['kwargs']['id']
        self.channel_group = 'chat_%s' % self.user_id

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.channel_group,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.channel_group,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.channel_group,
            {
                'type': 'chat_message',
                'message': message,
                'username' : username 
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username' : username
        }))
