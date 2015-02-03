from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

from models import NewsArticle, About, Contact, Alumni, Moseyer, MoseyEvent, MoseyerComment
from forms import AlumniForm, MoseyerForm, CommentForm

# Create your views here.

def home(request):
    articles = NewsArticle.objects.all().order_by('-date')[:10]
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

@login_required
def mosey_view(request):
    moseyers = Moseyer.objects.all()
    context = {'moseyers' : moseyers}
    return render_to_response("moseyer_list.html", context, context_instance=RequestContext(request))

def lodgical_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    context = {}
    form = AuthenticationForm()
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            context.update({'form': form, 'error': 'Your account has been disabled.'})
    else:
        context.update({'form': form, 'error': 'Invalid login information.'})
    return render_to_response("lodgical.html", context, context_instance=RequestContext(request))


def lodgical_logout(request):
    logout(request)
    return HttpResponseRedirect('/lodgical/')


def lodgical(request):
    form = AuthenticationForm()
    return render_to_response("lodgical.html", {'form' : form}, context_instance=RequestContext(request))

class MoseyerDetailView(DetailView):
    model = Moseyer

    def get_context_data(self, **kwargs):
        context = super(MoseyerDetailView, self).get_context_data(**kwargs)
        context['comments'] = MoseyerComment.objects.filter(moseyer=self.object.id)
        context['commentform'] = CommentForm()
        return context

@login_required
def add_comment(request, pk):
    if request.user.is_authenticated():
        if request.POST.has_key("text") and request.POST["text"]:
            author = request.user
            comment = MoseyerComment(moseyer=Moseyer.objects.get(pk=pk))
            cf = CommentForm(request.POST, instance=comment)
            comment = cf.save(commit=False)
            comment.author = author
            comment.save()
    return HttpResponseRedirect("/mosey/decision/{}".format(pk))

# @login_requires
# def lodgical_reset(request):


