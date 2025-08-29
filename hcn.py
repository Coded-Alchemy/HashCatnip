# HashCatnip.py

import optparse
import pyfiglet
import subprocess

# Constants
HASHES = []
WORD_LIST = ""
DEFAULT_HASH_FILE = "hash.txt"


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

    global HASHES, WORD_LIST

    parser = optparse.OptionParser(
        usage="usage: %prog -H <hash1,hash2,...> -l <enter_you_wordlist_path",
        description="Utility to automate Hashcat usage.",
        epilog="""By Taji Abdullah https://coded-alchemy.github.io\n"""
    )
    parser.add_option('-H', dest='hashes', type='string', help='Specify one or more hashes to crack, separated by commas.')
    parser.add_option('-l', dest='word_list', type='string', help='Specify word list location.')

    (options, args) = parser.parse_args()

    # Ensure hashes are provided
    if not options.hashes:
        parser.error("At least one hash is required. Use -H to specify it.")

    # Split hashes into a list
    HASHES = [h.strip() for h in options.hashes.split(',') if h.strip()]

    # Ensure a word list is provided
    if not options.word_list:
        parser.error("A word list is required. Use -l to specify it.")

    WORD_LIST = options.word_list


def store_hash_in_file():
    """
    Store hashes in file to pass into Hashcat.
    """

    global HASHES, DEFAULT_HASH_FILE

    # Open the file in write mode and store the hash
    with open(DEFAULT_HASH_FILE, 'w') as file:
        for h in HASHES:
            file.write(h + "\n")


def display_hash_mode_options():
    """
    Display Hashcat output to select hash mode.
    """

    try:
        # Command to run Hashcat with the --show option
        command = ['hashcat', '--show', DEFAULT_HASH_FILE]

        # Run the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Print the results of the command
        print(result.stdout)

    except FileNotFoundError:
        print("Unable to complete, is Hashcat installed?\n")
        exit()


def crack_hash():
    """
    Attempt to crack the hash with Hashcat.
    """
    try:
        hash_mode = int(input("Enter hash mode number: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer for hash mode.")
        return

    try:
        command = ['hashcat', '-m', str(hash_mode), '-a', '0', DEFAULT_HASH_FILE, WORD_LIST]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print("Hashcat cracked one or more hashes:")
            print(result.stdout)
        else:
            print("Hashcat failed to crack the hash.")
            print(f"Error: {result.stderr}")

    except FileNotFoundError:
        print("Unable to complete, is Hashcat installed?\n")
        exit()


def main():
    """
    Main entry point for the script.
    """

    display_banner()
    get_user_input()
    store_hash_in_file()
    display_hash_mode_options()
    crack_hash()


if __name__ == '__main__':
    main()
