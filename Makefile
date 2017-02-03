

#latexfile = connected-warmup

all: congress/docs/congress.pdf \
	mario/docs/mario.pdf \
	connected-warmup/docs/connected-warmup.pdf \
	mario/docs/report.pdf \
	giantbook/docs/giantbook.pdf \
	randomqueue/docs/randomqueue.pdf\
	gorillahash/docs/gorillahash.pdf\
	runsort/docs/runsort.pdf

%.pdf : %.tex Makefile createpdf.sh .git/index
	bash createpdf.sh $@

