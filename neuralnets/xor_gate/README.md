![photo](drawing.jpg?raw=true "Title")


A genetic algorithm that finds a valid combination of weights and thresholds
for an Artificial Neural Network.


----------------------------------------------------------------


in: x = 1 or 0, y = 1 or 0

out: x xor y


----------------------------------------------------------------

Encoding:

I used what is called "Value Encoding". Which means

that I used real world values as the allels in the chromosomes.

Each chromosome is an array of 19 values ranging from -255 to 255.

chromosome[0 ... 12] are the weights and chromosome[12 ... 18] are the thresholds.

----------------------------------------------------------------
Number of generations it took to find a solution given 10 trials:

(population size = 50)

1. 1
2. 8
3. 74
4. 1
5. 48
6. 24
7. 141
8. 163
9. 52
10. 1

Average: 57
