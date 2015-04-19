dna_input = "A T G T T T C G A G G C T A A"
dna_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}

dna_list = dna_input.split(" ")

print(dna_list)

for i in dna_list:
    dna_list[dna_list.index(i)] = [v for k, v in dna_dict.items() if i in k]

for i in dna_list:
    dna_list[dna_list.index(i)] = i[0]

print(dna_list)
