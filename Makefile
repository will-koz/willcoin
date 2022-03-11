# Python is not a compiled language, but I figured it would be easier to use make to automate some
# of the actions I make to update the program

package:
	~/.local/bin/pipreqs . --force

clean:
	rm -rf __pycache__

install:
	touch token.txt

.PHONY: package clean install
