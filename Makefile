# Python is not a compiled language, but I figured it would be easier to use make to automate some
# of the actions I make to update the program

package:
	~/.local/bin/pipreqs . --force
	echo "# This was automatically generated by pipreqs" >> requirements.txt

clean:
	rm -rf __pycache__

fortuned:
	# fortune dump
	python3 -c "import wu ; wu.fortune_dump()"

install:
	chmod +x install
	./install

.PHONY: package clean fortuned install
