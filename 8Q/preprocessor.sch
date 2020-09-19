EESchema Schematic File Version 4
LIBS:8Q-cache
EELAYER 26 0
EELAYER END
$Descr A1 33110 23386
encoding utf-8
Sheet 6 13
Title "8Q Quantum Computer"
Date "2020-06-29"
Rev ""
Comp "Spooky Manufacturing, LLC"
Comment1 "(c) 2020"
Comment2 ""
Comment3 ""
Comment4 "Development Schematics"
$EndDescr
$Comp
L Interface:S5933_PQ160 U178
U 1 1 5F32A775
P 5050 6350
F 0 "U178" H 5050 10928 50  0000 C CNN
F 1 "S5933_PQ160" H 5050 10837 50  0000 C CNN
F 2 "Package_QFP:PQFP-160_28x28mm_P0.65mm" H 5050 1850 50  0001 C CNN
F 3 "http://datasheet.datasheetarchive.com/originals/distributors/Datasheets-35/DSA-684194.pdf" H 5050 6350 50  0001 C CNN
	1    5050 6350
	1    0    0    -1  
$EndComp
$Comp
L Memory_RAM:IS42S16400J-xC U177
U 1 1 5F32A907
P 12000 3950
F 0 "U177" H 12000 5528 50  0000 C CNN
F 1 "IS42S16400J-xC" H 12000 5437 50  0000 C CNN
F 2 "Package_SO:TSOP-II-54_10.16x22.22mm_P0.8mm" H 12000 3950 50  0001 C CNN
F 3 "http://www.issi.com/WW/pdf/42-45S16400J.pdf" H 11400 5200 50  0001 C CNN
	1    12000 3950
	1    0    0    -1  
$EndComp
$Comp
L MCU_ST_STM32F4:STM32F429BITx U179
U 1 1 5F32AB85
P 17250 8450
F 0 "U179" H 17200 3064 50  0000 C CNN
F 1 "STM32F429BITx" H 17200 2973 50  0000 C CNN
F 2 "Package_QFP:LQFP-208_28x28mm_P0.5mm" H 15950 3350 50  0001 R CNN
F 3 "http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00071990.pdf" H 17250 8450 50  0001 C CNN
	1    17250 8450
	1    0    0    -1  
$EndComp
$EndSCHEMATC
