# Hash Catnip     
Automation wrapper for Hashcat that streamlines multi-hash cracking workflows using custom wordlists.

Hash Catnip reduces repetitive command-line overhead and improves workflow efficiency during password auditing and lab-based testing.

### Purpose

When working with Hashcat in lab or red-team simulations, cracking multiple hashes typically requires:
- Formatting input files
- Managing command syntax
- Tracking output
- Running multiple sequential commands

Hash Catnip simplifies this process by allowing users to:
- Submit multiple hashes at once
- Specify a wordlist
- Automatically handle execution
- Streamline output management

This tool is designed for educational use, lab environments, and authorized security testing only.

### Features
- Multi-hash support via comma-separated input
- Wordlist-based cracking
- Lightweight Python CLI interface
- Direct Hashcat execution from script
- Simplified workflow for lab exercises

### Requirements    
- Python 3.x 
- Hashcat installed and accessible from terminal
- Valid wordlist file

### Installation
Clone the repository:
	```git clone https://github.com/Coded-Alchemy/HashCatnip.git; cd HashCatnip```

Or download directly:
	```curl -L -O https://raw.githubusercontent.com/Coded-Alchemy/HashCatnip/dev/hcn.py```

### Usage  
Run the script with:
	```python hcn.py -H <hash1,hash2,...> -l <path_to_wordlist>``` 

Example
	```python hcn.py -H 5f4dcc3b5aa765d61d8327deb882cf99 -l /usr/share/wordlists/rockyou.txt```

This will:
- Pass the hash to Hashcat
- Use the specified wordlist
- Allow you to select hash mode for cracking
- Execute the cracking process
- Display results in terminal

[Watch the video](https://coded-alchemy.github.io/#/hashcatnip)  
  
See [Blog Post](https://technofiles.hashnode.dev/hash-catnip) for more info. 
  
### Security & Ethical Use
This tool is intended strictly for:
- Cybersecurity education
- Home lab experimentation
- Authorized penetration testing
- CTF practice

Do not use this tool against systems or data you do not own or have explicit permission to test.

### Why This Project Matters
This project demonstrates:
- Automation mindset
- CLI tool development
- Integration with external security tools
- Workflow optimization in offensive security contexts
- Practical Python scripting

This script shows how small automation tools can significantly improve operational efficiency.

### Author
Taji Abdullah
Security Analyst | Detection Engineering | Security Automation
