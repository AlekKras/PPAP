# PPAP
=
PPAP is a penetration testing toolkit. It is used for quick testing.
Powered by <a href="https://www.bettercap.org"> bettercap</a> and <a href="https://www.bettercap.org"> nmap</a>.

Dependencies
=

- nmap 
- hping3 
- build-essential 
- ruby-dev 
- libpcap-dev 
- libgmp3-dev
- tabulate 
- terminaltables

Instalation
=

You have two options: 
1) Standard Local way:

Dependencies will be automatically installed.

```
    git clone https://github.com/AlekKras/PPAP.git
    cd PPAP && sudo python install.py
    sudo PPAP
```
2) Docker way:

Build the image:

`docker build -t "ppap:dockerfile" .`

Run the container:

`docker run -it ppap:dockerfile bash`


features 
=
- Port scanning
- Network mapping
- Dos attack
- Html code injection
- Javascript code injection
- Sniffing
- Dns spoofing
- Drifnet
- Webpage defacement

I have some questions!
=

Please visit https://github.com/AlekKras/PPAP/issues