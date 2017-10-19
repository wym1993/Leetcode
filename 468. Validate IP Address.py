class Solution(object):
    def validIPAddress(self, IP):
        def is_hex(s):
            hex_digits = set("0123456789abcdefABCDEF")
            for char in s:
                if not (char in hex_digits):
                    return False
            return True
        ary = IP.split('.')
        if len(ary) == 4:
            for i in xrange(len(ary)):
                if not ary[i].isdigit() or not 0 <= int(ary[i]) < 256 or (ary[i][0] == '0' and len(ary[i]) > 1):
                    return "Neither"
            return "IPv4"
        ary = IP.split(':')
        if len(ary) == 8:
            for i in xrange(len(ary)):
                tmp = ary[i]
                if len(tmp) == 0 or not len(tmp) <= 4 or not is_hex(tmp):    
                    return "Neither"
            return "IPv6"
        return "Neither"
            
        