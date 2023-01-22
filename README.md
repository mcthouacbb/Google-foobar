# Google-foobar
Google foobar solutions

Problem 1(level 1): Decipher string by converting all lowercase letters to "opposite" (i.e. 'a' => 'z', 'b' => 'y', 'c' => 'x' ... 'x' => 'c', 'y' => 'b', 'z' => 'a')

Problem 2(level 2): A perfect binary tree of height h is assigned node indices in post-traversal order. Given an array of node indices, return an array where each corresponding entry in the result is equal to the index of the parent node in the argument.

EX:                 15
              7            14
           3     6      10    13
          1 2   4 5    8  9  11 12

Problem 3(level 2): Given 2 chess positions, find the minimum number of moves by a knight needed to go from 1 position to the other

Problem 4(level 3): Given a matrix representing the probabilities of transitioning from each state to the next, where a row of 0s represents a terminal states, find the exact probability of reaching any terminal state when starting from the first state

Problem 5(level 3): Given an array of positive integers, l, find the number of tuples (l[i], l[j], l[k]) where i < j < k such that l[k] is divisible by l[j] and l[j] is divisible by l[i]

Problem 6(level 3): there are 2 types of bombs, Mach and facula. You start with 1 of each type of bomb. At each "step", you can either
Have every Mach bomb retrieve a sync unit from a Facula bomb, for every Mach bomb there a new Facula bomb is added
Have every Fach bomb spontaenously create a Mach bomb
Given 2 targets, x and y, determine the fewest number of steps needed to have x Mach bombs and y Facula bombs if you start with 1 of each, or "impossible" if it is not possible

Problem 7: You need to distract a bunch of bunny trainers. You invite them to play the banana games. You will set up simultaneous thumb wrestling matches. In each match, the 2 bunny trainers will be in a thumb wrestling match. The trainer with fewer bananas will bet all their bananas, and the other trainer will match that bet. However, the trainer with more banans is always overconfident and losese.
EX: trainer 1: 10 bananas, trainer 2: 15 bananas
EX: trainer 2 loses 10 bananas, trainer 1 gains 10 bananas
EX: trainer 1: 20 bananas, trainer 2: 5 bananas
The trainers keep playing until they have the same amount of bananas. Some combinations of bananas, e.g. 3, 5, will result in the trainers eventually quitting and going back to training bunnies. Other combinations, such as 1, 4, will result in the trainers playing forever
Your goal is to maximize the number of trainers that are stuck in an infinite loop.
Given an array of size n where the ith entry indicates that bunny trainer i has array[i] bananas, find the most trainers that will not be stuck in an infinite loop (This is equivalent to finding n - (the maximum number of trainers stuck in an infinite loop))
The number of trainers is between 1 and 100, and the number of bananas for each trainer is between 1 and (2^30 - 1).
