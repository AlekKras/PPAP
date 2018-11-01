PPAP
=

PPAP is a penetration testing toolkit. It is used for quick testing.
Powered by <a href="https://www.bettercap.org"> bettercap</a> and <a href="https://nmap.org/"> nmap</a>.

If you want to know what the dedication was, check [`PPAP.txt`](https://raw.githubusercontent.com/AlekKras/PPAP/master/PPAP.txt) and zoom out.


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

Once there, you will need to run `python PPAP/install_docker.py` and you will be good to go. You can also run the general script `python install.py`

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

Please visit [this](https://github.com/AlekKras/PPAP/issues)
