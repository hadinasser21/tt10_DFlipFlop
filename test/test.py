# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start D Flip-Flop Test")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # --------------------
    # RESET TEST
    # --------------------
    dut._log.info("Reset Test")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    # Hold reset for a few cycles
    await ClockCycles(dut.clk, 5)

    # Release reset
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # After reset, Q must be 0
    assert dut.uo_out.value.integer & 0x1 == 0, "Q not reset to 0!"

    # --------------------
    # D = 1 → Q should become 1 on next clock
    # --------------------
    dut._log.info("Test D = 1")
    dut.ui_in.value = 1   # ui_in[0] = D = 1
    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value.integer & 0x1 == 1, "Q did not follow D = 1!"

    # --------------------
    # D = 0 → Q should become 0 on next clock
    # --------------------
    dut._log.info("Test D = 0")
    dut.ui_in.value = 0   # ui_in[0] = D = 0
    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value.integer & 0x1 == 0, "Q did not follow D = 0!"

    dut._log.info("D Flip-Flop Test PASSED ✅")
