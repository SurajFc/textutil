from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
        # Get the text
        djtext = request.POST.get('text', 'default')

        # Check checkbox values
        removepunc = request.POST.get('removepunc', 'off')
        fullcaps = request.POST.get('fullcaps', 'off')
        newlineremover = request.POST.get('newlineremover', 'off')
        extraspaceremover = request.POST.get('extraspaceremover', 'off')
        # charactercount = request.POST.get('charcount', 'off')
        numberremover = request.POST.get('nonum', 'off')

        # Check which checkbox is on
        if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char

            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
            djtext = analyzed

        if (fullcaps == "on"):
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()

            params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
            djtext = analyzed


        if (extraspaceremover == "on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext = analyzed

        if (newlineremover == "on"):
            analyzed = ""
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
                else:
                    print("no")

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext = analyzed

        if numberremover == "on":
            analyzed = ""
            for char in djtext:
                if not (char.isnumeric()):
                    analyzed += char
            params = {'purpose': 'Remove Numbers', 'analyzed_text': analyzed}


        if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and numberremover != "on" ):
            return HttpResponse("please select any operation and try again")


        return render(request, 'analyze.html', params)


def contactus(request):
    return render(request, "Contact Us.html")

def about(request):
    return render(request, "about.html")