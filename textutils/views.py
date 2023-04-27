# I have created this file - Rasikh
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def analyze(request):
    # get the given text
    djtext = request.POST.get('text', 'default')

    # checking the checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Checking which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        # removing the puncuations
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Puncuations', 'analyzed_text':analyzed}
        djtext = analyzed

    if uppercase == "on":
        analyzed = ""
        # changed to UPPERCASE
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change to uppercase', 'analyzed_text':analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        # removing the new line
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed new lines', 'analyzed_text':analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        # removing the new line
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Removed new lines', 'analyzed_text':analyzed}
        djtext = analyzed

    if removepunc != "on" and uppercase != "on" and newlineremover != "on" and extraspaceremover != "on":
        return HttpResponse("Please select any operation and try again!")

    return render(request, 'analyze.html', params)
