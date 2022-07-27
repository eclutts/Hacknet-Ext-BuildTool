# basing this off of the default computer generated on the website.
# I do not believe this is the full number of cases that are allowed.
# correction: this will reference another memory dump gen, which is identical HOWEVER
class memory_dump_file():
    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path
        self.references = []
    
    def add_reference(self, obj):
        self.references.append(obj)

    def xml_file_gen(self):
        tbr = ["<memoryDumpFile name=\"%s\" path=\"%s\">" % (self.file_name, self.file_path)]
        for i in self.references:
            tbr.extend(i.xml_file_gen())
        tbr.append("</memoryDumpFile>")
        return tbr

if __name__ == "__main__":
    test = memory_dump_file('test.md', 'home')
    print('\n'.join(test.xml_file_gen()))
