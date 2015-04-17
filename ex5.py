my_name = "Nithin"
my_age = 31 # not a lie
my_height = 74
my_height_cm = my_height * 2.54
my_weight = 180
my_eyes = 'Blue'

print "let's talk about %s." % my_name
print "ge's %d cm tall." % my_height_cm
print "he's %d pounds heavy." % my_weight
print "he's got %r eyes and %s name." % (my_eyes, my_name)

# this line is tricky, try to get it exactly right

print "if i add %r, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height)
