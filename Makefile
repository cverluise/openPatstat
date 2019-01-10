SCRIPTDIR = bin/
PKGDIR = open_patstat/
EDADIR = EDA/
DATADIR = data/
PLOTDIR = plots/

#OUTPUTS=
.PHONY: clean

#all: $(OUTPUTS)

open_patstat/requirements.txt:
	pipreqs --force $(PKGDIR)

#clean:
#	rm -rf $(OUTPUTS)