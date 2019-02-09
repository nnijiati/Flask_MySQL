
def my_arguments(arg1, *args):
  print ("Got "+arg1+" and "+ ", ".join(args))


my_arguments("one") # output: "Got one and "
my_arguments("one", "two") # output: "Got one and two"
my_arguments("one", "two", "three") # output: "Got one and two, three"