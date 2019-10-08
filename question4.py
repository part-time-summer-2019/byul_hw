#Big-O notation
#O(n) --> push 0 to the right 
#cant use sort

def sortnum(the_list, listlen):
    count = 0
    
    for i in range(listlen): #to see numbers in the list that isn't a zero
        '''
        using traverse - count number of non zeros
        if the element is not a zero then change the element using the count index
        '''
        if the_list[i] != 0:
            the_list[count]= the_list[i] 
            count = count + 1 
    #move non zero numbers to the front
    while count < listlen: 
        the_list[count] = 0
        count = count + 1

the_list = [1, 0, 7, 2, 0, 3, 9, 0, 4]
listlen = len(the_list) #get the length to for range
sortnum(the_list,listlen)
print(the_list) #print out the updated list