
# AI Chatbot / Calorie and Weight Tracker

The plan is to create a chatbot using the OpenAI GPT-3 model, which will also work as a food logger and weight tracker. I plan to make the bot available to myself via SMS using Twilio and store the data in postgres. This is my first real coding project in a while so we'll see how this goes.

Functions:
- Chat
- Log Foods
- Log Weight
- Report calorie totals for the day, and calories to goal

I would like for the chat to be fairly seamless, recognizing when it needs to add a food to the log or when it needs to respond to questions. My plan is to make the bot a little snarky but we'll see how that goes.

The bot should start by asking GPT-3 if the message contains a reference to food or weight, if so it will

# Open AI Prompts

To start classifying the initial request, I will use the following prompt:

    Classify the following sentence into these categories: eating food, current weight, questions, other.

    "How many calories have I eaten today?"

Show the calories mentioned and item named in the format below.

Example: 
Name: Banana
Calories: 150
Meal: Breakfast

"hamburger, lunch, 600 calories"

Name: Hamburger
Calories: 600
Meal: Lunch

