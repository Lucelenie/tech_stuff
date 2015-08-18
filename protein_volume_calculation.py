# This program prompts user for concentration, molecular_weight and desired molarity
# and outputs the amount of volume needed for the desired molarity.

# Get molecular_weight and extinction coefficient from Peanut.
# Src: MW 32689.6 Da, epsilon 52370 M^-1 cm^-1

# Get concentration from the Denovix in mg/mL.

concentration = input("What is the concentration of the protein in mg/mL? ")
molecular_weight = input("What is the molecular weight of the protein? ")
molarity_2 = input("At what concentration you need the protein (molarity)? ")

molarity_1 = (concentration / molecular_weight)
volume_1 = round((((0.014 * 0.0000005)/ molarity_1) * 1000000), 1)
buffer_1000 = round(1000 - volume_1) 

print "You will need %r uL of your protein and 13.%r mL of buffer for it to be at %r uM." % (
    volume_1, buffer_1000, molarity_2)