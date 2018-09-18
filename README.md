# info_kod

### Autoriai: Dovydas Kičiatovas ir Dovilė Preidytė

Informacijos kodavimo/dekodavimo programos pagal Elias C1/C2 ir LZW algoritmus.
Kodas parašytas Python 3.6 kalba.

Elias C1 ir C2 kodavimas - interval.py, dekodavimas - decoder.py

interval.py naudojimas:
interval.py [C1 arba C2] [koduojamo failo vardas] [užkoduoto failo vardas]

decoder.py naudojimas:
decoder.py [užkoduoto failo vardas] [atkoduoto failo vardas]

LZW kodavimas - lzw_encoding.py, dekodavimas - lzw_decoding.py

lzw_encoding.py naudojimas:
interval.py [koduojamo failo vardas] [užkoduoto failo vardas] [žodyno limitas] [ar užšaldyti žodyną, pasiekus limitą]

lzw_decoding.py naudojimas:
decoder.py [užkoduoto failo vardas] [atkoduoto failo vardas]
