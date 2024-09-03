
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request , 'index.html')

def analyze(request):
    txt =request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    caps = request.POST.get('fullcaps','off')
    spaceremover =request.POST.get('spaceremover','off')
    newline =request.POST.get('newline','off')
   
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if(removepunc=='on'):
       analyzed = ""
       for char in txt:
         if char not in punc:
            analyzed = analyzed+char
         params = {'purpose':'Remove Punctuation','analyzed_text':analyzed}
         txt = analyzed

    if(caps=="on"):
       analyzed=""
       for char in txt:
           analyzed = analyzed + char.upper()
       params = {'purpose':"UPPERCASE",'analyzed_text':analyzed}
       txt =analyzed

    if(spaceremover=="on"):
       analyzed=""
       for index,char in enumerate(txt):
          if txt[index]==" " and txt[index+1]==" ":
            pass
          else:
             analyzed = analyzed+char
       params = {'purpose':"Removed new line",'analyzed_text':analyzed}
       txt =analyzed
      
    if(newline=="on"):
       analyzed=""
       for char in txt:
          if char != "\n" and char != "\r":
             analyzed = analyzed+char
       
       params = {'purpose':"Removed new line",'analyzed_text':analyzed}
       txt = analyzed
      
    if(removepunc !="on" and newline !='on' and spaceremover !='on' and caps!='on'):
       return HttpResponse("Please select any operation")
    
    return render(request,'analyze.html',params)

       
        
    
  