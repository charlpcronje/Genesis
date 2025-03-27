# main.py

from emergent.engine import run_simulation

if __name__ == "__main__":
    logs = run_simulation()
    for log in logs:
        print(log)
