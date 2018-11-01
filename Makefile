all:

clean:

install:
	chmod 755 banner.py
	chmod 755 install.py
	chmod 755 run.sh
	chmod 755 PPAP.py
	mkdir -p $(DESTDIR)/opt/PPAP/
	mkdir -p $(DESTDIR)/usr/share/doc/PPAP/
	mkdir -p $(DESTDIR)/opt/PPAP/tools/
	mkdir -p $(DESTDIR)/usr/bin/
	cp banner.py $(DESTDIR)/opt/PPAP/
	cp install.py $(DESTDIR)/opt/PPAP/
	cp LICENSE $(DESTDIR)/opt/PPAP/
	cp Makefile $(DESTDIR)/opt/PPAP/
	cp README.md $(DESTDIR)/opt/PPAP/
	cp README.md $(DESTDIR)/usr/share/doc/PPAP/
	cp run.sh $(DESTDIR)/opt/PPAP/
	cp run.sh $(DESTDIR)/usr/bin/
	cp PPAP.py $(DESTDIR)/opt/PPAP/
	cp -r tools $(DESTDIR)/opt/PPAP/
	

