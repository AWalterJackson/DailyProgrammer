input = int(raw_input())

while input != 1:
    if input % 3 == 0:
        print str(input) + " 0"
        input /= 3
    else:
        if (input + 1) % 3 == 0:
            print str(input) + " 1"
            input = (input + 1) / 3
        else:
            print str(input) + " -1"
            input = (input - 1) / 3
print input
        #comment this biiiiitch
		#you dont even know