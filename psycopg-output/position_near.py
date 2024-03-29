
class position_near():
    def __init__(self, sql_id, init_id, target_id, position, total, extraDistance, force, target):
        self.target = target
        self.position = position
        self.total = total
        self.extraDistance = extraDistance
        self.force = str(force).lower()
    
    def xml_file_gen(self):
        tbr = ["<positionNear target=\"%s\" " % self.target]
        tbr[0] += "position=\"%s\" " % self.position
        tbr[0] += "total=\"%s\" " % self.total
        tbr[0] += "extraDistance=\"%s\" " % self.extraDistance
        tbr[0] += "force=\"%s\" />" % self.force
        return tbr

if __name__ == '__main__':
    test = position_near('test', '1', '3', '0.0', 'false')
    print('\n'.join(test.xml_file_gen()))