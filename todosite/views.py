from django.shortcuts import redirect, render, get_object_or_404
from .models import Note
from django.utils import timezone
# Create your views here.


def index(request):
    notes = Note.objects.all().order_by("-deadline")
    context = {"notes": notes, "today": timezone.now().date()}

    return render(request, "todosite/index.html", context=context)


def create_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")

        if deadline == "":
            deadline = None

        Note.objects.create(title=title, description=description, deadline=deadline)
        return redirect("index")
    return render(request, "todosite/create_note.html")


def toggle_note(request, note_id):
    if request.method == "POST":
        note = get_object_or_404(Note, id=note_id)

        note.completed = not note.completed
        note.save()
    return redirect(index)


def edit_note(request, note_id):
    pass


def delete_note(request, note_id):
    pass
