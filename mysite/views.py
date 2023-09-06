from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
   
    if removepunc == 'on':
        punctuations = '''@!#$%^&*()-_=[]'";:?/<>.,'''
        analyzed = ""
        for char in djtext:
            
         if char not in  punctuations:
          analyzed = analyzed+char
        params = {'purpose':'Removed punctuations', 'analyzed_text':
                  analyzed}
        djtext = analyzed
        
    
    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
          analyzed = analyzed+ char.upper()
          params = {'purpose':'CAPITILIZED TEXT', 'analyzed_text':
                  analyzed}
        djtext = analyzed
        
    
    if(newlineremover == 'on'):
       analyzed = ""
       for char in djtext:
          if char != "\n" and char !="\r":
           analyzed = analyzed+ char
          params = {'purpose':'New Line Removed', 'analyzed_text':
                  analyzed}
          djtext = analyzed 

    if(spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " "  and djtext[index+1] == " ":
                    pass
            else:
                    analyzed = analyzed + char
         
        params = {'purpose':'New Line Removed', 'analyzed_text':
                  analyzed} 
        djtext = analyzed
    if(charcount == "on"):
        print("PK")
        analyzed = len(djtext) 
        params = {'purpose':'Character counter', 'analyzed_text':
                  analyzed} 
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and spaceremover!="on" and charcount!="on" ):
     return HttpResponse("Please select a valid option!")
    
    return render(request, 'analyze.html', params)
           

def Features(request):
    return render(request, 'Features.html')

def Aboutus(request):
    return render(request, 'Aboutus.html')

def Contactus(request):
    return render(request, 'Contactus.html')    
