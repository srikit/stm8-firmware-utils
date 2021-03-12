#!/usr/bin/env python

import math

cpu_clock = input("Master Clock Frequency (MHz) : ")
timer_prescaler = input("Prescaler [PSCR] : ")

cpu_clock = cpu_clock * 1000 * 1000

prescaler = pow(2, timer_prescaler)
tick_freq = cpu_clock / prescaler

print("")
print("Prescaler = " + str(prescaler))
print("Tick Frequency = " + str(tick_freq) + "Hz")
print("               = " + str(tick_freq / 1000) + "kHz")
print("               = " + str(tick_freq / 1000000) + "MHz")

print("")
time_ms = input("Time (mili-seconds) : ")
div_rate = 1000 / time_ms

counter_val = tick_freq / div_rate
auto_run_reg = int(math.ceil(counter_val))

if counter_val < 0:
	print("Value out of range ! [" + str(counter_val) + "]")
	exit()
	
if auto_run_reg > 0xFFFF:
	print("Value out of range ! [" + str(auto_run_reg) + "]")
	exit()

print("")
print("Counter Value [ARR] = " + str(auto_run_reg))

reg_arrh = (auto_run_reg >> 8) & 0xFF
reg_arrl = auto_run_reg & 0xFF

print("ARRH = " + str(reg_arrh) + " = " + hex(reg_arrh))
print("ARRL = " + str(reg_arrl) + " = " + hex(reg_arrl))
exit()
