from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from .models import Reminder
import json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def api_reminders(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            message = data.get("message")
            date = data.get("date")
            time = data.get("time")
            reminder_type = data.get("reminder_type")

            if not all([message, date, time, reminder_type]):
                return JsonResponse({"message": "All fields are required"}, status=400)

            # Validate date and time format
            try:
                datetime.strptime(date, "%Y-%m-%d")
                datetime.strptime(time, "%H:%M")
            except ValueError:
                return JsonResponse({"message": "Invalid date or time format"}, status=400)

            Reminder.objects.create(
                message=message,
                date=date,
                time=time,
                reminder_type=reminder_type
            )

            return JsonResponse({"message": "Reminder created successfully"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)
        except Exception as e:
            logger.exception("Error creating reminder")
            return JsonResponse({"message": "Server error"}, status=500)

    return JsonResponse({"message": "Method not allowed"}, status=405)


# For rendering a simple HTML form (optional)
def index(request):
    return render(request, "index.html")
