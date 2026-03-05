# HashCatnip.py

import argparse
import pyfiglet
import subprocess
import tempfile
import os
import sys
import shutil

def display_banner():
    """
    Display ASCII banner.
    """
    banner = pyfiglet.figlet_format("Hash Catnip")
    print(banner)


def get_user_input():
    """
    Get input from the user.
    """
    parser = argparse.ArgumentParser(
        description="Hash Catnip 2.0 - Hashcat Automation Utility"
    )

    parser.add_argument(
        "-H", "--hashes",
        required=True,
        help="Comma-separated hashes to crack"
    )

    parser.add_argument(
        "-l", "--wordlist",
        required=True,
        help="Path to wordlist"
    )

    parser.add_argument(
        "-m", "--mode",
        required=True,
        type=int,
        help="Hashcat hash mode (e.g., 0 for MD5)"
    )

    parser.add_argument(
        "-a", "--attack-mode",
        type=int,
        default=0,
        help="Hashcat attack mode (default: 0 - straight)"
    )

    parser.add_argument(
        "-o", "--output",
        help="Optional output file to store cracked hashes"
    )

    parser.add_argument(
        "--rules",
        help="Optional rule file"
    )

    parser.add_argument(
        "--session",
        help="Optional hashcat session name"
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress banner"
    )

    return parser.parse_args()


def validate_environment(wordlist_path):
    if not os.path.isfile(wordlist_path):
        print("[-] Wordlist file does not exist.")
        sys.exit(1)

    if not shutil.which("hashcat"):
        print("[-] Hashcat is not installed or not in PATH.")
        sys.exit(1)


def create_temp_hash_file(hashes):
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    for h in hashes:
        temp_file.write(h.strip() + "\n")
    temp_file.close()
    return temp_file.name


def build_hashcat_command(args, hash_file):
    command = [
        "hashcat",
        "-m", str(args.mode),
        "-a", str(args.attack_mode),
        hash_file,
        args.wordlist
    ]

    if args.rules:
        command.extend(["-r", args.rules])

    if args.output:
        command.extend(["-o", args.output])

    if args.session:
        command.extend(["--session", args.session])

    return command


def run_hashcat(command):
    try:
        subprocess.run(command)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
        sys.exit(1)


def main():
    """
    Main entry point for the script.
    """
    display_banner()
    args = get_user_input()
    hashes = [h.strip() for h in args.hashes.split(",") if h.strip()]
    validate_environment(args.wordlist)
    hash_file = create_temp_hash_file(hashes)
    command = build_hashcat_command(args, hash_file)
    print("[*] Running:", " ".join(command))
    run_hashcat(command)
    os.remove(hash_file)


if __name__ == '__main__':
    main()
