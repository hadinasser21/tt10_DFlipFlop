# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start D Flip-Flop Test")

    # ----------------------------
    # Set control signals FIRST
    # ----------------------------
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0  # start in reset

    # Start clock
    clock = Clock(dut.clk, 10, units="us")  # 100 kHz
    cocotb.start_soon(clock.start())

    dut._log.info("Holding Reset")
    await ClockCycles(dut.clk, 5)

    dut._log.info("Releasing Reset")
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # Check reset behavior
    q0 = dut.uo_out.value.integer & 0x1
    dut._log.info(f"After reset: Q={q0}")
    assert q0 == 0, "Q not reset to 0!"

    # ----------------------------
    # Test D = 1
    # ----------------------------
    dut._log.info("Test D = 1")
    dut.ui_in.value = 1  # D=1 on bit 0

    await ClockCycles(dut.clk, 1)  # one rising edge

    q1 = dut.uo_out.value.integer & 0x1
    dut._log.info(f"After D=1 and 1 clock: Q={q1}")
    assert q1 == 1, "Q did not follow D = 1!"

    # ----------------------------
    # Test D = 0
    # ----------------------------
    dut._log.info("Test D = 0")
    dut.ui_in.value = 0  # D=0

    await ClockCycles(dut.clk, 1)

    q2 = dut.uo_out.value.integer & 0x1
    dut._log.info(f"After D=0 and 1 clock: Q={q2}")
    assert q2 == 0, "Q did not follow D = 0!"

    dut._log.info("D Flip-Flop Test PASSED ✅")
