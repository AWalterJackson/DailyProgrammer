hours = {0:"Twelve", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven"}
minutes = {0:"", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
tens = {0:"oh", 1:"ten", 2:"twenty", 3:"thirty", 4:"fourty", 5:"fifty"}

time = raw_input("Enter a time: ").split(':')

if int(time[0]) >= 12:
    suffix = "pm"
else:
    suffix = "am"

if time[1][0] == '1':
    print "It's " + hours[int(time[0])%12] + " " + minutes[int(time[1])] + " " + suffix
elif time[1] == '00':
    print "It's " + hours[int(time[0])%12] + " " + suffix
else:
    print "It's " + hours[int(time[0])%12] + " " + tens[int(time[1][0])] + " " + minutes[int(time[1][1])] + " " + suffix