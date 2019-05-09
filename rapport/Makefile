
REPORTS = methodology analysis
FOLDERS = $(addsuffix /, $(REPORTS))
ALL_MDS = $(join $(FOLDERS), $(addsuffix .md, $(REPORTS))) 1_semester/rapport.tex
PDFS = $(join $(FOLDERS), $(addsuffix .pdf, $(REPORTS)))

# crazy makefile functions
space :=
space +=
join-with = $(subst $(space),$1,$(strip $2))

FOLDERS_COLONS = $(call join-with,:,$(FOLDERS))


all: $(PDFS) rapport.html

%.html: $(ALL_MDS) html_pandoc.yaml
	pandoc $^ -o $@ --resource-path $(FOLDERS_COLONS) --self-contained

*/%.pdf: */layout_pandoc.yaml */%.md
	cd $(@D) && pandoc $(^F) -o $(@F)

.PHONY: clean remake r
clean:
	rm -f $(PDFS) *.html

remake: clean all
r: remake
