from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Node, Computer, GameObject
from django.forms import formset_factory, modelformset_factory
from nodebuilder.forms import NameForm, CompForm, CompForm_rev



def obj_list(request, focus=None):
    comp_list = Computer.objects.all()
    context = {'computers' : comp_list}
    return render(request, 'nodebuilder/computer_list.html', context)







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
    if type == 1:
        if subtype == 1:
            new_Computer = Computer(object_type = 1, node_type = 1, name="TBD")
            new_Computer.save()
    
    
    
    return HttpResponseRedirect(reverse('nodebuilder:view_obj', args=(new_Computer.sql_id,)))

def view_obj(request, obj_sql_id):
    # temp
    type = [1, 1]
    obj = Computer.objects.get(sql_id = obj_sql_id)
    if request.method == "POST":
        if type[0] == 1:
            if type[1] == 1:
                form = CompForm_rev(request.POST)
                if form.is_valid():
                    obj.node_id = form.cleaned_data['node_id']
                    obj.name = form.cleaned_data['name']
                    obj.save()
                    return HttpResponseRedirect(reverse('nodebuilder:view_obj', args=(obj.sql_id,)))
    
    if type[0] == 1:
        if type[1] == 1:
            vals = {'node_id' : obj.node_id,
                    'name': obj.name,
                    'icon': obj.icon,
                    'ip': obj.ip,
                    'security': obj.security,
                    'portsForCrack': obj.portsForCrack,
                    'proxyLevel': obj.proxyLevel,
                    'firewallLevel': obj.firewallLevel,
                    'adminType': obj.adminType,
                    'adminResetPassword': obj.adminResetPassword,
                    'adminIsSuper': obj.adminIsSuper,
                    'tracker': obj.tracker,
                    }
            form = CompForm_rev(vals, auto_id=False)

    comp_list = Computer.objects.all()
    context = {
        'form' : form,
        'obj_sql_id' : obj_sql_id,
        'computers' : comp_list,
    }

    return render(request, 'nodebuilder/node_form.html', context)

    
    
    


def get_obj_and_type(obj_sql_id):
    obj = GameObject(sql_id = obj_sql_id)
    type = [obj.object_type]
    if obj.object_type == 1:
        obj = Node.objects.get(sql_id = obj_sql_id)
        type.append(obj.node_type)
        if obj.node_type == 1:
            obj = Computer.objects.get(sql_id = obj_sql_id)
            
    return [obj, type]

