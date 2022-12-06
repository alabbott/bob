
# AI Chatbot / Calorie and Weight Tracker

The plan is to create a chatbot using the OpenAI GPT-3 model, which will also work as a food logger and weight tracker. I plan to make the bot available to myself via SMS using Twilio and store the data in postgres. This is my first real coding project in a while so we'll see how this goes.

Functions:
- Chat
- Log Foods
- Log Weight
- Report calorie totals for the day, and calories to goal

I would like for the chat to be fairly seamless, recognizing when it needs to add a food to the log or when it needs to respond to questions. My plan is to make the bot a little snarky but we'll see how that goes.

The bot should start by asking GPT-3 if the message contains a reference to food or weight, if so it will

Process:
1. Get message from user via whatever method, probably HTTPS request from Twilio
2. Make a call to GPT-3 to classify the request and respond with request type
    1. eating food
    2. current weight
    3. questions
    4. other
3. Use if/elif to handle the message based on classifiction
    1. Eating Food
        1. Have GPT-3 identify the item and calorie count
        2. Add food, calories, time, and user to database
        3. Tell the user that the food was logged!
    2. Current Weight
        1. Have GPT-3 identify the weight
        2. Log the weight to the database
        3. Tell the user the weight was logged
    3. Questions
        1. Have GPT-3 classify into the following categories
            a. Calories today
            b. Calories left to goal
            c. Weight lost
            d. Weight left to go
    4. Other
        1. General chat, send to GPT-3 and get a response


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

