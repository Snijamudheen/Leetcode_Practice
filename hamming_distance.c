/*The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.*/

int hammingDistance(int x, int y)
{
    int d = 0, n = x ^ y;
  
    while(n)
    {
        n& = n - 1;
        d++;
    }
  
    return d;
}
