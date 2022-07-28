class account():
    def __init__(self, sql_id, init_id, username, password, type):
        self.username = username
        self.password = password
        self.type = type
    
    def xml_file_gen(self):
        return ["<account username=\"%s\" password=\"%s\" type=\"%s\" />" % (self.username, self.password, self.type)]

if __name__ == '__main__':
    test = account('username', 'password', 'ADMIN')
    print("\n".join(test.xml_file_gen()))