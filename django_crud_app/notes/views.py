from django.http import Http404
from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import RequestContext, loader

from notes.models import Note

def index(request):
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	context = {'list_of_notes': list_of_notes}
	return render(request, 'notes/index.html', context)

def create(request, note_id):
	pass

def read(request, note_id):
	pass

def update(request, note_id):
	pass

def delete(request, note_id):
	pass
