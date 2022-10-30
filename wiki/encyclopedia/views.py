from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util

import markdown

import random

def index(request):
	return render(request,"encyclopedia/index.html",{
		"entries": util.list_entries()
		})

def convert_to_HTML(title):
	content = util.get_entry(title)
	markdowner = markdown.Markdown()
	if content == None:
		return None
	else:
		return markdowner.convert(content)

def entry(request,entry):
	entryPage = util.get_entry(entry)
	if entryPage is None:
		return render(request, "encyclopedia/error.html",{
			"entryTitle": entry 
			})
	
	else: 
		return render(request, "encyclopedia/entry.html", {
			"entry": convert_to_HTML(entry),
			"entryTitle": entry
			}) 
def search(request):
    value = request.GET.get('q', '')
    if(util.get_entry(value) is not None):
        return HttpResponseRedirect(reverse("entry", kwargs={'entry': value}))
    else:
        searchEntries = []
        for entry in util.list_entries():
            if value.upper() in entry.upper():
                searchEntries.append(entry)

        return render(request, "encyclopedia/search_results.html",{
            "entries": searchEntries,
            "search": True,
            "value": value
        })
		

def newEntry(request):
	return render(request, "encyclopedia/newEntry.html")

def save(request):
	if request.method == 'POST':
		input_title = request.POST['title']
		input_text = request.POST['text']
		entries = util.list_entries()
		html = convert_to_HTML(input_title)
		Already_exist_true = "false"
		for entry in entries:
			if input_title.upper() == entry.upper():
				Already_exist_true = "true"
				

		if Already_exist_true == "true":
			return render(request, "encyclopedia/existing.html",{
				"entry":html,
				"entryTitle":input_title
				})

		else:
			util.save_entry(input_title, input_text)
			return render(request, "encyclopedia/entry.html", {
				"entry": convert_to_HTML(input_title),
				"entryTitle": input_title
			})


def random_entry(request):
	entries = util.list_entries()
	randEntry = random.choice(entries)
	html = convert_to_HTML(randEntry)
	return render(request, "encyclopedia/entry.html",{
		"entry": html,
		"entryTitle":randEntry
		})

def editPage(request): 
	if request.method == 'POST':
		input_title = request.POST['title']
		text = util.get_entry(input_title)
		return render(request, "encyclopedia/editPage.html",{
			"entry": text,
			"entryTitle": input_title
		})

def saveEdit(request):
	if request.method == 'POST':
		entryTitle = request.POST['title']
		entry = request.POST['text']
		util.save_entry(entryTitle, entry)
		html = convert_to_HTML(entryTitle)
		return render (request, "encyclopedia/entry.html",{
			"entry": html,
			"entryTitle": entryTitle
			})
