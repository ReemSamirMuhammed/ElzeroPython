# practicing  for loop
#Dictionary

mySkills = {"html":"90%",
"css":"80%",
"php":"70",
"js":"60",
"python":"50"}

print(mySkills['html'])
print(mySkills.get("python"))
for skill in mySkills:
    print (skill)  #printing just keys
    print(f"my progress in languages {skill} is: {mySkills.get(skill)}")
