# HashCatnip.py

import optparse
import pyfiglet
import subprocess


# Constants
HASH = ""
WORD_LIST = ""
DEFAULT_HASH_FILE = "hash.txt"


def display_banner():
    """
    Display ASCII banner.
    """

    banner = pyfiglet.figlet_format("HashCatnip")
    print(banner)


def get_user_input():
    """
    Get input from the user.
    """

    global HASH, WORD_LIST

    parser = optparse.OptionParser(
        usage="usage: %prog -H <enter_your_hash_to_crack> -l <enter_you_wordlist_path",
        description="Utility to automate Hashcat usage.",
        epilog="""By Taji Abdullah https://coded-alchemy.github.io"""
    )
    parser.add_option('-H', dest='hash', type='string', help='specify hash to crack.')
    parser.add_option('-l', dest='word_list', type='string', help='specify word list location.')

    (options, args) = parser.parse_args()

    # Ensure a hash is provided
    if not options.hash:
        parser.error("A hash is required. Use -H to specify it.")

    HASH = options.hash

    if not options.word_list:
        parser.error("A word list is required. Use -l to specify it.")

    WORD_LIST = options.word_list


def store_hash_in_file():
    """
    Store hash in file to pass into Hashcat.
    """

    global HASH, DEFAULT_HASH_FILE

    # Open the file in write mode and store the hash
    with open(DEFAULT_HASH_FILE, 'w') as file:
        file.write(HASH)


def use_hashcat():
    # Command to run Hashcat with the --show option
    command = ['hashcat', '--show', DEFAULT_HASH_FILE]

    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the standard output (results of the command)
    print(result.stdout)

    # Print any errors (if there are any)
#    if result.stderr:
#        print(result.stderr)


def do_crack():
    try:
        hash_mode = int(input("Enter hash mode number: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer for hash mode.")
        return

    command = ['hashcat', '-m', str(hash_mode), '-a', '0', DEFAULT_HASH_FILE, WORD_LIST]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print("Hashcat cracked the hash:")
        print(result.stdout)
    else:
        print("Hashcat failed to crack the hash.")
        print(f"Error: {result.stderr}")


def main():
    """
    Main entry point for the script.
    """

    display_banner()
    get_user_input()
    store_hash_in_file()
    use_hashcat()
    do_crack()


if __name__ == '__main__':
    main()