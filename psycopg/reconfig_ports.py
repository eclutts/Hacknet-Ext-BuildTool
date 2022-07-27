def reconfig_ports(ports):
    # okay so we can't use terms like 'ssh' in ports command
    tbr = dict()
    for x, y in ports.items():
        match x:
            case 'ssh':
                tbr[22] = y
            case 'ftp':
                tbr[21] = y
            case 'smtp':
                tbr[25] = y
            case 'web':
                tbr[80] = y
            case 'sql':
                tbr[1433] = y
            case 'kbt':
                tbr[104] = y
            case 'tor':
                tbr[6881] = y
            case 'ssl':
                tbr[443] = y
            case 'pac':
                tbr[192] = y
            case 'rtsp':
                tbr[554] = y
            case default:
                # should probably throw some error here.
                continue 
                
    return tbr

if __name__ == '__main__':
    test = dict(ssh=5, ftp=12, web=96)
    print(reconfig_ports(test))