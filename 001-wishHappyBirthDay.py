#This program will accept a username and his age and print happy birthday for each year

text_Output_file = open("D:\\_Aman\\Python\\Python101\\001Output.txt", "w")
'''
#/Accept username as input
userName= input("Enter your name : ")
print ('user name is : ' + userName)

age= input("Enter your age : ")
print (age)

for x in range(1, int(age)):
  print ('Wish you happyBirthDay : ' + userName + 'for birthday #'+str(x)+' year')
'''
firstLineOfFile = open("D:\\_Aman\\Python\\Python101\\001UserNameAndBirthday.txt", "r")
#print(firstLineOfFile.readline())
firstLineString= firstLineOfFile.readline().replace('\n', '')

#firstLineString = firstLineOfFile

tempIndividualWordsArray=firstLineString.split()
userName,age = tempIndividualWordsArray[0],tempIndividualWordsArray[1]

print ('user name is : ' + userName)
print (age)
for x in range(1, int(age)):
  print ('Wish you happyBirthDay : ' + userName + 'for birthday #'+str(x)+' year')
  text_Output_file.write('Wish you happyBirthDay : ' + userName + 'for birthday #'+str(x)+' year'+'\n')

text_Output_file.close()
