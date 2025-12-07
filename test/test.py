# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ClockCycles, Timer


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start D Flip-Flop Test")

    # Clock = 100 kHz
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # --------------------
    # RESET PHASE
    # --------------------
    dut._log.info("Reset Test")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    # Hold reset for a few clean edges
    await ClockCycles(dut.clk, 5)

    # Release reset cleanly *between* edges
    await RisingEdge(dut.clk)
    dut.rst_n.value = 1

    # Wait for reset to propagate
    await RisingEdge(dut.clk)

    # After reset, Q MUST be 0
    assert dut.uo_out.value.integer & 0x1 == 0, "Q not reset to 0!"

    # --------------------
    # TEST D = 1
    # --------------------
    dut._log.info("Test D = 1")

    await RisingEdge(dut.clk)      # align to clean edge boundary
    dut.ui_in.value = 1           # D = 1

    await RisingEdge(dut.clk)      # capture edge

    assert dut.uo_out.value.integer & 0x1 == 1, "Q did not follow D = 1!"

    # --------------------
    # TEST D = 0
    # --------------------
    dut._log.info("Test D = 0")

    await RisingEdge(dut.clk)
    dut.ui_in.value = 0           # D = 0

    await RisingEdge(dut.clk)

    assert dut.uo_out.value.integer & 0x1 == 0, "Q did not follow D = 0!"

    dut._log.info("D Flip-Flop Test PASSED ✅")
