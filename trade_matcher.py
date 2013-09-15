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
from decimal import Decimal
from copy import copy

#Mappings for sdt values and pretty formats
def bijection(d):
    """Makes a 2 way dictionary. Undefined if values are not unique"""
    d = copy(d)
    revd=dict([reversed(i) for i in d.items()])
    d.update(revd)
    return d


symbol_map = {
    'JF'  : '35',
    'QAL' : 'F-',
    'RT'  : '1W',
    }

buysell_map= {
    'B':1,
    'S':2,
    }

ctype_month_code = {
    'A': (1 , 'C'),
    'B': (2 , 'C'),
    'C': (3 , 'C'),
    'D': (4 , 'C'),
    'E': (5 , 'C'),
    'F': (6 , 'C'),
    'G': (7 , 'C'),
    'H': (8 , 'C'),
    'I': (9 , 'C'),
    'J': (10, 'C'),
    'K': (11, 'C'),
    'L': (12, 'C'),
    'M': (1 , 'P'),
    'N': (2 , 'P'),
    'O': (3 , 'P'),
    'P': (4 , 'P'),
    'Q': (5 , 'P'),
    'R': (6 , 'P'),
    'S': (7 , 'P'),
    'T': (8 , 'P'),
    'U': (9 , 'P'),
    'V': (10, 'P'),
    'W': (11, 'P'),
    'X': (12, 'P'),
}

months = bijection({
    'Jan' : 1 ,
    'Feb' : 2 ,
    'Mar' : 3 ,
    'Apr' : 4 ,
    'May' : 5 ,
    'Jun' : 6 ,
    'Jul' : 7 ,
    'Aug' : 8 ,
    'Sep' : 9 ,
    'Oct' : 10,
    'Nov' : 11,
    'Dec' : 12,
    })

ctype_long = {
    'C' : 'Call Option',
    'P' : 'Put Option',
    'F' : 'Future',
}



class Trade(object):
    """
    Trade class uses the csv symbols and codes in its internal format
    Futures are indicated by 'F'
    """
    def __init__(self, symbol, contract_type, strike, month, side, quantity, price, format=None):
        self.symbol        = str(symbol)
        self.contract_type = str(contract_type)
        self.strike        = int(strike) if strike is not None else None
        self.month         = int(month)
        self.side          = int(side)
        self.quantity      = int(quantity)
        self.price         = Decimal(price)
        self._format       = format

        assert self.contract_type in ('C','P','F')
        assert 1 <= self.month <= 12
        assert self.side in (1,2)

    @classmethod
    def fromCSV(cls, line):
        splitline = line.split(',')
        return cls(
            symbol        = splitline[0],
            contract_type = splitline[1] if splitline[1] else 'F',
            strike        = splitline[2] if splitline[2] else None,
            month         = splitline[3],
            side          = splitline[4],
            quantity      = splitline[5],
            price         = splitline[6],
            format='CSV')

    @classmethod
    def fromSDT(cls, line):
        splitline = line.split(';')
        contract_codes = splitline[0].split(' ')
        if contract_codes[1] in months:
            contract_type = 'F'
            month = months[contract_codes[1].capitalize()]
            strike = None
        else:
            month, contract_type = ctype_month_code[contract_codes[1][0]]
            strike = contract_codes[1][1:]
        return cls(
            symbol        = symbol_map[contract_codes[0]],
            contract_type = contract_type,
            strike        = strike,
            month         = month,
            side          = buysell_map[splitline[1]],
            quantity      = splitline[2],
            price         = splitline[3],
            format='SDT')

    @property
    def is_future(self):
        return self.contract_type == 'F'

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

    def __eq__(self, other):
        if not isinstance(other, Trade):
            return False
        return self._asTuple == other._asTuple

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._asTuple)

    def __str__(self):
        return ",".join( str(x) if x is not None else ''
                         for x
                         in self._asTuple
                         )

    __repr__ = __str__

def pretty_format(trade):
    symbol        = trade.symbol
    contract_type = ctype_long[trade.contract_type]
    strike        = trade.strike
    month         = months[trade.month]
    side          = 'Buy' if trade.side == 1 else 'Sell'
    quantity      = trade.quantity
    price         = trade.price

    strike_string = 'Strike: {0},'.format(strike) if not trade.is_future else ""
    fstring = "<Symbol: {0}, Type: {1}, Month: {2}, {3} Side: {4}, Qty: {5}, Price: {6}>"
    return fstring.format(
            symbol, contract_type, month, strike_string, side, quantity, price)

def parse_trade_file(file):
    header = file.readline()
    if ',' in header:
        trade_factory = Trade.fromCSV
    elif ';' in header:
        trade_factory = Trade.fromSDT
    else:
        raise ValueError("Format not recognized: {0}".format(filename1))

    lst = []
    for line in file:
        line=line.strip()
        if not line:
            continue
        try:
            lst.append(trade_factory(line))
        except (AssertionError,ValueError,TypeError) as e:
            print("Error parsing line:{0}\n\twith factory {1}\n\terror:{2}".format(
                line, trade_factory, e), file=sys.stderr)
            continue;
    return lst


def main(filename1, filename2):
    with open(filename1) as f1:
        L1 = parse_trade_file(f1)

    with open(filename2) as f2:
        L2 = parse_trade_file(f2)

    matches, only_in_1, only_in_2 = reconcile(L1, L2)

    print("{0} Trades found in both lists:".format(len(matches)))
    for t in matches:
        print(pretty_format(t))
    print("\n"+"="*40 + "\n")
    print("{0} Trades found only in file 1:".format(len(only_in_1)))
    for t in only_in_1:
        print(pretty_format(t))
    print("\n"+"="*75 + "\n")
    print("{0} Trades found only in file 2:".format(len(only_in_2)))
    for t in only_in_2:
        print(pretty_format(t))


def reconcile(list1, list2):
    """
    returns (matches, only_in_1, only_in_2)
    """
    set1 = set(list1)
    set2 = set(list2)

    matches = set1 & set2
    only_in_1 = set1 - set2
    only_in_2 = set2 - set1

    return matches, only_in_1, only_in_2

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file1")
    parser.add_argument("file2")
    args = parser.parse_args()

    main(args.file1, args.file2)

