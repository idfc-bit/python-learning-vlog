#dictionaries                     
indian_t20_squad = {
    "pace":"bumrah,harshith rana,siraj",
    "spin":"kuldeep,varun",
    "allrounder" : "shivam dube , abhishek,",
    "batsmans" : "samson,ishan kishan,suryakumar yadav" 
}
 
print(indian_t20_squad)


#kal bolimaklu
student_1 = {
    "roll number" : 2,
    "student name" : "likhith",
    "pens he has stolen": 3
}

student_2 = {
    "roll number" : 1,
    "student name" : "ayush",
    "pens he has stolen" : 4
}


print(student_1)
print(student_2)

x = student_1.pop("roll number")
print(x)
print(f" total pens those mf stolen = {student_1['pens he has stolen' ]+student_2['pens he has stolen' ]}")

