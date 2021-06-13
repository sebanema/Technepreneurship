def Roman(n):
#Characters used in Roman numerals
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#Previous character and output integer
    prev = 0
    int = 0
#Iterate through characters
    rom = len(n)
    for i in range(rom-1, -1, -1):
#If greater than or equal to previous, add to output
        if rom_n[n[i]] >= prev:
            int += rom_n[n[i]]
#If smaller than previous, update previous
        else:
            int -= rom_n[n[i]]
        prev = rom_n[n[i]]
    return int

print(Roman("MMMCCCCXX"))