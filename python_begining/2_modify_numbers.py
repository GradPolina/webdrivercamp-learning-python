#!/usr/bin/python3

# option 1
num =3.14159265533789547842121
num_round = round(num,2)
print ("Learning Python is fun {0} %".format(num_round))

#oprion 2
text_dict = {
       "num":round(3.1415192057893456,2),
       "text":"Learning Python is fun"
        }
print("dict: {d[text]} {d[num]} %".format(d=text_dict))

# option 3
num = 3.1415149874569
num_around =round(num,2)
text = "Learning Python is fun "
print("{0} {1} %".format(text,num_round))

# option 4
print("Learning Python is fun %.2f $" % (3.141546458))

# option 5
num = 3.141547895879412
print ("Learning Python is fun {:2f} $".format(num))


