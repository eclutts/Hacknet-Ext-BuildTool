class eosnote():
    def __init__(self, sql_id, note_id, init_id, text):
        self.text = text
    
    def xml_file_gen(self):
        tbr = ["<note>%s" % self.text[0]]
        for i in self.text[1:]:
            tbr.append(i)
        tbr[-1] += "</note>"
        return tbr

"""
if __name__ == '__main__':
    test = eosnote(['this', 'is', 'a', 'test'])
    print('\n'.join(test.xml_file_gen()))
"""