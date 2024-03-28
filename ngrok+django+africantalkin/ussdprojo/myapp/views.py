from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/ussd", methods=['POST'])
def ussd():
    if request.method == 'POST':
        text = request.form.get("text", "")
        response = ""

        if text == '':
            response = "CON Welcome to Business Ideas \n"
            response += "Select a category to explore business ideas:\n"

            # Make a request to your Django ussd URL to retrieve categories
            try:
                django_response = requests.post('http://your-django-app-url/ussd', data={'text': ''})
                if django_response.status_code == 200:
                    categories = django_response.text.split('\n')  # Assuming Django view returns categories separated by newlines
                    for idx, category in enumerate(categories, start=1):
                        response += f"{idx}. {category}\n"
                else:
                    response = "END Unable to fetch categories"
            except requests.RequestException as e:
                response = "END Error fetching categories from Django"

        # Add other logic for handling user input, fetching ideas, etc.

        return response
    else:
        return "Only POST requests are allowed for USSD service.", 405

if __name__ == '__main__':
    app.run(debug=True, port=5000)
