import time
import schedule
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from apps.stt.forms import *
from apps.stt.services.speech_recognize import speech_recognition
from django.urls import reverse_lazy


@csrf_exempt
def record(request):
    text_db = Record.objects.last()
    if request.method == "POST":
        print("POST")
        audio_file = request.FILES.get("audio_data")
        text=speech_recognition(audio_file)
        print(text)
        messages.info(request, text)
        record = Record.objects.create(voice_record=audio_file, audio_name=text)
        record.save()

    context = {"page_title": "Record audio",
               'text_db': text_db
               }
    return render(request, "stt/record.html", context)

