### basic settings ###
SHELL		= /bin/bash

# directories
CURR_DIR	= $(shell pwd)
TEST_DIR	= $(TOP_DIR)/tests

.PHONY: test

all: test game

build:
	docker build -t knights . --no-cache

game:
	docker run -it --rm -v $(CURR_DIR)/src:/home/knights:rw knights python game.py

test:
	pytest tests

clean:
	docker rmi knights
