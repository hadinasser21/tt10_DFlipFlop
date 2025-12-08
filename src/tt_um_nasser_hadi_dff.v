/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none
module tt_um_nasser_hadi_dff (
    input  wire [7:0] ui_in,    
    output wire [7:0] uo_out,   
    input  wire [7:0] uio_in,   
    output wire [7:0] uio_out,  
    output wire [7:0] uio_oe,   
    input  wire       ena,      
    input  wire       clk,      
    input  wire       rst_n     
);

    // D Flip-Flop Input and Output
    wire D = ui_in[0];
    reg  Q = 1'b0;   // initialized so sim never sees X

    // Sequential Logic
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            Q <= 1'b0;    // async active-low reset
        else
            Q <= D;       // capture D on rising edge
    end

    // Output Assignment
    assign uo_out[0] = Q;
    assign uo_out[7:1] = 8'b0;

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    // Prevent unused warnings
    wire _unused = &{ena, ui_in[7:1], uio_in, 1'b0};

endmodule


