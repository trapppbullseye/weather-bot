#!/usr/bin/env python3
"""Discord bot that forecasts weather by city"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Discord bot that forecasts weather by city")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("weather-bot v0.1.0");return
 print(f"[12:01] weather-bot ready")
if __name__=="__main__":main()
