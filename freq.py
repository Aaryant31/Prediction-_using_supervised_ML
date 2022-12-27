#abacusdata, print just the letter when the letter is not a. and when it a print "this is a"  -- do wit

str = "abacusdata"

outputstr=""

for i in str:
    if i == "a":
        print("This is a")
    if i != "a":
        outputstr+=i
print(outputstr)