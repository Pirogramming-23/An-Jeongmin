from django.shortcuts import render,redirect, get_object_or_404
from .models import Tool
from  .form import ToolForm

# Create your views here.
def tool_list(request):
    tools = Tool.objects.all()
    context ={
        "tools" : tools
    }
    return render (request, "tools/tool_list.html",context)

def tool_detail(request, pk):
    tool = Tool.objects.get(id=pk)
    context = {
        "tool" : tool
    }
    return render(request,"tools/tool_detail.html",context)

def tool_create(request):
    if request.method == 'POST':
        form = ToolForm(request.POST,request.FILES)
        if form.is_valid():
            tool = form.save()
            return redirect("tools:tool_detail",pk=tool.pk)
    else:
        form = ToolForm()
    
    return render(request,"tools/tool_create.html",{"form":form})

def tool_update(request,pk):
    tool = get_object_or_404(Tool,id = pk)
    if request.method == 'POST':
        form = ToolForm(request.POST,request.FILES,instance=tool)
        if form.is_valid():
            tool = form.save()
            return redirect("tools:tool_detail",pk=tool.pk)
    else:
        form = ToolForm(instance=tool)
    
    return render(request,"tools/tool_create.html",{"form":form})

def tool_delete(request,pk):
    if request.method =="POST":
        tool = Tool.objects.get(id=pk)
        tool.delete()
    
    return redirect("tools:tool_list")
