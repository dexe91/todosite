from django.shortcuts import redirect, render, get_object_or_404
from .models import Note
from django.utils import timezone
from datetime import datetime
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
    note = get_object_or_404(Note, id=note_id)
    context = {"note": note}
    if request.method == "POST":
        new_title = request.POST.get("title")
        new_desciption = request.POST.get("description")
        new_deadline = request.POST.get("deadline")

        if new_title:
            note.title = new_title
        if new_desciption:
            note.description = new_desciption
        if new_deadline:
            try:
                note.deadline = datetime.strptime(new_deadline, "%Y-%m-%dT%H:%M")
            except ValueError:
                pass
        note.save()
        return redirect("index")
    return render(request, "todosite/edit_note.html", context)


def delete_note(request, note_id):
    if request.method == "POST":
        note = get_object_or_404(Note, id=note_id)

        note.delete()
        return redirect(index)
    return render(request, "todosite/confirm_delete.html")
