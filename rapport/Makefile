
REPORTS = methodology
FOLDERS = $(addsuffix /, $(REPORTS))
PDFS = $(join $(FOLDERS), $(addsuffix .pdf, $(REPORTS)))

all: $(PDFS)

*/%.pdf: */layout_pandoc.yaml */%.md
	cd $(@D) && pandoc $(^F) -o $(@F)

.PHONY: clean remake r
clean:
	rm -f $(PDFS)

remake: clean all
r: remake
