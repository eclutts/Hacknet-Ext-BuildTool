# generates default file class.
class file():
    def __init__(self, file_name, file_path, file_text):
        self.file_name = file_name
        self.file_path = file_path
        self.file_text = file_text
    
    def xml_file_gen(self):
        tbr = ["<file path=\"%s\" name=\"%s\">%s" % (self.file_path, self.file_name, self.file_text[0])]
        for i in self.file_text[1:]:
            tbr.append('%s' % i)
        tbr[-1] += "</file>"
        return tbr

if __name__ == '__main__':
    test = file('test', 'home', ['this', 'is', 'a', 'test'])
    print('\n'.join(test.xml_file_gen()))