import json
from channels.generic.websocket import AsyncWebsocketConsumer


class DonationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join a group for donation notifications
        await self.channel_layer.group_add(
            "donation_notifications",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the donation notifications group
        await self.channel_layer.group_discard(
            "donation_notifications",
            self.channel_name
        )

    async def donation_notification(self, event):
        print("Donation notification received!")
        message = event["message"]
        print(f"Message: {message}")
        await self.send(text_data=json.dumps({"message": message}))
