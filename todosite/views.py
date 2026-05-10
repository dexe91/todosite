from django.shortcuts import render
from .models import Note
from django.utils import timezone
# Create your views here.


def index(request):
    notes = Note.objects.all().order_by("completed", "deadline")
    context = {"notes": notes, "today": timezone.now().date()}

    return render(request, "todosite/index.html", context=context)
