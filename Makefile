.PHONY: all install version release clean

help:
	@echo "Make commands for packaging, releasing, and publishing ecos-python"
	@echo ""
	@echo "  version:  generates a version string using git tags for ecos-python"
	@echo "  install:  installs local version of ecos-python"
	@echo "  release:  uploads the wheels in the `dist` folder"

TAG := $(shell git describe --tags --always --dirty=.dirty | \
	sed 's/v\(.*\)/\1/' | \
	sed 's/\([0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\)-\([0-9][0-9]*\)-\(g.*\)/\1.dev\2+\3/')

all: version

version:
	@echo "__version__=\"$(TAG)\"" > src/ecos/version.py

src/ecos/version.py: version

install: version
	pip install .

release:
	twine upload dist/*

clean:
	@echo "nothing"

