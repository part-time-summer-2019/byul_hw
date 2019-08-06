#string = abcracecarxyz
#l_string = left
#r_string = right

palin_string = input('enter a string: ')
end = len(palin_string)
start = 0

palindrome_list = []

def palindrome(palin_string, start,  end):
    
    #l_string moves from left to right
    #r_string moves from right to left
    while start >= 0 and end< len(palin_string):
        
        #will start from first and last letter of the string
        if palin_string[start] != palin_string[end]:
            break
        
        #add the palindrome to a list 
        palindrome_list.append(palin_string[start : end + 1])
        
        #sort the palindrome
        sort_list = sorted(palindrome_list, key=len)
        
        #print the longest 
        print(sort_list[-1])
        
        start = start + 1
        end = end - 1

palindrome(palin_string, start,  end)