import subprocess
import sys

commits = [
    "asdasd",
    "asdasdasd"
]

step = sys.argv[1]
subprocess.call(["git", "checkout", f"{step}"])
