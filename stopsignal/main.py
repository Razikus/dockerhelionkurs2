import signal
import time

def handler(sig, frame):
    print("SIGNALNUMBER:", sig)

signals = set(signal.Signals) - {signal.SIGKILL, signal.SIGSTOP}
for sig in signals:
    signal.signal(sig, handler)

while True:
    print("...")
    time.sleep(1)
