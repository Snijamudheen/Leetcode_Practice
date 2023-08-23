/*Suppose we have a class:
public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). 
Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().
Note:
We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format 
you see is mainly to ensure our tests' comprehensiveness.*/

class Foo 
{
    promise<void> p1,p2;
  public:
      Foo() 
      { 
      }
  
      void first(function<void()> printFirst) 
      {
          
          // printFirst() outputs "first". Do not change or remove this line.
          printFirst();
          p1.set_value();
      }
  
      void second(function<void()> printSecond) 
      {
          
          // printSecond() outputs "second". Do not change or remove this line.
          p1.get_future().wait();
          printSecond();
          p2.set_value();
      }
  
      void third(function<void()> printThird) 
      {
          // printThird() outputs "third". Do not change or remove this line.
          p2.get_future().wait();
          printThird();
      }
};
