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

congress/docs/congress.pdf: congress/docs/congressphoto.pdf

gorillahash/docs/gorillahash.pdf: gorillahash/docs/sea_cucumber.png

mario/docs/mario.pdf: mario/docs/mario.png mario/docs/racetrack.pdf
