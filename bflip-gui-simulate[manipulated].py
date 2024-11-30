import hashlib
import os
import random
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BitFlipDetector:
    def __init__(self, file_path):
        self.file_path = file_path
        self.original_hash = self.calculate_hash()
        self.current_hash = self.original_hash
        self.bar_data = [0] * len(self.original_hash)  # no flips

       
        self.root = tk.Tk()
        self.root.title("Bit Flip Detector")

        # hash compare
        hash_frame = tk.Frame(self.root)
        hash_frame.pack(side=tk.TOP, pady=10)

        self.prev_label = tk.Label(hash_frame, text=f"Previous Hash:\n{self.original_hash}", bg="lightblue", width=80, height=5)
        self.prev_label.grid(row=0, column=0, padx=5)

        self.current_label = tk.Label(hash_frame, text=f"Current Hash:\n{self.current_hash}", bg="lightgreen", width=80, height=5)
        self.current_label.grid(row=0, column=1, padx=5)

    
        self.fig = Figure(figsize=(8, 4))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title('Bit Flip Visualization')
        self.ax.set_xlabel('Hash Index')
        self.ax.set_ylabel('Flip Detected (1=Yes, 0=No)')
        self.ax.set_ylim(0, 1.2)  # Y-axis range for binary values
        self.bar_plot = self.ax.bar(range(len(self.bar_data)), self.bar_data, color='blue')
        self.canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # loop detect
        self.root.after(100, self.simulate_bit_flip)  
        self.root.mainloop()

    def calculate_hash(self):
        """Calculate SHA-256 hash of a file."""
        sha256 = hashlib.sha256()
        with open(self.file_path, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()

    def simulate_bit_flip(self):
        """Simulate a bit flip in the file and detect changes."""
        self.introduce_bit_flip()  # manipualate

        self.current_hash = self.calculate_hash()
        self.bar_data = [1 if c1 != c2 else 0 for c1, c2 in zip(self.original_hash, self.current_hash)]

        # Update
        self.prev_label.config(text=f"Previous Hash:\n{self.original_hash}")
        self.current_label.config(text=f"Current Hash:\n{self.current_hash}")

       
        for bar, height in zip(self.bar_plot, self.bar_data):
            bar.set_height(height)

        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()  # Redraw

      
        self.root.after(100, self.simulate_bit_flip)

    def introduce_bit_flip(self):
        """Simulate a bit flip by modifying a random byte in the file."""
        with open(self.file_path, 'r+b') as f:
            file_size = os.path.getsize(self.file_path)
            flip_position = random.randint(0, file_size - 1)
            f.seek(flip_position)
            original_byte = f.read(1)
            flipped_byte = bytes([original_byte[0] ^ 0xFF])  # Flip bits in byte
            f.seek(flip_position)
            f.write(flipped_byte)
            print(f"Simulated bit flip at position {flip_position}.")

def main():
  
    if not os.path.exists('test_data.bin'):
        with open('test_data.bin', 'wb') as f:
            f.write(os.urandom(1024))  # Generate 1 KB random dt

    detector = BitFlipDetector('test_data.bin')

if __name__ == "__main__":
    main()
