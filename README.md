# Hash Catnip     
This script automates Hashcat usage. It allows for cracking one or more hashes against your choice of word list.

### Usage  
1. Download Hash Catnip to your environment:
	```curl -L -O https://github.com/Coded-Alchemy/HashCatnip/blob/dev/hcn.py```
2. Run this command with one or more comma separated hashes, and the path to your wordlist: 
	```python hcn.py -H <hash1,hash2,...> -l <enter your wordlist>``` 
  
[Watch the video](https://coded-alchemy.github.io/#/hashcatnip)  
  
See [Blog Post](https://technofiles.hashnode.dev/hash-catnip) for more info.  
  
### Requirements    
- Python should be installed.  
- Hashcat should be installed and accessible from the terminal.