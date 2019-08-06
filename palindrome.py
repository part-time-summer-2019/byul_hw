palin_string = input('Enter a string: ')


def palindrome(palin_string):

  #find the length of the input
  ranger = len(palin_string)
  start = 0
  end = 0

  #add all of the palindrome that is found in the input string
  palindrome_list = []
  palindrome_final = []
  final_word = 0
  for i in range(1, int(ranger)):
    start = i - 1
    end = i + 1 

    #check to see if there are words that start and end with same letter
    while start >= 0 and end < ranger:
      if palin_string[start] == palin_string[end]:
        palin1 = palin_string[start:end+1]
        palindrome_list.append(palin1)
        start -= 1
        end += 1
        continue
      else:
        start -+ 1
        end += 1
        continue
  #list of strings that start / end with same letter      
  print(palindrome_list)

  #check to see if the strings in palindrome_list are palindrome 
  for i in palindrome_list:
    if i == i[::-1]:
      palindrome_final.append(i)
      palindrome_final.sort()
  #print the longest string    
  print(palindrome_final[-1])

palindrome(palin_string)
