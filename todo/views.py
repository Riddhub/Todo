from django.http import HttpResponse
from django.shortcuts import render, redirect

from todo.forms import AddNoteForm
from todo.models import Note


def index(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddNoteForm()

    notes = Note.objects.all()
    context = {
        'notes': notes,
        'form': form
    }
    
    return render(request, 'todo/index.html', context=context)

