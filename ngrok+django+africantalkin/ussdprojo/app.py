import http.client
import json
from django.http import HttpResponse

def ussd(request):
    text = request.POST.get("text", "")
    response = ""

    if text == '':
        response = "CON Welcome to Business Ideas \n"
        response += "Select an option:\n"
        response += "1. Explore business ideas\n"
        response += "2. Ask a question\n"
    elif text == '1':
        # Code to display business ideas (same as before)
        pass
    elif text == '2':
        # Ask the user to enter their question
        response = "CON Enter your question:\n"
    elif text.startswith('2.'):
        # Extract the user's question
        user_question = text[2:].strip()
        
        # Call the AI service to get a response
        ai_response = get_ai_response(user_question)

        # Display the AI response to the user
        response = f"END {ai_response}"

    return HttpResponse(response)

def get_ai_response(question):
    conn = http.client.HTTPSConnection("chatgpt-api8.p.rapidapi.com")

    payload = [
        {
            "content": question,
            "role": "user"
        }
    ]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "3500609806msh05d65f788c7b82bp1f35b4jsn1d74d808c573",
        "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
    }

    conn.request("POST", "/", json.dumps(payload), headers)

    res = conn.getresponse()
    data = res.read()
    response_json = json.loads(data.decode("utf-8"))

    # Extract the AI response
    ai_response = response_json[0].get('content', 'No response from AI')

    return ai_response
