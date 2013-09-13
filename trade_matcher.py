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
