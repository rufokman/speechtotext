from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from apps.stt.forms import *
from django.contrib import messages
from django.http.response import JsonResponse

from apps.stt.services.speech_recognize import speech_recognition
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def record(request):

    if request.method == "POST":
        print("POST")
        print(request.FILES)
        audio_file = request.FILES.get("audio_data")
        print(audio_file)
        print(type(audio_file))
        #text=speech_recognition(audio_file)
        #print(text)
        record = Record.objects.create(voice_record=audio_file)
        record.save()
        # messages.success(request, "Audio recording successfully added!")
    context = {"page_title": "Record audio"}
    return render(request, "stt/record.html", context)


def record_detail(request, id):
    record = get_object_or_404(Record, id=id)
    context = {
        "page_title": "Recorded audio detail",
        "record": record,
    }
    return render(request, "stt/record_detail.html", context)


def index(request):
    records = Record.objects.all()
    context = {"page_title": "Voice records", "records": records}
    return render(request, "stt/index.html", context)

