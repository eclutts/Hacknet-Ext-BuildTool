from django.db import models
from django.forms import UUIDField
import uuid
import json
# Create your models here.

class GameObject(models.Model):
    sql_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    object_type_choices = [
        (1, 'Node'),            # Computer or eosPhone
        (2, 'File'),            # File, Encrypted File, Memory Dump File, eosDevice, eosMail
        (3, 'Connection'),      # dlink, positionNear
        (4, 'Daemon'),          # Daemon, ex) memory dump generator
        # Add more later.
    ]
    object_type = models.PositiveIntegerField(choices=object_type_choices, default=1)



# generic node (so phone or computer)
class Node(models.Model):
    sql_id = models.OneToOneField(GameObject, on_delete=models.CASCADE, limit_choices_to={'object_type': 1}, primary_key=True)
    node_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
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
    icon = models.PositiveIntegerField(choices=icon_choices, default=1)
    node_type = models.PositiveIntegerField(choices=[(1, 'Computer'), (2, 'eosDevice')])

    
    



class Computer(models.Model):
    sql_id = models.OneToOneField(Node, on_delete=models.CASCADE, limit_choices_to={'node_type': 1}, primary_key=True)
    ip = models.CharField(max_length=255, default="1.2.3.4")
    security = models.PositiveIntegerField(default=0)
    # to be implemented after we code daemons
    # allowsDefaultBootModule = models.BooleanField(default=False)
    
    TYPE_CHOICES = [
        (1, 'Corporate'),
        (2, 'Home'),
        (3, 'Server'),
        (4, 'Empty'),
    ]
    comp_type = models.IntegerField(choices=TYPE_CHOICES, default=4)

    ports = models.JSONField(null=True)
    portsForCrack = models.PositiveIntegerField(default=0)
    proxyLevel = models.IntegerField(default=-1)
    firewallLevel = models.IntegerField(default=-1)
    firewallSolution = models.CharField(max_length=255)
    firewallAdditionalTime = models.FloatField(default="0.0")

    traceTime = models.IntegerField(default=-1)
    
    ADMIN_TYPE_CHOICES = [
        (0, 'None'),
        (1, 'Basic'),
        (2, 'Progress'),
        (3, 'Fast'),
    ]
    adminType = models.PositiveIntegerField(choices=ADMIN_TYPE_CHOICES, default=0)
    adminResetPassword = models.BooleanField(default=False)
    adminIsSuper = models.BooleanField(default=False)

    tracker = models.BooleanField(default=False)
    
    # Implement Daemons at a later point

    

    
