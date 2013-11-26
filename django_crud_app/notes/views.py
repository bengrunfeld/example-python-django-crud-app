from django.shortcuts import render

from notes.models import Note

def index(request):
	"""Lists all of the Notes in the Database"""
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	if not list_of_notes:
		template = 'notes/empty.html'
	else:
		template = 'notes/base.html'
	target = list_of_notes[0]
	context = {'list_of_notes': list_of_notes, 'target': target}
	return render(request, template, context)

def create(request, note_id):
	"""Creates a new note in the Database"""
	pass

def read(request, note_id):
	"""Reads a specific note from the Database"""
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	if not list_of_notes:
		template = 'notes/empty.html'
	else:
		template = 'notes/base.html'
	target = Note.objects.get(id=note_id)
	context = {'list_of_notes': list_of_notes, 'target': target}
	return render(request, template, context)

def update(request, note_id):
	"""Updates a specific note in the Database"""
	pass

def delete(request, note_id):
	"""Deletes a specific note from the Database"""
	pass
