sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA", "ATGNNNCGC"]
long = []
lengths = []
count = 0

for seq in sequences:
    # gc, seq, len
    print(f"\nSequence: {seq} \nLength: {len(seq)}")
    # list of lens
    lengths.append(len(seq))
    # count startswith ATG
    if seq.startswith('ATG'):
        count += 1
    # gc content
    gc = round(((seq.count('G')+seq.count('C'))/len(seq)*100), 2)
    print(f"GC content: {gc}\n")
    # seqs longer than 5
    if len(seq) > 5:
        long.append(seq)

# > 5 bases
print("Sequences longer tham 5 nucleotides:", *long)

#start with ATG
print(f"Start with ATG: {count}")

# avg len
print(f"Average sequence length: {sum(lengths)/len(lengths)}\n")

# codons for the longest sequence
longest_seq = sequences[lengths.index(max(lengths))]
for i in range(0, len(longest_seq)+1, 3):
    print(longest_seq[i:i+3])