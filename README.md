# Genetic-Algo-in-PubG
A code that uses Genetic Algorithm to find the best possible combinations of Guns that You can carry

This is a basic code that uses basic Genetic Algorithm to find the best possible combination of Guns that you can carry
The data set is taken from https://docs.google.com/spreadsheets/d/1giKwsWYH9CcMXsvZnIkJKfBsr7jrX21Bu0-CwN-QKIM/edit#gid=0
If you want to add more then change the initial lists. All the list size must be same. The code will automatically adjust for the size

# How to run
You should have numpy installed
```
 python3 GeneticAlgoPubG.py
```
Enter the weightage you want to give to Damage per shot. If you are low on you aim,then you should give less weightage to it as the remaining % of weightage goes to Fire Rate(per minute). The no is bet 0 and 1
At last enter the no of iterations. The program will take care if you give unnecessarily too much

# For technical people
Here the phenotype are the guns where the genotype is the index of their name in the GunNames array
25 samples are taken and first crossed over . The maximum is left intact and others are divided randomly into two halves. The first element from the first half and second element from the second half and 12 such samples are made.
Now the worst 12 ones are removed . This the best 13 ones are preserved.
Then random mutation is done . If the best one is lost then that entire iteration is ignored.
If for last 10 iteration , there is no improvement in score then program is terminated

# Sample Output

