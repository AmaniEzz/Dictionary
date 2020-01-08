import json
from difflib import get_close_matches

def Translat(word):
   with open('data.json', 'r') as f:
     data_dict = json.load(f)
     #check first if the word in data as it is
     if(word in data_dict):
       return data_dict[word]
     #if not check other conditions; first turn it to lowercase and check
     #if not then check for Title, if not then turn it all into UPPERcase and check
     #finally if not then suggest a closer match to the user 
     #if the user choose yes and the word is found then yah we did it!
     #if not the word does not found !!
     elif(word not in data_dict):
         newstr = word.lower()
         if(newstr in data_dict):
             return data_dict[newstr]
         elif(newstr.title() in data_dict):
             return data_dict[newstr.title()]
         elif(newstr.upper() in data_dict):
             return data_dict[newstr.upper()]
         elif len(get_close_matches(newstr , data_dict.keys())) > 0 :
            print("did you mean %s instead" %get_close_matches(newstr, data_dict.keys())[0])
            decide = input("press y for yes or n for no")
            if decide == "y":
               return data_dict[get_close_matches(newstr , data_dict.keys())[0]]
            elif decide == "n":
               return("Then the word you enterd sadly is not correct try again!")
            else:
               return("You have entered wrong input please enter just y or n")
         else:
              return("Then the word you enterd sadly is not correct try again!")
              

print("Enter a word to translate!:")
str= input()
print(f"The meaning(s) of {str}:")
print("\n")
output = Translat(str)
count=1
if type(output) == list:
    for item in output:
      print([count])
      print(item)
      count+=1