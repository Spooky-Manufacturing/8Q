EESchema Schematic File Version 4
LIBS:8Q-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 13
Title "8Q Quantum Computer"
Date "2020-06-29"
Rev ""
Comp "Spooky Manufacturing, LLC"
Comment1 "(c) 2020"
Comment2 ""
Comment3 ""
Comment4 "Development Schematics"
$EndDescr
$Sheet
S 11700 0    2300 2650
U 5EFAA347
F0 "cpu" 50
F1 "cpu.sch" 50
$EndSheet
$Sheet
S 11700 3200 2350 2100
U 5EFAA353
F0 "qpu" 50
F1 "qpu.sch" 50
$EndSheet
$Sheet
S -2800 800  2800 2050
U 5EFAA39F
F0 "power" 50
F1 "power.sch" 50
$EndSheet
Text Notes 750  5050 0    197  ~ 0
This is a rather large project which integrates a macro-scale\nquantum processor with a standard computer processor and\nperipherals, as such the schematic is broken up into several pieces:\n\nMain:\n  This page\n  CPU:\n     Digital CPU board schematic\n  Power:\n     Mains power shematic\n  QPU:\n    Quantum Processing Unit Shematic
Wire Notes Line
	1800 3450 11550 3450
Wire Notes Line
	11550 3450 11550 1250
Wire Notes Line
	11550 1250 12400 1250
Wire Notes Line
	12400 1250 12400 1200
Wire Notes Line
	9000 4250 9000 4650
Wire Notes Line
	9000 4650 1800 4650
Wire Notes Line
	9000 4250 12350 4250
Wire Notes Line
	1050 4050 -1500 4050
Wire Notes Line
	-1500 4050 -1500 2700
$EndSCHEMATC
