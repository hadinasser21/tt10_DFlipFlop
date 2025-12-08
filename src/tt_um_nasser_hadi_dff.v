/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_nasser_hadi_dff(
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    wire din = ui_in[0];

    reg q;

    always @(posedge clk or negedge rst_n)
    begin
        if(!rst_n)
            q <= 1'b0;
        else
            q <= din;
    end

    // All output pins must be assigned. If not used, assign to 0.
    assign uo_out[0] = q;
    assign uo_out[1] = 1'b0;
    assign uo_out[2] = 1'b0; 
    assign uo_out[3] = 1'b0; 
    assign uo_out[4] = 1'b0; 
    assign uo_out[5] = 1'b0; 
    assign uo_out[6] = 1'b0; 
    assign uo_out[7] = 1'b0; 

    assign uio_out = 0;
    assign uio_oe  = 0;

    // List all unused inputs to prevent warnings
    wire _unused = &{ena, ui_in[7:1], uio_in, 1'b0};

endmodule 

