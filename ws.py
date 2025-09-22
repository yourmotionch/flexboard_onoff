#!/usr/bin/env python3
# ws.py
#
# Copyright (c) 2025 Yourmotion.ch and Flexboard.ch
# All rights reserved.
#
# NOTICE:
# This script is proprietary and confidential.
# Any use, modification, reproduction, or distribution
# without prior written permission from Yourmotion.ch is strictly prohibited.
#
from flask import Flask, abort
import os
import signal
import sys

os.environ["DISPLAY"] = ':0'

app = Flask(__name__)

@app.route("/poweroff")
def poweroff():
    os.system("xset dpms force off")
    return "OK\n", 200, {"Content-Type": "text/plain; charset=utf-8"}

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    abort(404)

def handle_sigint(signum, frame):
    print("\nStopping server")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_sigint)
    app.run(host="0.0.0.0", port=8881, threaded=True)
