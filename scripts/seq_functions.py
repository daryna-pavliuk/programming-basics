def gc_content(seq):
    gc = (seq.count("G") + seq.count("C"))/len(seq)*100
    gc = round(gc, 2)
    return(gc)

def reverce_complement(seq):
    complement = seq.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()
    rev_comp = complement[::-1]
    return(rev_comp)

def is_usable(seq, min_length = 30):
    if len(seq) >= min_length and seq.count("N") == 0:
        return(True)
    else:
        return(False)

def first_atg(seq):
    atg = seq.find("ATG")
    if atg >= 0:
        return(atg) 
    else:
        return("not found")

    

sequences = ["AAAGCTATGCAGCTACCGTTGGTGCACTCTTCTTCGACGCGGCTATC", 
             "ATATATATGATCGCGCGGCGAATTAGCGNNNC",
             "AAATTTCCCGGGAAAATTTCCCGGGAAATTTGGGCCC"]

for seq in sequences:
    print("GC:", gc_content(seq))
    print("Revese complement: ", reverce_complement(seq))
    print("First ATG: ", first_atg(seq))
    if is_usable(seq) == True:
        print("Usable")
    else:
        print("NOT usable")