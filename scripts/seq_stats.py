sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA"]
gene = ("BRCA1", "chr17", 43044295, 43125483)

print(f'There are {len(sequences)} sequences in the list \nThe first sequence: {sequences[0]} \nThe last sequence: {sequences[-1]}')
sequences.append('AATTCCGG')

lengths = []
for seq in sequences:
    lengths.append(len(seq))
print(f'Lengths of sequences: {lengths}')

print(f'Shortest sequence: {min(sequences)} \nLongest sequence: {max(sequences)} \nAverage lenght: {sum(lengths)/len(lengths)}')

name, chrom, start, stop = gene
print(f'{name} is on the {chrom} and is {stop-start} bases long.')

#bonus
genes = [('BRCA1', 81188), ('TP53', 25759)]
print(f'Length of TP53: {genes[1][1]}')

gene[0] = 'BRCA000'
