#!/usr/bin/python
# -*- coding: utf-8 -*-
#Maintainer: Aleksandr Krasnov
import os
import sys
if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] PPAP installer must be run as root. ¯\_(ツ)_/¯\n\033[1;m""")

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

	print("\033[1;34m\n[++] Installing PPAP ... \033[1;m")
	install = os.system("apt-get update && apt-get install -y nmap hping3 build-essential python-pip ruby-dev git libpcap-dev libgmp3-dev && pip install tabulate terminaltables && apt autoremove -y")

	install1 = os.system("""cd tools/bettercap/ && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && mkdir -p /opt/PPAP && cp -R tools/ /opt/PPAP/ && cp PPAP.py /opt/PPAP/PPAP.py && cp banner.py /opt/PPAP/banner.py && cp run.sh /usr/bin/PPAP && chmod +x /usr/bin/PPAP && tput setaf 34; echo "PPAP has been sucessfuly instaled. Execute 'PPAP' in your terminal." """)	

main()