seq = input()
print('Sequence length:', len(seq))
g = int(seq.count('G'))
c = int(seq.count('C'))
gc = (g+c)/len(seq)*100
print('GC content:', round(gc, 2), '%')