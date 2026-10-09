seq = 'AATTCTGTAGCTGGTACCTATATATGCCCGTA'
print(f'Length: {len(seq)}')
gc = round((seq.count("G")+seq.count("C"))/len(seq)*100, 2)
print(f'GC content: {gc} %')
print(f'First codon: {seq[:3]}, second codon: {seq[-3:]}')
print(f'RNA: {seq.replace("T","U")}')
rev_comp = seq.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()[::-1]
print(f'Reverse complement: {rev_comp}')
print(f'First codon is ATG: {seq.startswith("ATG")}')
print(f'First ORF: {seq[0:]} \nSecond ORF: {seq[1:]} \nThird ORF: {seq[2:]}')