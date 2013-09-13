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
    def __init__(self, arg):
        super(Trade, self).__init__()
        self.arg = arg

    @classmethod
    def fromCSV(cls):
        pass

    @classmethod
    def fromSDT(self):
        pass

    def __eq__(self):
        pass

    def __hash__():
        pass

    def __str__(self):
        pass


def main(filename1, filename2):
    pass

def reconcile(list1, list2):
    """
    returns (matches, only_in_1, only_in_2)
    """

if __name__ == '__main__':
    main(*sys.argv[1:]) #TODO:replace this with argparse
