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

ctype_month_code = {
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

months = {
    'Jan' : '1' ,
    'Feb' : '2' ,
    'Mar' : '3' ,
    'Apr' : '4' ,
    'May' : '5' ,
    'Jun' : '6' ,
    'Jul' : '7' ,
    'Aug' : '8' ,
    'Sep' : '9' ,
    'Oct' : '10',
    'Nov' : '11',
    'Dec' : '12',
    }



class Trade(object):
    """
    Trade class uses the csv symbols and codes in its internal format
    Futures are indicated by 'F'
    """
    def __init__(self, symbol, contract_type, strike, month, side, quantity, price, format=None):
        self.symbol        = symbol
        self.contract_type = contract_type
        self.strike        = strike
        self.month         = month
        self.side          = side
        self.quantity      = quantity
        self.price         = price
        self._format       = format

    @classmethod
    def fromCSV(cls, line):
        splitline = line.split(',')
        return Trade(
            symbol        = splitline[0],
            contract_type = splitline[1] if splitline[1] else 'F',
            strike        = splitline[2] if splitline[2] else None,
            month         = splitline[3],
            side          = splitline[4],
            quantity      = splitline[5],
            price         = splitline[6],
            format='CSV')

    @classmethod
    def fromSDT(self, line):
        splitline = line.split(';')
        contract_codes = splitline[0].split(' ')
        if contract_codes[1] in months:
            contract_type = 'F'
            month = months[contract_codes[1]]
            strike = None
        else:
            contract_type, month = ctype_month_code[contract_codes[1][0]]
            strike = contract_codes[1][1:]
        return Trade(
            symbol        = symbol_map[contract_codes[0]],
            contract_type = contract_type,
            strike        = strike,
            month         = month,
            side          = splitline[1],
            quantity      = splitline[2],
            price         = splitline[3],
            format='SDT')

    @property
    def _asTuple(self):
        return (self.symbol,
                self.contract_type,
                self.strike,
                self.month,
                self.side,
                self.quantity,
                self.price,
                )

    def __eq__(self):
        pass

    def __hash__():
        pass

    def __str__(self):
        return ",".join( str(x) if x is not None else ''
                         for x
                         in self._asTuple
                         )

    __repr__ = __str__

def parse_trade_file(file):
    header = file.readline()
    if ',' in header:
        trade_factory = Trade.fromCSV
    elif ';' in header:
        trade_factory = Trade.fromSDT
    else:
        raise ValueError("Format not recognized: {0}".format(filename1))

    return [trade_factory(line.strip()) for line in file if line.strip()]


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
