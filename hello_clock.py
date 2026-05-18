#!/usr/bin/env python3
"""HelloClock – tiny CLI to display the current local time.

Run simply with:
    python hello_clock.py
"""
import datetime

def main() -> None:
    now = datetime.datetime.now()
    print(f"Current time: {now:%Y-%m-%d %H:%M:%S}")

if __name__ == "__main__":
    main()
