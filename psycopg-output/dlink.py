class dlink():
    def __init__(self, target_id):
        self.target_id = target_id
    
    def xml_file_gen(self):
        return ["<dlink target=\"%s\" />" % self.target_id]
    
if __name__ == '__main__':
    test = dlink('test')
    print('\n'.join(test.xml_file_gen()))