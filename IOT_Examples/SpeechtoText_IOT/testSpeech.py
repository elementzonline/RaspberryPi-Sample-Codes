import subprocess

myProcess = subprocess.Popen(['espeak', 'hi there'])
myProcess.wait()
myProcess = subprocess.Popen(['espeak', 'how is your day'])
myProcess.wait()