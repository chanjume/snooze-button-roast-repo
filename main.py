#!/usr/bin/env python3
"""Snooze Button Roast: write one roast line to /output/entry.txt.

Craft: one concrete time (6 AM on Saturday), one named thing (the smoke
detector), one quoted grievance — the alarm behaves like a smoke
detector with a grudge, and there is no fire, no smoke, only the
weekend going up in flames. The roast is the alarm's, in its own voice,
landing in one breath with no setup that needs explaining.
"""
import os

ENTRY = 'My alarm clock rang at 6 AM on Saturday like a smoke detector with a grudge — no fire, no smoke, just my weekend going up in flames.'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
