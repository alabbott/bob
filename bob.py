import os
from dotenv import load_dotenv
import openai
import psycopg2

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''

def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'

def classifyRequest(message):
    prompt = f'Classify the following sentence into these categories: eating food, current weight, questions, other. "[{message}]"'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer

def handleMessage(message, category):
    if category == "eating food":
        # handle eating food
        return message
    elif category == "current weight":
        # handle
        return message
    elif category == "current weight":
        # handle
        return message
    else:
        # handle
        return message

def executeQuery(query):
    # Connect to the database
    conn = psycopg2.connect(
        host="localhost",
        database="my_database",
        user="postgres",
        password='POSTGRES_PASS'
    )

    # Create a cursor to interact with the database
    cur = conn.cursor()

    # Execute a SQL query
    cur.execute(query)

    # Fetch the query results
    results = cur.fetchall()

    # Loop through the results and print each row
    # for row in results:
    #    print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()

    return results