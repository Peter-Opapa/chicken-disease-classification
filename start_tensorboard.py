#!/usr/bin/env python3
"""
Simple script to start TensorBoard
"""
import subprocess
import sys
import os

def start_tensorboard():
    log_dir = "artifacts/prepare_callbacks/tensorboard_log_dir"
    
    if not os.path.exists(log_dir):
        print(f"Error: Log directory {log_dir} does not exist!")
        return
    
    print(f"Starting TensorBoard...")
    print(f"Log directory: {log_dir}")
    print(f"TensorBoard will be available at: http://localhost:6006")
    
    try:
        # Start TensorBoard
        cmd = [sys.executable, "-m", "tensorboard.main", f"--logdir={log_dir}", "--port=6006"]
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\nTensorBoard stopped.")
    except Exception as e:
        print(f"Error starting TensorBoard: {e}")

if __name__ == "__main__":
    start_tensorboard()
