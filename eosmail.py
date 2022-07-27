class eosmail():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def xml_file_gen(self):
        return ["<mail username=\"%s\" pass=\"%s\" />" % (self.username, self.password)]
    
if __name__ == '__main__':
    test = eosmail('username', 'password')
    print('\n'.join(test.xml_file_gen()))
