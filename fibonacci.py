import requests
import random

if __name__ == "__main__":
    for _ in range(1, int(1e10)):
        n = random.randint(1, 31)
        response = requests.get(f"http://localhost:5000/{n}")
        response.raise_for_status()
