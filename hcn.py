# HashCatnip.py

import optparse


# Constants
HASH = ""


def get_user_input():
    """
    Get input from the user.
    """
    global HASH

    parser = optparse.OptionParser(
        usage="usage: %prog -H <enter_your_hash_to_crack>",
        description="Hashcat Automation.",
        epilog="""Utility to automate Hashcat usage."""
    )
    parser.add_option('-H', dest='hash', type='string', help='specify hash to crack.')

    (options, args) = parser.parse_args()

    # Ensure a hash is provided
    if not options.hash:
        parser.error("A hash is required. Use -H to specify it.")

    HASH = options.hash


def store_hash_in_file():
    global HASH

    # Open the file in write mode and store the hash
    with open('hash.txt', 'w') as file:
        file.write(HASH)

    print("Hash has been written to hash.txt")


def main():
    """
    Main entry point for the script.
    """
    get_user_input()
    store_hash_in_file()


if __name__ == '__main__':
    main()