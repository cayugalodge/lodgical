from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from models import NewsArticle, About, Contact, Alumni, Moseyer, MoseyEvent
from forms import AlumniForm, MoseyerForm

# Create your views here.

def home(request):
    articles = NewsArticle.objects.all()[:10]
    context = {'news' : articles}
    return render_to_response("index.html", context, context_instance=RequestContext(request))

def about(request):
    try:
        about = About.objects.get()
    except About.DoesNotExist:
        about = None
    context = {'about' : about}
    return render_to_response("about.html", context, context_instance=RequestContext(request))

def alumni(request):
    alum_form = AlumniForm()
    context = {'alum_form' : alum_form}
    return render_to_response("alumni.html", context, context_instance=RequestContext(request))

def add_alum(request):
    form = AlumniForm(request.POST, request.FILES)
    if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            alum = Alumni.objects.create(name=name, email=email)
            alum.save()
            return HttpResponse("success")
    else:
        return HttpResponse("error")

def mosey(request):
    events = MoseyEvent.objects.all().order_by('start_date')
    context = {'events' : events}
    return render_to_response("mosey.html", context, context_instance=RequestContext(request))

def contact(request):
    contacts = Contact.objects.all()
    context = {'contacts' : contacts}
    return render_to_response("contact.html", context, context_instance=RequestContext(request))

def add_mosey(request):
    if request.method == 'POST':
        form = MoseyerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mosey/thanks/')
    else:
        form = MoseyerForm()

    return render(request, "mosey_signup.html", {'form' : form, })
