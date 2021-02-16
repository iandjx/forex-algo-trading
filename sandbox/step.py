import subprocess
import sys

commits = [
    "5d15425",
    "a6d5645",
    "c04927d",
    "2f5246b",
    "8d4cbbe",
    "2c70220",
    "d725c31",
    "408ea8e",
    "da0f695",
    "cc53756",
    "e974c9f",
    "3666a44",
    "0b907b1",
    "7fdd9b3",
    "bc34920"
]

step = sys.argv[1]
subprocess.call(["git", "checkout", f"{step}"])
