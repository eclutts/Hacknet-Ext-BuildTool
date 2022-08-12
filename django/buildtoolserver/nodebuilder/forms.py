from django import forms
from django.forms import ModelForm
from nodebuilder.models import Computer

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class CompForm(forms.Form):

    node_id = forms.CharField(label='ID ', max_length=255)
    name = forms.CharField(label="Name ", max_length=255)
    ip = forms.CharField(label="IP ", max_length=255)
    icon_choices = [
        (1, 'Laptop'),
        (2, 'Chip'),
        (3, 'Kellis'),
        (4, 'Tablet'),
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
    icon = forms.ChoiceField(label="Icon: ", choices=icon_choices)
    security = forms.ChoiceField(label="Security Level: ", choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    TYPE_CHOICES = [
        (1, 'Corporate'),
        (2, 'Home'),
        (3, 'Server'),
        (4, 'Empty'),
    ]
    comp_type = forms.ChoiceField(label="Computer Type: ", choices=TYPE_CHOICES)
    
    ssh_port = forms.BooleanField(label="SSH")
    ssh_remap = forms.IntegerField(label="SSH Remap")
    ftp_port = forms.BooleanField(label="FTP")
    ftp_remap = forms.IntegerField(label="FTP Remap")

class CompForm_rev(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompForm_rev, self).__init__(*args, **kwargs)
        self.fields['tracker'].required = False
        
    ssh_port = forms.BooleanField(label="SSH", required=False, widget=(forms.CheckboxInput))
    ssh_remap = forms.IntegerField(label="SSH Remap")

    ftp_port = forms.BooleanField(label="FTP", required=False, widget=(forms.CheckboxInput))
    ftp_remap = forms.IntegerField(label="FTP Remap")
    class Meta:
        model = Computer
        fields = ['node_id', 'name', 'icon', 'ip', 'security', 'comp_type', 'portsForCrack', 'proxyLevel', 'firewallLevel', 'firewallSolution', 'firewallAdditionalTime', 'adminType', 'adminResetPassword', 'adminIsSuper', 'traceTime', 'tracker']

