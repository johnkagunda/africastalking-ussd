import random
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from myapp.models import BusinessIdea, User, Account

@csrf_exempt
def ussd(request):
    if request.method == 'POST':
        text = request.POST.get("text", "")
        session_id = request.POST.get("sessionId", "")
        phone_number = request.POST.get("phoneNumber", "")
        response = ""

        # Check if the session exists or create a new session
        if session_id:
            try:
                user = User.objects.get(session_id=session_id)
            except User.DoesNotExist:
                # Create a new user if session_id doesn't exist
                user = User.objects.create(session_id=session_id)
        else:
            # Create a new session if session_id is not provided
            user = User.objects.create()

        # If the user doesn't have a UID, generate one
        if not user.uid:
            user.uid = User.generate_uid()
            user.save()

        # If user's name and phone number are not set, ask for them
        if not user.name:
            if not text:
                response = "CON Please enter your name:\n"
            else:
                user.name = text.strip()
                user.save()
                response = "CON Please enter your phone number:\n"

        elif not user.phone_number:
            if not text:
                response = "CON Please enter your phone number:\n"
            else:
                user.phone_number = text.strip()
                user.save()

                # Check if the user already has an account
                try:
                    account = Account.objects.get(user=user)
                    response = f"CON Welcome back, {user.name}!\n\n"
                    response += f"Account Details:\n"
                    response += f"User ID: {user.uid}\n"
                    response += f"Phone Number: {user.phone_number}\n"
                    response += f"Balance: {account.balance}\n"
                    response += f"Loan Limit: {account.loan_limit}\n\n"
                except Account.DoesNotExist:
                    # Create an account for the user if it doesn't exist
                    account_balance = 1000  # Default account balance
                    account_loan_limit = 1000  # Default loan limit
                    account = Account.objects.create(user=user, balance=account_balance, loan_limit=account_loan_limit)
                    account.save()

                    response = f"CON Account created successfully for {user.name}!\n\n"
                    response += f"Account Details:\n"
                    response += f"User ID: {user.uid}\n"
                    response += f"Phone Number: {user.phone_number}\n"
                    response += f"Balance: {account.balance}\n"
                    response += f"Loan Limit: {account.loan_limit}\n\n"

                # Add options for checking balance, loan limit, requesting loan, and business ideas
                response += "Select an option:\n"
                response += "1. Check Balance\n"
                response += "2. Check Loan Limit\n"
                response += "3. Business Ideas\n"
                response += "4. Request Loan\n"

        elif text == '1':
            # Logic for checking balance
            account = Account.objects.get(user=user)
            response = f"END Your balance is ${account.balance}\n"
        elif text == '2':
            # Logic for checking loan limit
            try:
                account = Account.objects.get(user=user)
                loan_limit = account.loan_limit
                response = f"END Your loan limit is ${loan_limit}\n"
            except Account.DoesNotExist:
                response = "END Account not found"
        elif text == '3':
            # Logic for displaying business ideas
            business_ideas = BusinessIdea.objects.all()
            if business_ideas:
                response = "END Business Ideas:\n"
                for idx, idea in enumerate(business_ideas, start=1):
                    response += f"{idx}. {idea.category}: {idea.idea}\n"
            else:
                response = "END No business ideas available\n"
        elif text == '4':
            # Logic for requesting a loan
            response = "CON Enter the amount you want to request for a loan:\n"
        else:
            # Invalid choice for subsequent responses
            response = "END Invalid choice"

        return HttpResponse(response)
    else:
        return HttpResponse(status=405)
