def strentgh(text, variable) :
 
     for char in text:
       if char.isupper():
           variable += 20
       elif char.isalpha():
         variable += 20
       elif char.islower():
          variable += 20
     if text.length > 8:
        variable+=20
while True :
   print ("1: Enter Text")
   print ("2: Exit")
   choice =""
   choice == input()
   if choice == "1":
      text = input("Enter Text: ")
      result = strentgh(text, variable)
      print (f"Your Password is : {result}")
      if text.length > "80":
         print (" /tstrong")
      elif text <"80" :
         print ("is weak, Try again: ")
   elif choice == "2":
      exit() 
      
