# Notes

**Week 1 · Environment, Git, Docker, Python**

**4 Sep 2026** · Week 1 check-in

**Attendee:** Adetokunbo Teriba

---

## Status at a glance

| Area | Result | Evidence |
|---|---|---|
| Git checkpoint | Done | PR merged to main |
| Python refresher | Done | venv + module ran successfully |
| Docker | Blocked | Desktop will not start on this laptop |

---

## Notes

- **Environment**
  - Installed and verified on my HP 650 (Windows 10 Pro N 22H2): Git 2.55.0, VS Code, Python 3.14.7, Node.js 24.20.0 LTS, and Docker Desktop 29.7.2 (CLI present).
  - Git identity configured (name and email). First GitHub push authenticated with Git Credential Manager.

- **Git checkpoint — done**
  - Cloned a practice repo, created branch `my-first-change`, made a trivial change, committed, pushed, opened a pull request, and merged to main.
  - Pull request: https://github.com/Axdel17/week1-practice/pull/1

- **Python refresher — done**
  - Created a project virtual environment and confirmed pip (26.2.1).
  - Wrote a module (`greet.py` with functions) and ran it from `main.py`. Output: “Hello, Adetokunbo. Week 1 Python is working.” and “2 + 3 = 5”.

- **Docker — blocked, needs help**
  - Docker Desktop installs but does not start. Error: “Virtualization support not detected.”
  - Task Manager shows Virtualisation: Enabled (Intel i3-2328M).
  - Windows Subsystem for Linux, Virtual Machine Platform, and Hyper-V do not appear in Windows Features.
  - `wsl --install` returns `0x800f080c`. DISM / Get-WindowsOptionalFeature returns `0x800f081f` (source files missing).
  - Windows is not activated (watermark). Hardware: HP 650, 8GB RAM, HDD.
  - Could not run `docker compose up` on this machine.

- **Ask / next**
  - Guidance on Docker: activate or repair this Windows install, use another machine, or skip Docker until a supported laptop is available.
  - Ready to start Week 2 once that is decided. Team project repository links are still needed if the real checkpoint should be on the product repos rather than the practice repo.

---

Prepared by Adetokunbo Teriba · 4 September 2026
