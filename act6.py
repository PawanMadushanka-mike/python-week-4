import sys

if len(sys.argv)<2:
    print("Too few arguments")

elif len(sys.argv)>2:
    print("Too much arguments")

else:
    print("my name is ",sys.argv[1])