'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  # if the length of the arr is less than 2 return 0
    if len(word) <= 1:
        return 0
    #if the first two characters of the string are "th"
    if word[:2] == "th":
        # add one and call the function recursevely with the string without the first two characters
        return 1 + count_th(word[2:])
    else:
        # call the function recursevely with the string without the first character
        return 0 + count_th(word[1:])

# First-pass iterative solution
# def count_th(word):
#     count = 0
#     if len(word) == 0:
#         return 0
#     for i in range(0, len(word)-1):
#         if word[i] == "t" and word[i+1] == "h":
#             count+=1
#         else:
#             i+=1
#     return count
print(count_th("wthththththththteththethetehteh"))    