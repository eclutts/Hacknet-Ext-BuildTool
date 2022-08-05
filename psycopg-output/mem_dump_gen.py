# memory dump generated

class mem_dump_gen():
    def __init__(self, sql_id, init_id, file_commands, file_data, file_images):
        self.file_data = file_data
        self.file_commands = file_commands
        self.file_images = file_images

    def xml_file_gen(self):
        tbr = ["<Memory>"]
        if self.file_data != ['']:
            tbr.append("\t<Data>")
            for i in self.file_data:
                tbr.append("\t\t<Block>%s</Block>" % i)
            tbr.append("\t</Data>")
        
        if self.file_commands != ['']:
            tbr.append("\t<Commands>")
            for i in self.file_commands:
                tbr.append("\t\t<Command>%s</Command>" % i)
            tbr.append("\t</Commands>")
        
        if self.file_images != ['']:
            tbr.append("\t<Images>")
            for i in self.file_images:
                tbr.append("\t\t<Image>%s</Image>" % i)
            tbr.append("\t</Images>")
        
        tbr.append("</Memory>")
        return tbr


if __name__ == '__main__':
    test = mem_dump_gen(['test_1', 'test_7'], ['test_2'], [''])
    print('\n'.join(test.xml_file_gen()))
