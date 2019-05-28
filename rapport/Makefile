
REPORTS = methodology analysis
FOLDERS = $(addsuffix /, $(REPORTS))

MDS = $(join $(FOLDERS), $(addsuffix .md, $(REPORTS)))
TEXS = 1_semester/rapport.tex $(join $(FOLDERS), $(addsuffix .tex, $(REPORTS)))
PDFS = $(join $(FOLDERS), $(addsuffix .pdf, $(REPORTS)))

# crazy makefile functions
space :=
space +=
join-with = $(subst $(space),$1,$(strip $2))

FOLDERS_COLONS = $(call join-with,:,$(FOLDERS)):1_semester/


all: $(PDFS)

1_semester/rapport.tex:

*/%.tex: */layout_pandoc.yaml */%.md
	cd $(@D) && pandoc $(^F) -o $(@F)

%.html: $(TEXS) html_pandoc.yaml
	pandoc $(TEXS) -o $@ --resource-path $(FOLDERS_COLONS) --self-contained

*/%.pdf: */layout_pandoc.yaml */%.md
	cd $(@D) && pandoc $(^F) -o $(@F)

.PHONY: clean remake r
clean:
	rm -f $(PDFS) *.html

remake: clean all
r: remake
