
from django.shortcuts import render
import xml.etree.ElementTree as gfg 
from xml.dom import minidom
import os
# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Node, Computer, GameObject
from django.forms import formset_factory, modelformset_factory
from nodebuilder.forms import NameForm, CompForm, CompForm_rev
import json



def obj_list(request, focus=None):
    comp_list = Computer.objects.all().order_by('node_id')
    context = {'computers' : comp_list}
    return render(request, 'nodebuilder/computer_list.html', context)





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
                    obj.icon = form.cleaned_data['icon']
                    obj.ip = form.cleaned_data['ip']
                    obj.security = form.cleaned_data['security']
                    obj.portsForCrack = form.cleaned_data['portsForCrack']
                    print(json.dumps(ports_to_json(form)))
                    obj.ports = json.dumps(ports_to_json(form))
                    obj.comp_type = form.cleaned_data['comp_type']
                    obj.proxyLevel = form.cleaned_data['proxyLevel']
                    obj.firewallLevel = form.cleaned_data['firewallLevel']
                    obj.firewallSolution = form.cleaned_data['firewallSolution']
                    obj.firewallAdditionalTime = form.cleaned_data['firewallAdditionalTime']
                    obj.traceTime = form.cleaned_data['traceTime']
                    obj.adminType = form.cleaned_data['adminType']
                    obj.adminResetPassword = form.cleaned_data['adminResetPassword']
                    obj.adminIsSuper = form.cleaned_data['adminIsSuper']
                    obj.tracker = form.cleaned_data['tracker']
                    obj.save()
                    print(obj.node_id)
                    return HttpResponseRedirect(reverse('nodebuilder:view_obj', args=(obj.sql_id,)))
    
    if type[0] == 1:
        if type[1] == 1:
            vals = {'node_id' : obj.node_id,
                    'name': obj.name,
                    'icon': obj.icon,
                    'ip': obj.ip,
                    'security': obj.security,
                    'comp_type': obj.comp_type,
                    'portsForCrack': obj.portsForCrack,
                    'proxyLevel': obj.proxyLevel,
                    'firewallLevel': obj.firewallLevel,
                    'firewallSolution': obj.firewallSolution,
                    'firewallAdditionalTime': obj.firewallAdditionalTime,
                    'traceTime': obj.traceTime,
                    'adminType': obj.adminType,
                    'adminResetPassword': obj.adminResetPassword,
                    'adminIsSuper': obj.adminIsSuper,
                    'tracker': obj.tracker,
                    }
            p = json_to_ports(obj.ports)
            if p != None:
                vals.update(json_to_ports(obj.ports))
            form = CompForm_rev(vals, auto_id=False)

    comp_list = Computer.objects.all().order_by('node_id')
    context = {
        'form' : form,
        'obj_sql_id' : obj_sql_id,
        'computers' : comp_list,
        'port_list' : list(map(lambda x : str(x) + '_port', port_mapping.keys())) + list(map(lambda x : str(x) + '_remap', port_mapping.keys()))
    }

    return render(request, 'nodebuilder/node_form.html', context)

    
def json_to_ports(port_list):
    tbd = dict()
    if port_list == None:
        for i, j in port_mapping.items():
            tbd[i + '_port'] = False
            tbd[i + '_remap'] = j
        return tbd
    for x, y in json.loads(port_list).items():
        tbd[str(x) + '_port'] = True
        tbd[str(x) + '_remap'] = y
            
    for i in set(map(lambda x : x + '_port', port_mapping.keys())).difference(tbd.keys()):
        tbd[i] = False
    return tbd

def ports_to_json(form):
    tbd = dict()
    for i in port_mapping.keys():
        if form.cleaned_data[i + '_port']:
            tbd[i] = form.cleaned_data[i + '_remap']
    return tbd



def gen_obj(request, obj_sql_id):
    obj = Computer.objects.get(sql_id = obj_sql_id)
    
    root = gfg.Element("Computer")
  
    root.set('id', obj.node_id)
    root.set('name', obj.name)
    root.set('ip', obj.ip)
    root.set('security', str(obj.security))
    root.set('icon', icon_choices[obj.icon - 1][1])
    root.set('type', str(obj.comp_type))

    ports = gfg.SubElement(root, "ports")
    ports.text = ','.join(map(lambda x : str(port_mapping[x]), json.loads(obj.ports).keys()))

    portRemap = gfg.SubElement(root, "portRemap")
    portRemap.text = ",".join(map(lambda x, y: str(port_mapping[x]) + "=" + str(y), json.loads(obj.ports).keys(), json.loads(obj.ports).values()))
    pFC = gfg.SubElement(root, 'portsForCrack')
    pFC.set('val', str(obj.portsForCrack))

    if obj.proxyLevel != -1:
        proxy = gfg.SubElement(root, 'proxy')
        proxy.set("val", str(obj.proxyLevel))
    
    if obj.traceTime != -1:
        trace = gfg.SubElement(root, 'trace')
        trace.set('time', obj.traceTime)

    if obj.adminType != 0:
        admin = gfg.SubElement(root, 'admin')
        admin.set('type', ADMIN_TYPE_CHOICES[obj.adminType][1])
        admin.set('resetPassword', str(obj.adminResetPassword).lower())
        admin.set('isSuper', str(obj.adminIsSuper).lower())

    if obj.firewallLevel != -1:
        firewall = gfg.SubElement(root, 'firewall')
        firewall.set('level', str(obj.firewallLevel))
        firewall.set('solution', obj.firewallSolution)
        firewall.set('additionalTime', str(obj.firewallAdditionalTime))

    if obj.tracker:
        tracker = gfg.SubElement(root, 'tracker')

    tree = gfg.ElementTree(root)
  
    save_path_file = "nodebuilder\\static\\nodebuilder\\xml_files\\" + obj_sql_id + ".xml"
  
    with open(save_path_file, "wb") as f:
        tree.write(f)

    return HttpResponseRedirect(reverse('nodebuilder:download_obj', args=(obj_sql_id,)))

def download_obj(request, obj_sql_id):
    context = {
        'filepath': "nodebuilder/xml_files/" + str(obj_sql_id) + ".xml"
    }
    return render(request, 'nodebuilder/download.html', context)



icon_choices = [
    (1, 'laptop'),
    (2, 'chip'),
    (3, 'kellis'),
    (4, 'tablet'),
    (5, 'ePhone'),
    (6, 'ePhone2'),
    (7, 'Psylance'),
    (8, 'PacificAir'),
    (9, 'Alchemist'),
    (10, 'DLCLaptop'),
    (11, 'DLCPC1'),
    (12, 'DLCPC2'),
    (13, 'DLCServer'),
]

port_mapping = {
    'ssh': 22,
    'ftp': 21,
    'smtp': 25,
    'web': 80,
    'sql': 1433,
    'kbt': 104,
    'tor': 6881,
    'ssl': 443,
    'pac': 192,
    'rtsp': 554,
}

ADMIN_TYPE_CHOICES = [
        (0, 'None'),
        (1, 'basic'),
        (2, 'progress'),
        (3, 'fast'),
]