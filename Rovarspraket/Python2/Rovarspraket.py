input = raw_input()
conso = 'bcdfghjklmnpqrstvwxyz'

#Encoder starts here
output = ""
for character in input:
    if character.lower() in conso:
        output += (character + "o" + character)
    else:
        output += character
print output

#Decoder starts here
decoded = ""
i=0
while i < len(output):
    if output[i].lower() in conso:
        decoded += output[i]
        i += 3
    else:
        decoded += output[i]
        i += 1
print decoded