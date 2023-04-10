
Verilog code must have the following logic commands
And &
or |
not ~
xor ^
NAND ~&
XNOR ~^
NOR ~|

This is a file to describe the current constraints of the verilog visualization, the verilog file can only have up to 2 parenthesis as of the current iteration.

Example:
assign cout[1] = (~ a[3] & d[1]) | (~ a[3] & cout[0]); 

It is not able to handle more parenthesis so this will produce an error

Example:
assign cout[1] = (~ a[3] & d[1]) | (~ a[3] & cout[0]) | (f[3] & ~g);

To execute the file run this command:

python3 Thesis.py B mylib.genlib f2-aig.v 

