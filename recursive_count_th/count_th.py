'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
      # Find Base Case
    if len(word) < 2:
        return 0
    
    # starting at 0 and counting by 2 for a 'th' match - if it matches then add 1 recursive
    if(word[0:2] == 'th'): 
        return 1 + count_th(word[1:])

    return count_th(word[1:])
    

print(count_th("the only thing to test Tyrannossaurus Rex that is a long word for ht or th"))
