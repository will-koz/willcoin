package:
	~/.local/bin/pipreqs . --force

clean:
	rm -rf __pycache__

.PHONY: package clean
