# Creates the node class, with subsequent UUIDs
from reconfig_ports import reconfig_ports
from get_icon import get_icon, get_admin_type
from json import load
class node():
    def __init__(self, sql_id, id, name, ip, security, allowsDefaultBootModule, icon, type, ports, portsForCrack,
                proxyLevel=-1, firewallLevel=-1, firewallSolution='', firewallAdditionalTime=0.0, traceTime = -1,
                adminType = -1, adminResetPassword = False, adminIsSuper = False, tracker = False, memdumpexists = False, daemons = []):
        self.id = id
        self.name = name
        self.ip = ip
        self.security = security
        self.allowsDefaultBootModule = allowsDefaultBootModule
        self.icon = get_icon(icon)
        self.type = type
        tbkeys = ports[0::2]
        tbvalues = ports[1::2]
        self.ports = reconfig_ports(dict(zip(tbkeys, tbvalues)))
        self.portsForCrack = portsForCrack

        if proxyLevel != None:
            self.proxyLevel = proxyLevel
        else:
            self.proxyLevel = -1
        
        if firewallLevel != -1:
            self.firewallLevel = firewallLevel
            self.firewallSolution = firewallSolution
            self.firewallAdditionalTime = firewallAdditionalTime
        else:
            self.firewallLevel = -1
        self.traceTime = traceTime
        if adminType not in [1, 2, 3]:
            self.adminType = -1
        else:
            self.adminType = get_admin_type(adminType)
            self.adminResetPassword = adminResetPassword
            self.adminIsSuper = adminIsSuper
        
        self.tracker = tracker
        self.memdumpexists = memdumpexists
        self.daemons = daemons
        self.references = []

    def add_reference(self, reference):
        # reference: the object in question
        # reference_id, value dictating what the reference is (file, eos_device)
        self.references.append(reference)
        return

    def xml_file_gen(self):
        # generate an array of stuff, then join via \n and return.
        tbr = ["<?xml version = \"1.0\" encoding = \"UTF-8\" ?>",
                "<Computer id=\"%s\"" % self.id,
                "name=\"%s\"" % self.name,
                "ip=\"%s\"" % self.ip,
                "security=\"%s\"" % self.security,
                "allowsDefaultBootModule=\"%s\"" % self.allowsDefaultBootModule,
                "icon=\"%s\"" % self.icon,
                "type=\"%s\" >" % self.type,
                # ports, assuming that reconfig_ports.py has been called.
                "<ports>%s</ports>" % ", ".join(map(str, self.ports.keys())),
                "<portRemap>%s</portRemap>" % ",".join(map(lambda x, y : "%s=%s" % (x, y), self.ports.keys(), self.ports.values())),
                "<portsForCrack>%s</portsForCrack>" % self.portsForCrack,
                "<proxy time=\"%s\" />" % self.proxyLevel,
                "<trace time=\"%s\" />" % self.traceTime]

        if self.firewallLevel != -1:
            tbr.append("<firewall level=\"%s\" solution=\"%s\" additionalTime=\"%s\" />" % (self.firewallLevel, self.firewallSolution, self.firewallAdditionalTime))

        
        if self.adminType != -1:
            
            tbr.append("<admin type=\"%s\" resetPassword=\"%s\" isSuper=\"%s\" />" % (self.adminType, self.adminResetPassword, self.adminIsSuper))

        if self.tracker:
            tbr.append("<tracker />")

        # here's where daemons would go if I could be bothered.

        for i in self.references:
            tbr.extend(i.xml_file_gen())
        
        tbr.append("</Computer>")

        return tbr

"""
if __name__ == '__main__':
    test = node(12345, 'test', 'test', '5', '0', False, 'laptop', '0', {22 : 24}, 0, -1, -1)
    print('\n'.join(test.xml_file_gen()))
"""

