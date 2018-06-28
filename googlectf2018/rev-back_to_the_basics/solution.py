import struct

bits = (0.062500000001818989403545856475830078125, 0.0156250000004547473508864641189575195312, 0.0039062500001136868377216160297393798828, 0.0009765625000284217094304040074348449707, 0.0002441406250071054273576010018587112427, 0.0000610351562517763568394002504646778107, 0.0000152587890629440892098500626161694527, 0.0000038146972657360223024625156540423632, 0.0000009536743164340055756156289135105908, 0.0000002384185791085013939039072283776477, 0.0000000596046447771253484759768070944119, 0.000000014901161194281337118994201773603, 0.0000000037252902985703342797485504434007)

s = ""    
for target in (0.671565706376017, 0.682612358126820, 0.682552023325146, 0.667647300753773, 0.682310803327740, 0.670638734940470, 0.729427094105661, 0.683334092143953, 0.729182238224924, 0.682352954987467, 0.745769257191599, 0.666743217501820, 0.682352764997662, 0.670634204987467, 0.733381925616444, 0.667648012284220, 0.749690691474855, 0.682356773410023, 0.670817057136476):
    target -= (0.6666666666612316235641 - 0.00000000023283064365386962890625)
    
    for i in xrange(13):
        if target < bits[i]:
            s += "0"
        else:
            s += "1"
            target -= bits[i]
            

ss = ""
for i in xrange(0, len(s), 8):
    ss += chr(int(s[i:i+8][::-1], 2))
    
print repr(ss)