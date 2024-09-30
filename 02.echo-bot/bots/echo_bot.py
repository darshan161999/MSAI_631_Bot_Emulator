from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
import random

class EchoBot(ActivityHandler):
    def __init__(self):
        self.conversation_state = {}

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome! How can I assist you today?")

    async def on_message_activity(self, turn_context: TurnContext):
        user_message = turn_context.activity.text.lower()
        user_id = turn_context.activity.from_property.id

        if user_id not in self.conversation_state:
            self.conversation_state[user_id] = {"state": "initial"}

        state = self.conversation_state[user_id]["state"]

        if "hello" in user_message or "hi" in user_message:
            response = "Hello! How are you doing today?"
            self.conversation_state[user_id]["state"] = "greeting"
        elif state == "greeting" and ("good" in user_message or "fine" in user_message or "well" in user_message):
            response = "That's great to hear! Is there anything specific you'd like to chat about?"
            self.conversation_state[user_id]["state"] = "topic_selection"
        elif state == "topic_selection":
            if "weather" in user_message:
                response = "The weather is a fascinating topic! Did you know that weather patterns are influenced by both local factors and global climate systems?"
            elif "sports" in user_message:
                response = "Sports are a great way to stay active and have fun. Do you have a favorite sport or team?"
            elif "music" in user_message:
                response = "Music is a universal language! What genre of music do you enjoy the most?"
            else:
                response = "That's an interesting topic! I'd love to learn more about it. Can you tell me what specifically interests you about it?"
            self.conversation_state[user_id]["state"] = "conversation"
        elif "bye" in user_message or "goodbye" in user_message:
            response = "It was great chatting with you! Have a wonderful day!"
            self.conversation_state[user_id]["state"] = "initial"
        else:
            responses = [
                "That's interesting! Tell me more about it.",
                "I see. How does that make you feel?",
                "Fascinating! What else can you share on this topic?",
                "I'm curious to hear your thoughts on that. Can you elaborate?",
                "That's a unique perspective. How did you come to that conclusion?"
            ]
            response = random.choice(responses)

        await turn_context.send_activity(MessageFactory.text(response))