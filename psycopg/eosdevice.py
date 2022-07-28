# generates generic eosdevice
import get_icon
class eosdevice():
    def __init__(self, sql_id, init_id, id, name, icon, isempty, passoverride):
        self.id = id
        self.name = name
        self.icon = get_icon.get_icon(icon)
        self.isempty = isempty
        if passoverride is None:
            self.passoverride = "alpine"
        else:
            self.passoverride = passoverride
        self.references = []

    def add_reference(self, reference):
        # reference: the object in question
        # reference_id, value dictating what the reference is (file, eos_device)
        self.references.append(reference)
        return

    def xml_file_gen(self):
        tbr = ["<eosDevice name=\"%s\" id=\"%s\" icon=\"%s\" empty=\"%s\" passOverride=\"%s\">"
            % (self.name, self.id, self.icon, self.isempty, self.passoverride)]
        
        for i in self.references:
            tbr.extend(i.xml_file_gen())
        
        tbr.append("</eosPhone>")

        return tbr

"""
if __name__ == '__main__':
    test = eosdevice('test', 'test', 'laptop', False, 'alpine')
    print('\n'.join(test.xml_file_gen()))
"""