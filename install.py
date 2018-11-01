#!/usr/bin/python
# -*- coding: utf-8 -*-
#Maintainer: Aleksandr Krasnov
import os
import sys
if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] 😤 PPAP installer must be run as root \n\033[1;m""")
print(""" \033[1;36m

                  oyssssssssssssyyyysyooossssooossoooossooooossssssssoosossssossssho`
      .yd-       o-...................................-.......------------------:mMNm-     `
     /dssNm`    ::.............................................................-hmmdyd   :dNo
    `yy/ohNhhdmhh-.............................................................oo-mdhd++omoyN-
   `oyo/sys/+oos/..............................................................y-sdooosssy+yhs
:o/osm+/yy+////s-.............................................................:h-ms/////os/hyh/  `
oyyhNd++hhooo++s...............P.P.A.P....I.n.s.t.a.l.l.e.r...................oo/Mo/////oo+hhyhy+hh`
ooshNhysdhhyyyho..............................................................y+oNooossssyshdMmmdyN-
`.`-oyNmNymmddN/..............................................................h/ymyyyyyysddmhNh+--/`
    -+NMMhNddmN-..............................................................d:dmmdddddsMMNyy-
     :yNNhm/--/..............................................................-m+hsyyyyys+dNNy/
     `-+o+/   /.....P.e.n.e.t.r.a.t.i.o.n....t.e.s.t.i.n.g....t.o.o.l........-N+mmo+ss- `+shy`
       `-`    /..............................................................:Mymdoo+y   `-/`
              /............................................................../Mymdoy/s
              +..............................................................+Mmmmy/s-
             `/..............................................................oNdsy:o+
             -:.............................................................-oo:-:::
             --.............................................................-y-
             -:.............................................................-y.
             /..............................................................-y:
        `````+-------------:::::::::::::::::::::::::::::::::/::::::///++/-..-y:
       -ssoo+o+////////////////++++++++++++/////////////:::::::::::::+Nmdh/.-y:
      -/-.---.......................................................-mNs:-h--y:
      :.............................................................+yody-o/-h:
      /.............................................................y-omy+/o-d.
     --.............................................................h-hm+s:o-d
     ...............................................................h:hmoo/+:d
     ...............................................................yssdy:s-/s
      -.............................................................odsh:+s-y/
      :.--..--...---------------:::::/:///////////////+++++/////////+doss+.:h
      .://+/+++++oossoooooooooooooooooooooooooo+ooooosssoooooooooooo+h+...-h.
       /+yyhhhhhhhhhhhyhhhyhhyyyyyyyyyyyyyyyyyyyyyysssssssssssssysyysshs+os.
        .:oo++////:::::::::--:-------------............-..-.............``

  \033[1;m""")

def main():

	print("\033[1;34m\n[++] 🤓  Chose your OS (currently we support the ones with APT package and ParrotOS\033[1;m")

	print("""
1) Ubuntu / Kali linux / Others
2) Parrot OS
""")
	system0 = raw_input(">>> ")
	if system0 == "1":
		print("\033[1;34m\n[++] 👀 Installing PPAP ... \033[1;m")
		install = os.system("apt-get update && apt-get install -y nmap hping3 build-essential python-pip ruby-dev git libpcap-dev libgmp3-dev && pip install tabulate terminaltables && apt autoremove -y")

		install1 = os.system("""cd tools/bettercap/ && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && mkdir -p /opt/PPAP && cp -R tools/ /opt/PPAP/ && cp PPAP.py /opt/PPAP/PPAP.py && cp banner.py /opt/PPAP/banner.py && cp run.sh /usr/bin/PPAP && chmod +x /usr/bin/PPAP && tput setaf 34; echo "PPAP has been sucessfuly instaled. Execute 'PPAP' in your terminal." """)
	elif system0 == "2":
		print("\033[1;34m\n[++] 👀 Installing PPAP ... \033[1;m")

		bet_un = os.system("apt-get remove bettercap") # Remove bettercap to avoid some problems . Installed by default with apt-get .
		bet_re_ins = os.system("gem install bettercap") # Reinstall bettercap with gem.

		install = os.system("apt-get update && apt-get install -y nmap hping3 ruby-dev git libpcap-dev libgmp3-dev python-tabulate python-terminaltables && apt autoremove -y")

		install1 = os.system("""cd tools/bettercap/ && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && mkdir -p /opt/PPAP && cp -R tools/ /opt/PPAP/ && cp PPAP.py /opt/PPAP/PPAP.py && cp banner.py /opt/PPAP/banner.py && cp run.sh /usr/bin/PPAP && chmod +x /usr/bin/PPAP && tput setaf 34; echo "PPAP has been sucessfuly instaled. Execute 'PPAP' in your terminal." """)


	else:
		print("Please select the option 1 or 2")
		main()
main()
