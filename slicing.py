#Indexing

indexing_list = "My family is blessed"
print(indexing_list)

# There is positive and negative indexing.
# Positive Indexing starts from 0
# Positive prints the number before
# Negative indexing starts from -1
print(indexing_list[0])
print(indexing_list[1])
print(indexing_list[2])
print(indexing_list[3])

print(indexing_list[-1]) #Negative indexing
print(indexing_list[-2])

#Slicing a string ie to get a sub string from a string
print(indexing_list[0:3])
print(indexing_list[:])
print(indexing_list[:6])

#INDEXING

class_age = [1990, 1967, 2000, [[1930, 8765, 2004], [783, 756, 456]]]
print(class_age[-1])

project = {'key1' : 1991, 'key2' : 1992, 'key3' : 1993, 'key4' : 1987, 'key5': 6,}
print(project['key1'])

class_age=[1990, 2000, 1987, 1954, [1995, 1980, 1979, 1960, [2000, 2001,2002]], 1995]

nested = [['name', 'age', 'travel_history', 'state'],
('date_of_birth', 'LGA', 'occupation', [4, 5, 6, 7, 8]),
[3, 45, 7, ('HP', 'Macbook', 'Find me', {"a": [1, 3, 5, 6, {"b":'try finding me'}]})]]
#print(len(nested))

nested = [['name', 'age', 'travel_history', 'state'],
('date_of_birth', 'LGA', 'occupation', [4, 5, 6, 7, 8]),
[3, 45, 7, ('HP', 'Macbook', 'Find me', {"a": [1, 3, 5, 6, {"b":'try finding me'}]})]]
print(nested[2][3][3]['a'][4]['b'])

nested = [['name', 'age', 'travel_history', 'state'],
('date_of_birth', 'LGA', 'occupation', [4, 5, 6, 7, 8]),
[3, 45, 7, ('HP', 'Macbook', 'Find me', {"a": [1, 3, 5, 6, {"b":'try finding me'}]})]]
print(nested[-1][-1][-1]['a'][-1]['b'])

list = ['jobina', 'tina', 'joy', 'rose', 'joy']
print(list[0])
list = ['i have been changed']
print(list[0])

#LOOP

#Why should we use loops?

#A loop is used for repeated computation on a collection

#class_age = [1968, 1845, 2045, 2367]
#for w in class_age:
#    print(w)

#class_age = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#for w in class_age:
#    if w <= 20:
#        print(w)
    
    







    