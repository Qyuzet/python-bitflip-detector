# python-bitflip-detector

A Python-based project for detecting and simulating bit-flip scenarios in binary data, with automation and GUI-based tools for enhanced analysis. This repository offers tools to handle and simulate potential bit-flip occurrences in data systems, useful for reliability testing and educational purposes.

![kWvifopqyBAqgWEup5TzQ5](https://github.com/user-attachments/assets/89563b58-277d-4981-9bc7-63442ff7d6fd)

<div align="center">
  <table>
    <tr>
      <td><img src="https://github.com/user-attachments/assets/d32a8185-5509-4b43-aacf-a6f14e402926" alt="Image 1" style="width:550;"/></td>
      <td><img src="https://github.com/user-attachments/assets/c0e89862-2cc4-4fe1-add8-4cb2e2a5be87" alt="Image 2" style="width:300px;"/></td>
    </tr>
  </table>
</div>


## Features
- **Automatic Termination**: Detect and handle bit-flip scenarios using automation (`bflip-auto-terminate.py`).
- **GUI Simulation**: A graphical user interface for simulating and visualizing bit-flips (`bflip-gui-simulate[manipulated].py`).
- **Binary Test Data**: Pre-included `test_data.bin` for experimentation.


<div align="center">
  <table>
    <tr>
      <td><img src="https://github.com/user-attachments/assets/ede929a8-450d-4c8c-8acf-eeff9d2a1db7" alt="Image 1" style="width:250px;"/></td>
      <td><img src="https://github.com/user-attachments/assets/8bf8f951-ae3b-44d6-9680-8e9923716b60" alt="Image 2" style="width:550px;"/></td>
    </tr>
  </table>
</div>

<div align="center">
  <table>
    <tr>
      <td>The left side is a real-time detector, but it is hard to detect since my CPU runs in a stable environment, bit flip is a rare condition in a stable environment since it happens more likely due to cosmic rays or noise radiation from radioactivity on the ground, to make it more probable, we need to heat the CPU or even make it overclock, so the electrons particle runs faster and vulnerable to interference</td>
      <td>Because it is hard to simulate, I built the right-side version to manipulate the bit randomly to showcase how it looks, but it is not an actual condition, since we are using SHA-256, where the flip just makes the entire structure changes, so to analyze it deeply, we need other algorithms to detect each chunks of memory. Here 1 represents 1 flip, and 0 means no, or we can see that a bar represents 1, and nothing represents 0</td>
    </tr>
  </table>
</div>


## Getting Started

### Prerequisites
- Python 3.8 or above.
- Recommended: A virtual environment for dependency management.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Qyuzet/python-bitflip-detector.git
   cd python-bitflip-detector
   ```

2. Set up the virtual environment (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### File Descriptions
- **`bflip-auto-terminate.py`**: A script for automatic detection and handling of bit-flip errors.
- **`bflip-gui-simulate[manipulated].py`**: A GUI application to simulate and analyze bit-flip errors in a controlled environment.
- **`test_data.bin`**: Binary data used for testing and simulations.

### Usage
1. **Run the GUI Simulation**:
   ```bash
   python bflip-gui-simulate[manipulated].py
   ```
   Follow on-screen instructions to simulate bit-flips on binary data.

2. **Use the Auto-Terminate Script**:
   ```bash
   python bflip-auto-terminate.py
   ```
   This script automatically processes the `test_data.bin` file to detect and log bit-flip events.

## Contributing
Feel free to submit issues or pull requests to improve the project. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

**Author**: [Qyuzet](https://github.com/Qyuzet)
