# Triple-Sort
This Repository will contain the sorting algorithm for an array by selecting any three elements and perform circular right shift to get a sorted array.
You are given a permutation p1,p2,…,pN of the integers 1 through N. You may perform up to K

operations of the following type:

    Choose three pairwise distinct valid indices i1,i2,i3

. Note that these indices do not have to be chosen in increasing order.
Let's denote the values of pi1
, pi2 and pi3 before this operation by v1, v2 and v3
respectively.
Change pi2
to v1, pi3 to v2 and pi1 to v3. In other words, perform a cyclic right shift on the elements pi1,pi2,pi3

    in this order.

For example, the permutation (1,4,3,2,5)
can be changed to the permutation (1,5,3,4,2) in one operation by choosing i1=2, i2=4 and i3=5

.

Your task is to sort the permutation in increasing order. Note that you do not have to minimise the number of performed operations.
