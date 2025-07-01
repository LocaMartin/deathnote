| Protocol       | Transport                   | Port / Pins       | Network Layer        | Language (Original/Typical) | Communication Type              | Default Credentials | Encryption / Encoding          | Raw Request Example                         | Raw Response Example                    |
| -------------- | --------------------------- | ----------------- | -------------------- | --------------------------- | ------------------------------- | ------------------- | ------------------------------ | ------------------------------------------- | --------------------------------------- |
| **I²C**        | Electrical Bus              | SDA/SCL (2 wires) | Data Link            | C / Assembly                | Binary (Register/Address-based) | None                | None                           | `[START][ADDR_W][REG][STOP]`                | `[START][ADDR_R][DATA][STOP]`           |
| **SPI**        | Electrical Bus              | MISO/MOSI/SCLK/SS | Data Link            | C / Assembly                | Binary                          | None                | None                           | `[SS LOW][CMD][DATA][SS HIGH]`              | `[SS LOW][RESP][SS HIGH]`               |
| **UART**       | Serial (TX/RX)              | TX/RX             | Physical / Data Link | C / Assembly                | Text / Binary                   | None                | None                           | `AT+CMD\r\n`                                | `OK\r\n` or `+RESP:DATA\r\n`            |
| **CAN**        | Differential Bus            | CAN\_H / CAN\_L   | Data Link / Network  | C / C++                     | Binary (Frame-based)            | None                | Optional (CAN-FD/ISO)          | `ID: 0x123, DATA: [01 02 03 04]`            | `ACK / Response Frame`                  |
| **Modbus RTU** | Serial (RS-485/RS-232)      | Varies            | Application          | C / Ladder Logic            | Binary (Frame)                  | None                | CRC16                          | `[0x01][0x03][0x00][0x00][0x00][0x02][CRC]` | `[0x01][0x03][0x04][DATA][CRC]`         |
| **Modbus TCP** | TCP/IP                      | 502               | Application          | C / Ladder Logic            | Binary (Modbus PDU)             | None                | CRC or TCP checksum            | `[MBAP][Function][Data]`                    | `[MBAP][Function][Response Data]`       |
| **JTAG**       | Electrical Pins             | TDI/TDO/TCK/TMS   | Physical             | Assembly / Debug Tools      | Binary                          | None                | None                           | `IRSCAN`, `DRSCAN`, `RESET` commands        | Target responds during shift operations |
| **USB**        | Differential                | D+ / D-           | Link / Transport     | C                           | Binary                          | None                | Optional (USB Secure Comm)     | `Setup Packet: bmRequestType, bRequest...`  | `Data Packet or ACK`                    |
| **PCIe**       | Serial (Differential Pairs) | Lanes x1 to x16   | Link / Transport     | C / HDL                     | Binary (TLP/DLLP)               | None                | Optional (IDE, TLP encryption) | `Memory Read TLP`                           | `Memory Read Completion TLP`            |
| **HDMI-CEC**   | Single Wire                 | Pin 13 (CEC)      | Application          | C                           | Text (hex opcodes)              | None                | None                           | `0x10 0x44 0x41` (Volume Up)                | `0x10 0x8C` (Feature Abort)             |

## 🛠️ How to Interact with Hardware Protocols

Hardware protocols depend on the specific protocol, the tools available, and the environment (e.g., embedded system, PC, dev board). Here's a protocol-wise breakdown of how to interact with each one listed in the table above:

---

### 🔌 I²C (Inter-Integrated Circuit)

- **Tools:** Microcontroller (e.g., Arduino, STM32), Raspberry Pi, Logic Analyzer  
- **Libraries:** `Wire.h` (Arduino), `smbus` / `i2c-tools` (Linux)  
- **How to interact:**
  - Linux: `i2cdetect`, `i2cget`, `i2cset`
  - Python: `smbus2` or `periphery.I2C()`

**Example (Linux):**
```bash
i2cget -y 1 0x3c 0x00
```

### 🔄 SPI (Serial Peripheral Interface)

- **Tools:** Microcontroller, Bus Pirate, Logic Analyzer  
- **Libraries:** `spidev` (Linux), `SPI.h` (Arduino)  
- **How to interact:**
  - Linux: `/dev/spidevX.Y` device
  - Python: `spidev` library

**Example (Python):**
```python
import spidev
spi = spidev.SpiDev()
spi.open(0, 0)
resp = spi.xfer2([0x01, 0x02])
```
### 🧵 UART (Serial)

- **Tools:** Serial-to-USB adapters (FTDI), any MCU with UART  
- **Libraries:** `pyserial`, Arduino `Serial`  
- **How to interact:**
  - Linux: `/dev/ttyUSB0`, `/dev/serial0`
  - Windows: `COM3`, `COM4`
  - Python: `pyserial`

**Example (Python):**
```python
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.write(b'AT\r\n')
print(ser.readline())
```

### 🚗 CAN (Controller Area Network)

- **Tools:** CAN transceivers (MCP2515), USB-CAN adapters (CANable, Kvaser)  
- **Libraries:** `python-can`, SocketCAN (Linux)  
- **How to interact:**
  - Linux: `can0` via SocketCAN

**Example (Python):**
```python
import can
bus = can.interface.Bus(channel='can0', bustype='socketcan')
msg = can.Message(arbitration_id=0x123, data=[0x01, 0x02], is_extended_id=False)
bus.send(msg)
```

### ⚡ Modbus RTU / TCP

- **Tools:** RS-485 USB dongle (RTU), Ethernet (TCP)  
- **Libraries:** `pymodbus`, `libmodbus`, PLCs  
- **How to interact:**
  - RTU: `/dev/ttyUSB0`
  - TCP: IP + port 502

**Example (Python TCP):**
```python
from pymodbus.client.sync import ModbusTcpClient
client = ModbusTcpClient('192.168.0.10')
rr = client.read_holding_registers(0x00, 2, unit=1)
print(rr.registers)
```

### 🧠 JTAG (Debug Interface)

- **Tools:** J-Link, OpenOCD, FTDI-based adapters  
- **Software:** OpenOCD, JTAGulator, UrJTAG  
- **How to interact:**
  - Define the target in OpenOCD configuration files

**Example (Bash):**
```bash
openocd -f interface/jlink.cfg -f target/stm32f1x.cfg
```

### 🔌 USB (Universal Serial Bus)

- **Tools:** USB sniffers (Wireshark with USB capture), USB analyzers  
- **Libraries:** `libusb`, `pyusb`, `WinUSB`  
- **How to interact:**
  - Use Python's `pyusb` to send control/read transfers

**Example (Python):**
```python
import usb.core
dev = usb.core.find(idVendor=0x1234, idProduct=0x5678)
dev.ctrl_transfer(0x80, 6, 0x100, 0, 64)
```

### 🚀 PCIe (Peripheral Component Interconnect Express)

- **Tools:** FPGA development boards, PCIe drivers, Root Complex/Endpoint  
- **Libraries/Utilities:** Linux tools (`lspci`, `setpci`), Windows `WinDriver`  
- **How to interact:**
  - Write a kernel-space or user-space PCIe driver
  - Use Linux PCI utilities to inspect or modify configuration space

**Example (Bash):**
```bash
lspci -vvv
setpci -s 00:1f.2 60.L
```
### 📺 HDMI-CEC (Consumer Electronics Control)

- **Tools:** HDMI-CEC adapters (Pulse-Eight), Raspberry Pi (built-in CEC support)  
- **Libraries:** `libcec`, `cec-utils`  
- **How to interact:**
  - Use `cec-client` on Linux to send/receive CEC messages

**Example (Bash):**
```bash
echo "tx 10 44 41" | cec-client -s
```
| Tool                             | Supports                      | Use Case                             |
| -------------------------------- | ----------------------------- | ------------------------------------ |
| **Bus Pirate**                   | UART, I²C, SPI                | Quick CLI-based interaction          |
| **Logic Analyzer (e.g. Saleae)** | Most protocols (for decoding) | Debugging signals                    |
| **Raspberry Pi**                 | I²C, SPI, UART, HDMI-CEC      | Embedded controller, protocol tester |
| **Arduino**                      | UART, I²C, SPI                | Prototyping embedded interaction     |
| **OpenOCD**                      | JTAG/SWD                      | Flashing, debugging MCUs             |
| **Sigrok (PulseView)**           | Multiple protocols            | Visual decoding of signal traces     |
