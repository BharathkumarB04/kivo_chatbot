from django.shortcuts import render
from django.http import JsonResponse
from .models import Chat
import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def chatbot_page(request):
    return render(request, 'chat.html')

def get_bot_response(request):
    if request.method == 'POST':
        user_msg = request.POST.get('message')
        try:
            response = model.generate_content(user_msg)
            bot_reply = response.text.strip()
            Chat.objects.create(user_message=user_msg, bot_response=bot_reply)
            return JsonResponse({'response': bot_reply})
        except Exception as e:
            return JsonResponse({'response': "Error from Gemini API"})
