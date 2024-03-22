/*You are playing the following Nim Game with your friend:
Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.*/

class Solution 
{
  public:
      bool canWinNim(int n) 
      {
          return n % 4;
      }
      /* f(1)=f(2)=f(3)=1;
      f(n)=!(f(n-1) && f(n-2) && f(n-3));
      
      f(4)=!(1 && 1 && 1)=0;
      f(5)=!(0 && 1 && 1)=1=f(6)=f(7);
      f(8)=!(1 && 1 && 1)=0;
      */
};
