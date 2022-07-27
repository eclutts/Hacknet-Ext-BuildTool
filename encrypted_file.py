class encrypted_file():
    def __init__(self, file_name, file_path, file_header, file_header_text, file_text, file_dec_password = '', file_extension = ''):
        self.file_name = file_name
        self.file_path = file_path
        self.file_extension = file_extension
        self.file_header = file_header
        self.file_header_text = file_header_text
        self.file_dec_password = file_dec_password
        self.file_text = file_text

    def xml_file_gen(self):
        tbr = ["<encryptedFile path=\"%s\" name=\"%s\" " % (self.file_path, self.file_name)]
        if self.file_extension != '':
            tbr[0] += "extension=\"%s\" " % self.file_extension
        tbr[0] += "ip=\"%s\" header=\"%s\"" % (self.file_header, self.file_header_text)
        if self.file_dec_password != '':
            tbr[0] += " pass=\"%s\"" % self.file_dec_password
        tbr[0] += ">"
        for i in self.file_text:
            tbr.append(i)
        tbr.append("</encryptedFile>")
        return tbr

if __name__ == '__main__':
    test = encrypted_file('test', 'home', '192.168.1.1', 'this is the header', ['this', 'is', 'a', 'test'], 'password', '.txt')
    print('\n'.join(test.xml_file_gen()))