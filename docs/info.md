<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

A D Flip-Flop is a sequential logic circuit that stores one bit of data. The output follows the input only on the rising edge of the clock and holds its value until the next clock edge or until reset is asserted.

We start by declaring the module. module, a basic building design unit in Verilog HDL, is a keyword to declare the module’s name. tt_um_nasser_hadi_dff is the identifier. Identifiers are the name of the module. The module command instructs the compiler to create a block containing certain inputs and outputs. The list in parenthesis is known as the port list, it contains the input and output ports. Then we declare other datatypes required in our design as follows.

reg Q;  
The reg type in Verilog is used to store the output value of the flip-flop. It holds the previous value until a clock edge updates it.

always @(posedge clk or negedge rst_n)  
This statement defines the sequential behavior. On the rising edge of the clock, the value of input D is stored in Q. If the reset signal rst_n is low, Q is cleared to 0. This allows the output to start from a known state.

assign uo_out[0] = Q;  
The stored value Q is then sent to the output pin. All other outputs are forced to 0.

endmodule terminates the module.

## How to test

Apply different values to input D and toggle the clock. On every rising edge of the clock, the output Q should follow the value of D. When rst_n is driven low, Q should reset to 0 regardless of the clock.

## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any.  
NONE
