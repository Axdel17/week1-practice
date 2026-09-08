import json
import subprocess

user = input("username: ").strip()
pw = input("password: ").strip()
body = json.dumps({"username": user, "password": pw})

p = subprocess.run(
    [
        "curl.exe",
        "-s",
        "-X",
        "POST",
        "http://127.0.0.1:8000/api/token/",
        "-H",
        "Content-Type: application/json",
        "-d",
        body,
    ],
    capture_output=True,
    text=True,
)
print(p.stdout)
if not p.stdout.strip():
    print(p.stderr)
    raise SystemExit("No token response. Is the server running?")

tokens = json.loads(p.stdout)
p2 = subprocess.run(
    [
        "curl.exe",
        "-s",
        "http://127.0.0.1:8000/api/me",
        "-H",
        "Authorization: Bearer " + tokens["access"],
    ],
    capture_output=True,
    text=True,
)
print(p2.stdout)
