"""
Trade Reconciler.

This script reads in two files, each containing a list of trades'
It then attempts to reconcile the two, printing a list of matches,
and two lists of non-matches.

This script can comprehend 2 different formats, csv and sdt
(Comma Seperated Values and Semicolen Delimited Text)
These formats vary in more then just seperator and file
extention. See "MO Developer Take-Home Test.docx" for details
"""

import sys

#Mappings for sdt values
symbol_map = {
    'JF'  : '35',
    'QAL' : 'F-',
    'RT'  : '1W',
    }

buysell_map= {
    'B':'1',
    'S':'2',
    }

otype_month_code = {
    'A': ('1' , 'C'),
    'B': ('2' , 'C'),
    'C': ('3' , 'C'),
    'D': ('4' , 'C'),
    'E': ('5' , 'C'),
    'F': ('6' , 'C'),
    'G': ('7' , 'C'),
    'H': ('8' , 'C'),
    'I': ('9' , 'C'),
    'J': ('10', 'C'),
    'K': ('11', 'C'),
    'L': ('12', 'C'),
    'M': ('1' , 'P'),
    'N': ('2' , 'P'),
    'O': ('3' , 'P'),
    'P': ('4' , 'P'),
    'Q': ('5' , 'P'),
    'R': ('6' , 'P'),
    'S': ('7' , 'P'),
    'T': ('8' , 'P'),
    'U': ('9' , 'P'),
    'V': ('10', 'P'),
    'W': ('11', 'P'),
    'X': ('12', 'P'),
}


class Trade(object):
    """Trade class uses the csv format as it's internal format"""
    def __init__(self, *args, format=None): #symbol, callput, strike, month, side, quantity, price):
        #Todo: Stub
        self.all = args
        self.format = format

    @classmethod
    def fromCSV(cls, line):
        return Trade(line, format='CSV')

    @classmethod
    def fromSDT(self, line):
        return Trade(line, format='SDT')

    def __eq__(self):
        pass

    def __hash__():
        pass

    def __str__(self):
        return "{0},{1}".format(self.format, str(self.all))

    __repr__ = __str__

def parse_trade_file(file):
    header = file.readline()
    if ',' in header:
        trade_factory = Trade.fromCSV
    elif ';' in header:
        trade_factory = Trade.fromSDT
    else:
        raise ValueError("Format not recognized: {0}".format(filename1))

    return [trade_factory(line) for line in file]


def main(filename1, filename2):
    #Todo: Stub
    with open(filename1) as f1:
        L1 = parse_trade_file(f1)

    with open(filename2) as f2:
        L2 = parse_trade_file(f2)

        from pprint import pprint
        pprint(list(L1))
        pprint(list(L2))


def reconcile(list1, list2):
    """
    returns (matches, only_in_1, only_in_2)
    """

if __name__ == '__main__':
    main(*sys.argv[1:]) #TODO:replace this with argparse
