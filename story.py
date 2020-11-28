funny_story = "One day in {} i saw my {} acting {}. She was  {}  in a big {} .Then she went to {} and did it again."

name = input("Enter a Town Name : ")
Familymember = input("Enter a family member  : ")
describingword = input("Enter A describing word : ")
actionword = input("Enter A action word : ")

thing = input("enter some thing : ")
place = input("enter some place name: ")

story = funny_story.format(name,Familymember,describingword,actionword,thing,place)

print(story)