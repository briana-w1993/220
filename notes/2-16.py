def encode ():
   word = input("enter a word: ")
   nums = []

   for letter in word:
       num = ord(letter)
       nums.append(str(num))
   print(num, end=" ")


