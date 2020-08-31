from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .forms import SearchForm
from .models import Note


# Create your views here.
class ListNotes(ListView):
    model = Note


class NotesDetail(DetailView):
    model = Note


class CreateNote(CreateView):
    model = Note
    fields = ["note_title", "note_body"]
    template_name_suffix = "_create"
    success_url = '/notes/'


class UpdateNote(UpdateView):
    model = Note
    template_name_suffix = "_update"
    fields = ["note_title", "note_body"]
    success_url = '/notes/'


class DeleteNote(DeleteView):
    model = Note
    success_url = "/notes/"


def search_notes(request):
    if request.method == "GET":
        form = SearchForm()

        return render(request, "notes/search.html", {"form": form})

    else:
        title_search = request.POST["title"]
        title_search_by = request.POST["title_search_by"]
        body_search = request.POST["body"]
        body_search_by = request.POST["body_search_by"]

        if title_search_by == "includes":
            results = Note.objects.filter(note_title__contains=title_search)

        elif title_search_by == "starts with":
            results = Note.objects.filter(note_title__startswith=title_search)

        else:
            results = Note.objects.filter(note_title=title_search)

        if body_search_by == "includes":
            results = results.filter(note_body__contains=body_search)

        if body_search_by == "starts with":
            results = results.filter(note_body__startswith=body_search)

        else:
            results = results.filter(note_body=body_search)

        return render(request, "notes/search_results.html", {"results": results})
