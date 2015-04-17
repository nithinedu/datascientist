from sys import argv

script, filename = argv

print "we are going to erase %r" % filename
print "if you don't want that , hit ctrl-c (^c)."
print " if you do want that, hit ReTURN"

raw_input("?")

print "opening the file ..."
target = open(filename, 'w+')

print "truncating the file goodbye"

target.truncate()

print "now i am going to ask you for three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "i'm going to the write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")

#target.close()

#target = open(filename)

print target.read()

print "and finally, we close it"
target.close()
