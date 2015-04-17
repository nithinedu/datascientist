from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" %(from_file, to_file)

# we could do these to on one line too how?

in_file =open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" % len(indata)

print "does the output file exist? %r" % exists(to_file)
print "ready, hit return to continue, ctrl-c to abort"
raw_input()

out_file = open(to_file, "w")
out_file.write(indata)
out_file.close()
out_file = open(to_file)
outdata = out_file.read()

print "output file lenght %d" % len(outdata)
print "Output file exist %r " %exists(to_file)

print "allright, all don"

out_file.close()
in_file.close()