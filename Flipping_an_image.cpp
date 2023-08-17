/*Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0].*/

class Solution 
{
  public:
      // Helper function to reverse an array
      void reverseArr(int arr[], int n)
      {
          int start = 0;
          int end = n - 1;
        
          while(start < end)
          {
              swap(arr[start], arr[end]);
              start++;
              end--;
          }
      }
  
      // Main function to flip and invert the input image
      vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) 
      {
          int n = image.size(); // Get the number of rows in the image
          int arr[image.size()]; // Create an integer array 'arr' of the same size as the number of rows in the image
  
          for(int i = 0; i < n; i++)  // Iterate through each row of the image  
          { 
              for(int j = 0; j < n; j++) // Iterate through each element of the current row
              {  
                  // Invert the value of each element in the current row
                  if(image[i][j] == 1)
                      arr[j] = 0; // If the element is 1, set arr[j] to 0 (invert 1 to 0)
                  else
                      arr[j] = 1; // If the element is 0, set arr[j] to 1 (invert 0 to 1)
              }
  
              reverseArr(arr, n); // Reverse the 'arr' array using the helper function
  
              for(int j = 0; j < n; j++)
              {
                  image[i][j] = arr[j]; // Copy the reversed and inverted values back to the image row
              }
          }
  
          return image; // Return the modified image after flipping and inverting each row
      }
};
