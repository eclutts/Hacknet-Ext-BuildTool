from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Node, Computer, GameObject
from django.forms import formset_factory, modelformset_factory
from nodebuilder.forms import NameForm, CompForm



def obj_list(request, focus=None):
    comp_list = Computer.objects.all()
    data = []
    for i in comp_list:
        data.append({
            'node_id': i.node_id,
            'name': i.name,
            'icon': i.icon,
            'ip': i.ip,
            'security': i.security,
            'comp_type': i.comp_type,
            'portsForCrack': i.portsForCrack,
            'proxyLevel': i.proxyLevel,
            'firewallLevel': i.firewallLevel,
            'firewallSolution': i.firewallSolution,
            'firewallAdditionalTime': i.firewallAdditionalTime,
            'traceTime': i.traceTime,
            'adminType': i.adminType,
            'adminResetPassword': i.adminResetPassword,
            'adminIsSuper': i.adminIsSuper,
            'tracker': i.tracker,

        })
    CompFormSet = modelformset_factory(Computer, exclude=('sql_id', 'node_type', 'ports', 'object_type', ), extra= len(data)+ 1)
    if (request.method == 'POST'):
        formset = CompFormSet(request.POST, initial=data)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for i in instances:
                i.object_type = 1
                i.node_type = 1
                i.save()
            return HttpResponseRedirect(reverse('nodebuilder:obj_list'))
            
    formset = CompFormSet(initial=data)
    context = {'formset' : formset}




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
    new_gameObj = GameObject(object_type = type)
    new_gameObj.save()
    if type == 1:
        new_Node = Node(sql_id = new_gameObj, node_type = subtype, node_id = "test", name="test")
        new_Node.save()
        if subtype == 1:
            new_Computer = Computer(sql_id = new_Node)
            new_Computer.save()
    
    
    
    return HttpResponseRedirect(reverse('nodebuilder:view_obj', args=(new_gameObj.sql_id,)))

def view_obj(request, obj_sql_id):
    obj, type = get_obj_and_type(obj_sql_id)

    if request.method == "POST":
        if type[0] == 1:
            if type[1] == 1:
                form = CompForm(request.POST)
                if form.is_valid():
                    obj.sql_id.node_id = form.cleaned_data['node_id']
                    obj.sql_id.name = form.cleaned_data['name']
                    obj.sql_id.save()
                    return HttpResponseRedirect(reverse('nodebuilder:view_obj', args=(obj.sql_id.sql_id.sql_id,)))
    
    if type[0] == 1:
        if type[1] == 1:
            vals = {'node_id' : obj.sql_id.node_id, 'name': obj.sql_id.name}
            form = CompForm(vals, auto_id=False)

    comp_list = Computer.objects.select_related('sql_id')
    context = {
        'form' : form,
        'obj_sql_id' : obj_sql_id,
        'computers' : comp_list,
    }

    return render(request, 'nodebuilder/node_form.html', context)

    
    
    


def get_obj_and_type(obj_sql_id):
    obj = GameObject.objects.get(sql_id = obj_sql_id)
    type = [obj.object_type]
    if obj.object_type == 1:
        obj = Node.objects.get(sql_id = obj_sql_id)
        type.append(obj.node_type)
        if obj.node_type == 1:
            obj = Computer.objects.get(sql_id = obj_sql_id)
            
    return [obj, type]