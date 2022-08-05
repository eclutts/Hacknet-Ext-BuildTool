from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Node, Computer, GameObject

class IndexView(generic.ListView):
    template_name='nodebuilder.node_list.html'
    context_object_name = 'alphabetical_node_list'

    def get_queryset(self):
        return GameObject.objects.all()



def obj_list(request):
    comp_list = Computer.objects.select_related('sql_id')
    context = {
        'computers': comp_list
    }

    return render(request, 'nodebuilder/computer_list.html', context)



from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm, CompForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'nodebuilder/name.html', {'form': form})


def add_obj(request, type, subtype):
    new_gameObj = GameObject(object_type = type)
    new_gameObj.save()
    if type == 1:
        new_Node = Node(sql_id = new_gameObj, node_type = subtype, node_id = "", name="")
        new_Node.save()
        if subtype == 1:
            new_Computer = Computer(sql_id = new_Node)
            new_Computer.save()
    
    
    
    return HttpResponseRedirect(reverse('nodebuilder:view_obj', args=(new_gameObj.sql_id,)))

def view_obj(request, obj_sql_id):
    print("it works!")
    if request.method == "POST":
        # Insert something here
        return
    
    obj = GameObject.objects.get(sql_id = obj_sql_id)
    if obj.object_type == 1:
        obj = Node.objects.get(sql_id = obj_sql_id)
        if obj.node_type == 1:
            obj = Computer.objects.get(sql_id = obj_sql_id)
            form = CompForm()
            context = {
                'form' : form,

            }
    return render(request, 'nodebuilder/node_form.html', context)