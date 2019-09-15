from firebase.firebase import FirebaseApplication
fba=FirebaseApplication("https://raghava2211-24c32.firebaseio.com/")
fba.put("employee/","101",{"name":"ravi","salary":185000.00})