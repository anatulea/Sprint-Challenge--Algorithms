#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) The loop is going to run n times. To get the value a to be equal to n and exit the while loop the computation needs to happen n times. So as n increases the runtime increases linearly


b)O(n^2) The outer for loop has a runtime of O(n), it loops as many times as the n value. The internal while loop has an O(n/2) runtime, it loops inside and doubles it's value with every iteration and breaks out only when the j value is bigger than the n value. With small input numbers, it runs pretty fast but as the input n increases the runtime slows significantly. The proper Big O = O(n)* O(1/2*n), but because we drop the constants and consider worst case scenario the right answer is: O(n^2)


c) O(n) The function is going to loop and add 2 to the number of bunnies with every iteration. It is going to loop the as many times as the # of bunnies, in other words, it's going to have a linear runtime.

## Exercise II
Input: 
n - number of floors
e - number of eggs

Output:
f - the first floor at which the eggs are going to break

So form the floor f to the len(n)-1 the eggs will brake. 
Need to use the minimum amount of eggs. 

Will start at the first floor and drop an egg, 
    if the egg doesn't break I move to the next, 
    else will return the floor number I am at.

This will have a run time of O(n) and will break just one egg but it is not the fastest.
We already know that the number of floors is ordered. So for a faster solution will use a binary search tree and start throwing eggs from the middle of the building. That will cost us more broken eggs.



