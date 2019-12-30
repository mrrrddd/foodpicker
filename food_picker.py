import secrets

#collect food options from user, separated by a space
while True:
    food_choices = input("Enter some food options: ").split()
    if food_choices:
        #make a dict so we can tally results later
        food_dict = {}
        for choice in food_choices:
            food_dict[choice] = 0
        break
    else:
        print("You need to provide at least one option!")
        continue

#make sure there's one true winner (and less likely to have a tie (lazy))
for i in range(100):
    choice = secrets.choice(food_choices)
    food_dict[choice] += 1

print('---------------------------------------')
print("Looks like a good day for ..... %s !" % max(food_dict, key=food_dict.get).upper())
print('---------------------------------------')
#ww3 averted


#print(food_dict) #uncomment to see the count at the end
