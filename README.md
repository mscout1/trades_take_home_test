trades_take_home_test
=====================

This is a take home test given to me by an employer


Assumptions
===========
* Files will always have a single consistent internal format. (No mixing CSV and SDT in the same file)

* There will always be a first line containing header information

* The format of a file can be correctly determined by the presence of "," or ";" in the first line

* The other contents of the first line are for human use only, not relevent to parsing of the files

* Blank lines can be safely ignored.

* Unparsable lines should be reported then ignored.

* Files are of resonable length, such that they can both be read into memory at once.

* All valid symbols have been provided.

* We are to compare "contract, side, price, and quantity". I assume that contract includes all of(symbol, contract_type, strike, and month).

* symbols are unique across both systems
