.PHONY: all install version release clean

help:
	@echo "Make commands for packaging, releasing, and publishing ecos-python"
	@echo ""
	@echo "  version:  generates a version string using git tags for ecos-python"
	@echo "  install:  installs local version of ecos-python"
	@echo "  release:  uploads the wheels in the `dist` folder"

TAG := $(shell git describe --tags --always --dirty=.dirty | \
	sed 's/v\(.*\)/\1/' | \
	sed 's/\([0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\)\(rc[0-9]*\)\{0,1\}-\([0-9][0-9]*\)-\(g.*\)/\1\2.dev\3+\4/')

all: version

version:
	@echo "__version__=\"$(TAG)\"" > src/ecos/version.py

src/ecos/version.py: version

install: version
	pip install .

release: version
	-rm -rf dist
	mkdir -p dist
	python setup.py sdist
	curl -s https://api.github.com/repos/embotech/ecos-python/releases/tags/$(TAG) \
		| grep browser_download_url.*whl \
		| cut -d : -f 2,3 \
		| tr -d \" \
		| wget -P dist -qi -
	twine upload dist/*

clean:
	@echo "nothing"

