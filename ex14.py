from sys import argv

script, user_name = argv
prompt = '> '

print "hi %s, i'm the % script." % (user_name, script)
print "i'd like to ask you a few questions."
print "do you like me %s?" %user_name
likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
you live %r. Not sure where that is.
and you have a %r computer. Nice.
""" % (likes, lives, computer)