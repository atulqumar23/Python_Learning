'''4. Create a file named “4.txt” that contains all unique ticker symbols along with their 
corresponding `undrlygFinInstrmId`. 
• Extract both columns and remove duplicates. 
• Format each line as: SYMBOL - underlygFinInstrmId 
• Save this mapping into a new text file using standard file writing operations. '''

file_path = R"E:\SEPTEMBER\contract_file\contract -3.txt"
unique_pairs = set()

with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split('|')
        if len(parts) > 10:
            symbol = parts[3]
            underlygFinInstrmId = parts[1]
            unique_pairs.add((symbol, underlygFinInstrmId))
print(unique_pairs)
with open('4.txt', 'w') as f:
    for symbol, underlygFinInstrmId in unique_pairs:
        f.write(f"{symbol} - {underlygFinInstrmId}\n")


