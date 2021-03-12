#!/usr/bin/env python

import math

cpu_clock = input("Master Clock Frequency (MHz) : ")
baud_rate = input("Baud rate : ")

uart_div = int(math.ceil((cpu_clock * 1000000.0) / baud_rate))

print("UART_DIV = " + str(uart_div))

uart_div30 = uart_div & 0x000F
uart_div1512 = uart_div & 0xF000

uart_div1114 = uart_div & 0x0FF0

brr1 = uart_div1114 >> 4
brr2 = uart_div30 | (uart_div1512 >> 8)

print("")
print("BRR1 = " + str(brr1) + " = " + hex(brr1))
print("BRR2 = " + str(brr2) + " = " + hex(brr2))
exit()
