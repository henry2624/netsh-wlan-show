"""Netsh WLAN Show — Show the current WLAN interface, SSID, and signal without dumping profiles or keys."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='netsh_wlan_show',
        description='Show the current WLAN interface, SSID, and signal without dumping profiles or keys.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Netsh WLAN Show')
    print('Which Wi-Fi you are on, nothing else.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
