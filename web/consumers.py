import json
from channels.generic.websocket import AsyncWebsocketConsumer


class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the websocket connection
        print("Accepting Connection....")
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"web_{self.room_id}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
			self.room_id,
			self.channel_name
		)
        # Close the websocket connection
        await self.close()

    # Receive message from WebSocket
    async def receive(self, text_data):
        # Deserialize the JSON data
        print("Text data = ", text_data)




