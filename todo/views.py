from django.shortcuts import render, redirect

from todo.forms import AddNoteForm
from todo.models import Note


def index(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddNoteForm()

    notes = Note.objects.order_by('id')

    context = {
        'notes': notes,
        'form': form
    }

    return render(request, 'todo/index.html', context=context)


def addTodo(request):
    form = AddNoteForm(request.POST)
    return redirect('index')


def completeTodo(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.finished = True if note.finished is False else False
    note.save()
    return redirect('index')


def deleteCompleted(request):
    Note.objects.filter(finished__exact=True).delete()
    return redirect('index')


def deleteAll(request):
    Note.objects.all().delete()
    return redirect('index')