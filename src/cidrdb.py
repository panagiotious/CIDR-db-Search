'''
# REQUIREMENTS
py-radix (https://code.google.com/p/py-radix/)


# USAGE

import cidrdb
db = cidrdb.cidrdb('pathOfPickledTree')
x = db.searchFor('195.251.161.10')
if x:
    print x.asn, x.isp, x.cc, x.reg, x.network, x.prefix
else:
    print 'Not found'

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
asn = ASN
ISP = ISP
cc = Country Code
reg = Registar
network = Starting IP of CIDR
prefix = CIDR

'''

import radix 
import cPickle as pickle

class cidrdb:
    # Read and load the pickle file
    def __init__(self, pickleFileName):
        self.tree = radix.Radix()
        self.tree = pickle.load(open(pickleFileName, 'rb'))
    
    def searchFor(self, ip):
        node = self.tree.search_best(ip)
        if node:
            return Node(node.network, node.prefix, node.data['asn'], node.data['isp'], node.data['cc'], node.data['reg'])
        else:
            return None
    
class Node:
    __slots__ = ('network', 'prefix', 'asn', 'isp', 'cc', 'reg')
    def __init__(self, net, pref, asn, isp, cc, reg):
        self.network = net
        self.prefix = pref
        self.asn = asn
        self.isp = isp
        self.cc = cc
        self.reg = reg