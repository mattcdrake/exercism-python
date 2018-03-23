def to_rna(dna_strand):
    out_dna = ""
    for e in dna_strand:
        if e == "G":
            out_dna += "C"
        elif e == "C":
            out_dna += "G"
        elif e == "T":
            out_dna += "A"
        elif e == "A":
            out_dna += "U"
        else:
            raise ValueError("Non-RNA character supplied")
    return out_dna
