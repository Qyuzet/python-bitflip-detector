import hashlib
import os
import threading
import time
import sys

def run_periodically(interval, func, *args):
    while True:
        time.sleep(interval)
        func(*args)

def calculate_hash(file_path):
   
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def detect_bit_flip(file_path, original_hash):
    
    current_hash = calculate_hash(file_path)
    
   
    if original_hash == current_hash:
        print("NO | ", end='')
        print(f"Hash: {original_hash} | {current_hash}")
    
    else:
        print("YES |", end='')
        print(f"Hash: {original_hash} | {current_hash}")
        sys.exit()
   

def main():
  
    file_path = 'test_data.bin'
    
    if not os.path.exists(file_path):
    
        with open(file_path, 'wb') as f:
            f.write(os.urandom(1024))  # 1 KB of random data
    

    original_hash = calculate_hash(file_path)
    

    thread = threading.Thread(target=run_periodically, args=(0.01, detect_bit_flip, file_path, original_hash))
    thread.daemon = True 
    thread.start()

    
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
