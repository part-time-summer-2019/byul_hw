palin_string = input('Enter a string: ')


def palindrome(palin_string):
  ranger = len(palin_string)
  start = 0
  end = 0
  palindrome_list = []
  final_word = 0
  for i in range(1, int(ranger)):
    start = i - 1
    end = i + 1 
    while start >= 0 and end < ranger:
      if palin_string[start] == palin_string[end]:
        hello = palin_string[start:end+1]
        palindrome_list.append(hello)
        start = start - 1
        end = end + 1
        continue
      else:
        start = start - 1
        end = end + 1
        continue
  # print(palindrome_list)
  for i in palindrome_list:
    if i == i[::-1]:
      if len(i) > len(str(final_word)):
        final_word = i
  print(final_word)


palindrome(palin_string)
