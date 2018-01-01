# Sissi Xu S3C2 grading program

filename = "digitCount1.py"

# check total number of lines
file = open(filename,"r")
lines = file.readlines()
print("total number of lines",len(lines))
for line in open(filename):
    line = file.readline()
file.close()
if len(lines) <= 20:
    print("total number of lines <= 20")
else:
    print("total number of lines > 20")

# check how many lines over 80 chars
counter = 0
count1 = 0
for counter in range(len(lines)): 
#    print("%3d  line:  %4d chars" % (counter + 1, len(lines[counter]) - 1))
    if len(lines[counter]) > 81:
        count1 += 1
print ("number of lines with more than 80 characters: ", count1)

# check number of lines of comment
file = open(filename,"r")
stat = 0
#stat1 = 0
#for line in file:
#    if line[0] == "#":
#        stat += 1
#    else:
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            stat += 1
                    

# print score of comment
print("number of comment lines:\t" + str(stat))
if (stat / len(lines)) >= 0.2:
    print("your score for comment is 10")
else:
    print("your score for comment is 0")

# print score of lines
if len(lines) <= 20:
    print("your score for lines is 10")
elif len(lines) > 20 and len(lines) <= 40:
    print("your score for lines is 8")
elif len(lines) > 40 and len(lines) <= 60:
    print("your score for lines is 6")
else:
    print("your score for lines is 0")
file.close()
