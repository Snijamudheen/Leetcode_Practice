/*A MATLAB program that opens and reads the logtable text file to display it to the user.

Log            Function

0.000000        -Inf
10.000000        2.302585
20.000000        2.995732
30.000000        3.401197
40.000000        3.688879
50.000000        3.912023
60.000000        4.094345
70.000000        4.248495
80.000000        4.382027
90.000000        4.499810
100.000000        4.605170

*/

x = 0:10:100;
y = [x;log(x)];

fid = fopen('logtable.txt','w');

fprintf(fid, 'Log            Function\n\n');
fprintf(fid, '%f        %f\n',y);

fclose(fid);
type logtable.txt


