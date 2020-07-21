#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0 #Time O(1) while (a < n * n * n): #Time O(n^3) a = a + n * n #Time O(1)

The running time is O(n).
(n * n * n) is O(n^3). However, We add to the (a) iterator (n * n) in the While loop. If we divide n^3 from n^2 we get O(n). (While a < n) is the only condition.


b) sum = 0 #Time O(1) for i in range(n): #Time O(n) j = 1 #Time O(1) while j < n: #Time O(log n) j *= 2 #Time O(1) sum += 1 #Time O(1)

The running time is O(n log n) - Logarithmic

The While loop runs less than half the times of n. Making it O(log n). However, we need to calculate that the loop is running (n) times

j quickly stops the loop with (j *= 2) thus making it logarithmic in time. With the loop running (n) times, we multiply O(log n) times O(n).


c) def bunnyEars(bunnies): if bunnies == 0: return 0

The running time is O(n).

This function is recursive. It calls itself (n) times and using bunnies as a counter that starts at (n) and then subtracts the recursive call to 0.

It's like a for loop iterating backwards by -1 to get to the base case 0.


## Exercise II

USE A BINARY SEARCH TREE This has a running time at O(log n) - Logarithmic The better approach is to use a binary search tree where the target is when the egg breaks.

pseudocode:

make a low and high variable for the first and last floors make a loop like... (WHILE low_var <= high_var>) guess a middle floor of the x-story building see if egg breaks at guessed floor if does - return the floor number if not...guess another middle floor to the right of the current spot

