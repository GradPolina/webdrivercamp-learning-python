#!/usr/bin/python3

# option 1
num ="100%"
print ("Learning Python is fun {0}".format(num))
Learning Python is fun 100%

#oprion 2
 text_dict = {
       "num":"100%",
       "text":"Learning Python is fun"
        }
print("dict: {d[text]}, {d[num]}".format(d=text_dict))

# option 3
num = "100%"
text = "Learning Python is fun "
print("{0} {1}".format(text, num))


