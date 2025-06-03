#test if a number is a prime number



def prime(number):
  for i in range(1,number+1):
    if number%i == 0:
      print(number, i)
