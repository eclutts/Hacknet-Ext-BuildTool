"""
NODE BASICS:

<?xml version = "1.0" encoding = "UTF-8" ?>

<Computer id=
"""

def generate_node_file(node):
    if "id" not in node.keys():
        node["id"] = "none"
    
    if "name" not in node.keys():
        node["name"] = "none"
    
    docName = node["id"] + "_" + node["name"] + ".xml"

    f = open(docName, "w")

    f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" ?>\n\n")
    f.write("<Computer id=\"" + node["id"] + "\" name=\"" + node["name"] + "\" ")

    if "ip" in node.keys():
        f.write("ip=\"" + node["ip"] + "\" ")

    if "security" in node.keys():
        f.write("security=\"" + node["security"] + "\" ")
    
    if "allowsDefaultBootModule" in node.keys():
        f.write("allowsDefaultBootModule=\"" + node["allowsDefaultBootModule"] + "\" ")

    if "icon" in node.keys():
        f.write("icon=\"" + node["icon"] + "\" ")

    if "type" in node.keys():
        f.write("type=\"" + node["type"] + "\" ")
    else:
        f.write("type=\"empty\" ")
    
    f.write(">\n\n")

    if "adminPass" in node.keys():
        f.write("<adminPass pass=\"" + node["adminPass"] + "\" /> \n\n")

    """
    Account Setup:
    node["accounts"] = list of dictionaries?
    node["accounts"][1] = {"name"="dave", "type"="XYZ", "pass"="password"}
    """

    if "accounts" in node.keys():
        for i in node["accounts"]:
            f.write("<account username=\"" + i["name"] + "\" password=\"" + i["pass"] + "\" type=\"" + i["type"] + "\" />\n\n")

    """
    Ports!
    <ports>[port1], [port2], [port3], etc.</ports>
    """

    if "ports" in node.keys():
        f.write("<ports>" + ", ".join(node["ports"]) + "</ports>\n\n")

    if "proxy" in node.keys():
        f.write("<proxy time=\"" + node["proxy"] + "\" />\n\n")

    if "portsForCrack" in node.keys():
        f.write("<portsForCrack val=\"" + node["portsForCrack"] + "\" />\n\n")
    

    """
    <portRemap>old=new,old2=new2</portRemap>
    Pass it as a dictionary node["portRemap"]["old"] = new
    """

    if "portRemap" in node.keys():
        f.write("<portRemap>" + ",".join(map(lambda x, y : x + "=" + y, node["portRemap"].items())) + "</portRemap>\n\n")


    """
    <firewall level="int" solution="string" additionalTime="float"/>
    """
    if "firewall" in node.keys():
        f.write("<firewall level=\"" + node["firewall"]["level"] + "\" solution=\"" + node["firewall"]["solution"] + "\" additionalTime=\"" + node["firewall"]["additionalTime"] + "\"/>\n\n")
    
    """
    <trace time="int"/>
    """

    if "trace" in node.keys():
        f.write("<trace time=\"" + node["trace"] + "\"/>\n\n")


    """
    <admin type="string" resetPassword="bool" isSuper="bool"/>
    """
    if "admin" in node.keys():
        f.write("<admin type=\"" + node["admin"]["type"] + "\" resetPassword=\"" + node["admin"]["resetPassword"] + "\" isSuper=\"" + node["admin"]["isSuper"] + "\"/>\n\n")
    


    if "tracker" in node.keys():
        f.write("<tracker />\n\n")


    """
    <dlink target="otherComputerID" />
    can have multiple, pass as a list of IDs.
    """

    if "dlink" in node.keys():
        for i in node["dlink"]:
            f.write("<dlink target=\"" + i + "\" /> \n")
        f.write("\n")

    """
    <positionNear target="id" position="pos" total="tot" extraDistance="ext" force="bool" />
    can have multiple.
    list of dictionaries.
    """
    if "positionNear" in node.keys():
        f.write("\n".join(map(lambda x : "<positionNear target=\"" + x["id"] + "\" position=\"" + x["pos"] + "\" total=\"" + x["tot"] + "\" extraDistance=\"" + x["ext"] + "\" force=\"" + x["force"] + "\" />", node["positionNear"])))
        f.write("\n\n")


    """
    <file path="fp" name="nm">file[i]["text"]</file>
    """
    if "file" in node.keys():
        for i in node["file"]:
            f.write("<file path=\"" + i["fp"] + "\" name=\"" + i["nm"] + "\">" + i["text"] + "</file>\n\n")
        f.write("\n\n")
    

    """
    <customthemefile path="fp" name="nm" themePath="xmldoc"/>
    array of dictionaries
    """
    if "customthemefile" in node.keys():
        f.write("\n".join(map(lambda x : "<customthemefile path=\"" + x["fp"] + "\" name=\"" + x["nm"] + "\" themePath=\"" + x["xmldoc"] + "\" />", node["customthemefile"])))
        f.write("\n\n")

    """
    Encrypted Files:
    <encryptedFile path="fp" name="nm" extension="ext" ip="ip" header="head" pass="pass">
        "text"
    </encryptedFile>

    array of dictionaries.
    """

    if "encryptedFile" in node.keys():
        f.write("\n\n".join(map(lambda x : "<encryptedFile path=\"" + x["fp"] + "\" name=\"" + x["nm"] + "\" ip=\"" + x["ip"] + "\" header=\"" + x["head"] + "\" pass=\"" + x["pass"] + "\"> \n\t" + x["text"] + "\n</encryptedFile>", node["encryptedFile"])))
        f.write("\n\n")


    """
    <eosDevice name="nm" id="id" icon="ic" empty="bool" passOverride="string">
        <note>"note"[0]["text"]</note>
        <mail username="user" pass="pass" />
        can have multiple of both and also files
    """

    if "eos" in node.keys():
        f.write("<eosDevice name=\"" + node["eos"]["nm"] + "\" id=\"" + node["eos"]["id"] + "\" icon=\"" + node["eos"]["ic"] + "\" empty=\"" + node["eos"]["empty"] + "\" passOverride=\"" + node["eos"]["pass"] + "\">\n")
        if "note" in node["eos"]:
            f.write("\n".join(map(lambda x : "<node>" + x + "</node>", node["eos"]["note"])))
            f.write("\n")

        if "mail" in node["eos"]:
            f.write("\n".join(map(lambda x : "<mail username=\"" + x["user"] + "\" pass=\"" + x["pass"] + "\" + />", node["eos"]["mail"])))
            f.write("\n")

        
        if "file" in node["eos"].keys():
            for i in node["eos"]["file"]:
                f.write("<file path=\"" + i["fp"] + "\" name=\"" + i["nm"] + "\">" + i["text"] + "</file>\n\n")
            f.write("\n\n")
        f.write("</eosDevice>\n\n")


    """
    <mailServer name="Example Mail Server" color="50,237,212" generateJunk="true">
    <email recipient="mailGuy" sender="Sender Guy" subject="Adding an email!">
This is how you add emails to the mail server - logging in with someone's account
will show these just like the way the player gets emails.
    </email>
    <email recipient="mailGuy" sender="Spam" subject="amazing features">
You can have as many of these as you want
    </email>
    <email recipient="Matt" sender="Spam" subject="amazing features">
Different users too
    </email>
  </mailServer>
    """
    if "mailServer" in node.keys():
        f.write("<mailServer name=\"" + node["mailServer"]["nm"] + "\" color=\"" + node["mailServer"]["color"] + "\" generateJunk=\"" + node["mailServer"]["junk"] + "\">\n")
        if "email" in node["mailServer"].keys():
            for i in node["mailServer"]["email"]:
                f.write("<email recipient=\"" + i["rec"] + "\" sender=\"" + i["send"] + "\" subject=\"" + i["sub"] + "\">\n" + i["text"] + "\n</email>\n")
        f.write("</mailServer>\n\n")
    
    """
    Upload Server Daemon
    <uploadServerDaemon name="nm" folder="f" needsAuth="auth" color="color"/>
    """

    if "upload" in node.keys():
        f.write("<uploadServerDaemon name=\"" + node["upload"]["nm"] + "\" folder=\"" + node["upload"]["f"] + "\" needsAuth=\"" + node["upload"]["auth"] + "\" color=\"" + node["upload"]["color"] + "\"/>\n\n")

    """
    Web Server Daemon:
    <addWebServer name="nm" url="url" />
    """
    if "webServer" in node.keys():
        f.write("<addWebServer name=\"" + node["webServer"]["nm"] + "\" url=\"" + node["webServer"]["url"] + "\" /> \n\n")
    
    if "onlineServer" in node.keys():
        f.write("<addOnlineWebServer name=\"" + node["onlineServer"]["nm"] + "\" url=\"" + node["onlineServer"]["url"] + "\" /> \n\n")

    if "deathRow" in node.keys():
        f.write("<deathRowDatabase />\n\n")
    
    

    f.write("</Computer>")
    f.close()