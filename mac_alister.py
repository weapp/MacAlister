import urllib2, base64, re

class MacAlister:
    def get_password(self):
        pwdpage = urllib2.urlopen("http://192.168.1.1/password.cgi").read()
        return re.search("pwdAdmin = '(.*)';", pwdpage).group(1)

    def get_macs(self, user=1234, pwd=None):
        if pwd is None:
            pwd = self.get_password()
        req = urllib2.Request("http://192.168.1.1/wlstationlist.cmd")
        base64string = base64.encodestring('%s:%s' % (1234, pwd))[:-1]
        req.add_header("Authorization", "Basic %s" % base64string)
        macspage = urllib2.urlopen(req).read()
        return re.findall("<tr> <td><p align=center> (.*)", macspage)


if __name__ == '__main__':
    mac_alister = MacAlister()
    for mac in mac_alister.get_macs():
        print mac
