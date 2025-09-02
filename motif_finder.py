print("Welcome to the Motif Finder!")

motif = ('ATCG', 'ATC','AGC')

sequence_1 = input("Enter the DNA sequence you want to check motif's: ").upper()
  
          
for m in sequence_1:
    if m in sequence_1:
        print("Motifs is present there")
        break
    else:
        print("No Motifs founds")


print("")        