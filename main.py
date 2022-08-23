friends = ["Kevin" , "Karen" , "Jim" , "Oscar" , "Toby"]

friends.append("Creed")
# add the element "Creed" into the friends list

friends.insert(2 , "Kelly")
# add Kelly in the no. 2 index of friends list

friends.remove("Oscar")
# remove Oscar from the list

friends.pop()
# remove the last element in the list

print(friends.index("Kevin"))
# to find Kevin in the friends list

print(friends.count("Jim"))
# to know how many times Jim shows up

friends.sort()
# to sort the list from A to Z

friends.reverse()
# to sort the list from Z to A

friends_2 = friends.copy()
# to copy friends list into friends_2 list