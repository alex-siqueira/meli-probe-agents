import os
import platform
import requests
import socket

localIP = socket.gethostbyname(socket.gethostname())

processor = platform.processor()
osname = os.uname().sysname
version = os.popen('lsb_release -r -s').read()
sessions = os.popen('who -s').read()
processes = os.popen('ps -e').read()

payload = {
  "localIP": localIP,
  "processor": processor,
  "osname": osname,
  "version": version,
  "sessions": sessions.splitlines(),
  "processes": processes.splitlines()
}

requests.post(url="http://127.0.0.1:5000/", json=payload)
