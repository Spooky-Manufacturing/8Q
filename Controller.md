# Controller

Sitting between the Bridge and the QCore, the Controller's role is to control the QCore circuitry by sending signals to fire photons, redirect qubits from registers to logic gates, etc.

## Digital Registers

The Controller has both digital and quantum registers, digital registers may be read directly, however quantum registers first require that a measurement operation be performed.

### FLAGS Register

The FLAGS Register (or Status Register, if you prefer) , is the status register that holds the current state of the processor.

| Bit # | Mask | Abbreviation | Description | Category | =1        | =0           |
| ----- | ---- | ------------ | ----------- | -------- | --------- | ------------ |
| 0     | 0x01 | CF           | Carry Flag  | Status   | CY(Carry) | NC(No-Carry) |
| 1     | 0x02 | ZF           | Zero Flag   | Status   | ZR(Zero)  | NZ(Not Zero) |
| 2     | 0x04 | SF           | Sign Flag   | Status   |           |              |
| 3     | 0x08 |              |             |          |           |              |
| 4     | 0x10 |              |             |          |           |              |
| 5     | 0x20 |              |             |          |           |              |
| 6     | 0x40 |              |             |          |           |              |
| 7     | 0x80 |              |             |          |           |              |

### Control Register

The Control Register has various control flags which modify the basic operation of the processor.

| Bit # | Mask | Abbreviation | Description | Category | =1   | =0   |
| ----- | ---- | ------------ | ----------- | -------- | ---- | ---- |
|       |      |              |             |          |      |      |
|       |      |              |             |          |      |      |
|       |      |              |             |          |      |      |
|       |      |              |             |          |      |      |
|       |      |              |             |          |      |      |
|       |      |              |             |          |      |      |
|       |      |              |             |          |      |      |



### Instruction Registers

s

## Quantum Register

