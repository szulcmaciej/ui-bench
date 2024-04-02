.phony: build run

build:
	docker build -t my-firefox .

run: build
	docker run --rm --name vnc-firefox -p 6080:80 -p 5900:5900 my-firefox
