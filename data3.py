from firebase.firebase import FirebaseApplication
fba=FirebaseApplication("https://raghava2211-24c32.firebaseio.com/")

s_rno=int(input("ROLL NO: " ))
s_name=input("NAME: ")
s_marks=int(input("TOTAL MARKS: "))
fba.put("student/",s_rno,{"name":s_name,"marks":s_marks})
print("students is saved")