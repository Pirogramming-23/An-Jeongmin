from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from .models import Idea, IdeaStar
from  .form import IdeaForm
from django.db.models import Count

# Create your views here.
def idea_list(request):
    sort = request.GET.get('sort', 'created')

    if sort == 'name':
        ideas = Idea.objects.all().order_by('title')
    elif sort == 'created': 
        ideas = Idea.objects.all().order_by('-id')
    elif sort == 'like':
        ideas = Idea.objects.annotate(star_count=Count('ideastar')).order_by('-star_count')    
        
    starred_ideas = []
    if request.user.is_authenticated:
        starred_ideas = Idea.objects.filter(ideastar__user=request.user)
    context ={
        "ideas" : ideas,
        'starred_ideas': starred_ideas
    }

    return render (request, "ideas/idea_list.html",context)

def idea_detail(request, pk):
    idea = Idea.objects.get(id=pk)
    if request.user.is_authenticated:
        is_starred = IdeaStar.objects.filter(user=request.user, idea=idea).exists()
    context = {
        "idea" : idea,
        'is_starred': is_starred,
    }
    return render(request,"ideas/idea_detail.html",context)

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST,request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect("ideas:idea_detail",pk=idea.pk)
    else:
        form = IdeaForm()
    
    return render(request,"ideas/idea_create.html",{"form":form})

def idea_update(request,pk):
    idea = get_object_or_404(Idea,id = pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST,request.FILES,instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect("ideas:idea_detail",pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    
    return render(request,"ideas/idea_create.html",{"form":form})

def idea_delete(request,pk):
    if request.method =="POST":
        idea = Idea.objects.get(id=pk)
        idea.delete()
    
    return redirect("ideas:idea_list")

def update_interest(request, pk):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        action = request.POST.get("action")

        if action == "increase":
            idea.interest += 1
        elif action == "decrease":
            idea.interest -= 1

        idea.save()
        return JsonResponse({"interest": idea.interest})
    
@login_required
def star_idea(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    IdeaStar.objects.get_or_create(user=request.user, idea=idea)
    return redirect('ideas:idea_list')

@login_required
def unstar_idea(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    IdeaStar.objects.filter(user=request.user, idea=idea).delete()
    return redirect('ideas:idea_list')
