#!/usr/bin/env python3
# install_cron_relative.py
#
# Copyright (c) 2025 Yourmotion.ch and Flexboard.ch
# All rights reserved.
#
# NOTICE:
# This script is proprietary and confidential.
# Any use, modification, reproduction, or distribution
# without prior written permission from Yourmotion.ch is strictly prohibited.
#

import os, shutil, subprocess
from pathlib import Path

# Directory containing this script
APP = Path(__file__).resolve().parent
SCRIPT = APP / "ws.py"

if not SCRIPT.exists():
    raise SystemExit(f"❌ Missing: {SCRIPT}")

py = shutil.which("python3") or "/usr/bin/env python3"
cron_cmd = f"sh -c 'cd {APP}; sleep 10; {py} {SCRIPT.name} >> ws.log 2>&1'"
CRON_LINE = f"@reboot {cron_cmd}"

try:
    current = subprocess.check_output(["crontab", "-l"], text=True)
except subprocess.CalledProcessError:
    current = ""

if CRON_LINE not in current:
    new = (current.rstrip() + "\n" + CRON_LINE + "\n").lstrip()
    subprocess.run(["crontab", "-"], input=new, text=True, check=True)

print("Cron job installed:")
print(CRON_LINE)
print(f"Note: after reboot: tail -n 200 {APP}/ws.log")
