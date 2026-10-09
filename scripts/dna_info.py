seq = 'AATTCTGTAGCTGGTACCTATATATGCCCGTA'
print('Sequence length:', len(seq))
g = int(seq.count('G'))
c = int(seq.count('C'))
print('GC content:', (g+c)/len(seq)*100, '%')