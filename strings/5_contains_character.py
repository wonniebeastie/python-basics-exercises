# Write code that checks whether the string `char_sequence` contains the 
# character `x`.
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

print('x' in char_sequence)     # True
print(char_sequence.find('x'))  # 26 (returns -1 if not found)
print(char_sequence.count('x')) # 1 (return 0 if not found)
print(char_sequence.index('x')) # 26 (raises an error if not found)
