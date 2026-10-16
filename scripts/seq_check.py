seq = 'ATGCGTAGCTAGCNATCGTNATCATGNGATGANNGTAGA'

gc = (seq.count('G') + seq.count('C'))/len(seq)*100

if len(seq) <= 30:
    print('too short')
if 'N' in seq:
    print("contains unknown bases")
if gc > 60:
    print('GC rich')
elif gc < 40:
    print('AT rich')
else:
    print("balanced")
if seq.startswith('ATG') and len(seq) % 3 == 0:
    print('possible ORF')