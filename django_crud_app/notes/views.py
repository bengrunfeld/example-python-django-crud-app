from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

from notes.models import Note

class NotesForm(forms.Form):
    title = forms.CharField(max_length=150)
    content = forms.CharField()

def index(request):
	"""Lists all of the Notes in the Database"""
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	template = 'notes/base.html'
	target = list_of_notes[0]
	if request.method == 'POST':
		form = NotesForm(request.POST)
		if form.is_valid():
			# Process the data in form.cleaned_data
			return HttpResponseRedirect('/notes/') # Redirect after POST
	else:
		form = NotesForm()
	print(form)
	context = {'list_of_notes': list_of_notes, 'target': target, 'form':form}
	return render(request, template, context)

# def create(request, note_title, note_content):
# 	# """Creates a new note in the Database"""
# 	# list_of_notes = Note.objects.all().order_by('-last_update_date')
# 	# template = 'notes/base.html'
# 	# newspace = True
# 	pass

def create(request):
	template = 'notes/base.html'
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	target = "1"
	if request.method == 'POST':
		form = NotesForm(request.POST)
		if form.is_valid():
			# Process the data in form.cleaned_data
			return HttpResponseRedirect('/notes/') # Redirect after POST
	else:
		form = NotesForm()
	print(form)
	context = {'list_of_notes': list_of_notes, 'form':form, 'target':target}
	return render(request, template, context)
	
	


def read(request, note_id):
	"""Reads a specific note from the Database"""
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	template = 'notes/base.html'
	target = Note.objects.get(id=note_id)
	context = {'list_of_notes': list_of_notes, 'target': target}
	return render(request, template, context)

def update(request, note_id):
	"""Updates a specific note in the Database"""
	pass

def delete(request, note_id):
	"""Deletes a specific note from the Database"""
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	template = 'notes/base.html'
	target = Note.objects.get(id=note_id)
	tempid = target.id
	target.delete()
	deleted = True
	context = {'deleted': deleted, 'tempid': tempid, 'list_of_notes': list_of_notes}
	return render(request, template, context)
