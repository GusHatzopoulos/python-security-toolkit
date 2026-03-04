"""
Log Reader Module
Simple tool for reading and analyzing security logs.
Part of the Python Security Toolkit.
"""

from pathlib import Path

def read_log_file(file_path):
    """Read a log file and print its contents."""

    log_file = Path(file_path)

    if not log_file.exists():
        print("Log file not found.")
        return

    print(f"\nReading log file: {log_file}\n")

    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            print(line.strip())


if __name__ == "__main__":
    # Example usage
    read_log_file("example.log")