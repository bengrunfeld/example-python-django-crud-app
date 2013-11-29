from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
import time
from django import forms

from notes.models import Note

class NotesForm(forms.Form):
    title = forms.CharField(max_length=150)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':30, 'cols':65}))
    noteid = forms.CharField()

def index(request):
	"""Lists all of the Notes in the Database"""
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	template = 'notes/base.html'
	target = list_of_notes[0]
	noteid = list_of_notes[0].id
	form = NotesForm(initial={'title': target.title, 'content': target.content})
	context = {'list_of_notes': list_of_notes, 'target': target, 'form':form, 'noteid': noteid}
	return render(request, template, context)

def create(request):
	template = 'notes/create.html'
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	if not list_of_notes[0].title == '':
		note = Note(title='', content='')
		note.save()
	form = NotesForm()
	noteid = list_of_notes[0].id
	context = {'list_of_notes': list_of_notes, 'form':form, 'noteid': noteid}
	return render(request, template, context)


def read(request, note_id):
	"""Reads a specific note from the Database"""
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	template = 'notes/base.html'
	note = Note.objects.get(id=note_id)
	noteid = note.id
	target = Note.objects.get(id=note_id)
	form = NotesForm(initial={'title': target.title, 'content': target.content})
	context = {'list_of_notes': list_of_notes, 'target': target, 'form': form, 'noteid': noteid}
	return render(request, template, context)

def update(request):
	"""Updates a specific note in the Database"""
	template = 'notes/update.html'
	list_of_notes = Note.objects.all().order_by('-last_update_date')
	if request.method == 'POST':
		form = NotesForm(request.POST)
		if form.is_valid():
			print "WE HIT THE FORM!"
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			noteid = form.cleaned_data['noteid']
			note = Note.objects.get(pk=noteid)
			note.title = title
			note.content = content
			note.save()
			return HttpResponseRedirect('/notes/')
	else:
		form = NotesForm()
		context = {'list_of_notes': list_of_notes, 'form':form}
		return render(request, template, context)	

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
