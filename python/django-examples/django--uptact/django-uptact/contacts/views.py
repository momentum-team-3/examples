from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Note
from .forms import ContactForm, NoteForm


# Create your views here.
def list_contacts(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.filter(contact_of=request.user)
    
    else:
        contacts = None
    
    return render(request, "contacts/list_contacts.html",
                  {"contacts": contacts})


def view_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact_notes = Note.objects.filter(contact=contact)

    return render(request, 
    "contacts/view_contact.html", 
    {"contact": contact, "contact_notes": contact_notes})


def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.contact_of = request.user
            new_contact.save()

            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
    else:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_contact.html", {
        "form": form,
        "contact": contact
    })


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                  {"contact": contact})



# Add, edit, and delete notes
def add_note(request, c_pk):
    if request.method == "GET":
        form = NoteForm()

    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            contact = get_object_or_404(Contact, pk=c_pk)
            
            # Get new note instance so the contact can be set
            new_note = form.save(commit=False)
            new_note.contact = contact
            new_note.save()
            
            return redirect(to='list_contacts')

    return render(request, "contacts/add_note.html", {"form": form, "contact_pk": c_pk})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == 'GET':
        form = NoteForm(instance=note)
    
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_note.html", {
        "form": form,
        "note": note
    })


def delete_note(request, c_pk, pk):
    # Save the contact primary key to navigate back to the right view
    note = get_object_or_404(Note, pk=pk)
    if request.POST:
        note.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_note.html",
                  {"note": note, "pk": pk, "c_pk": c_pk})
