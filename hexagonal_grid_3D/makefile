SRC := src/*.cpp
TARGET := build/game.out

CXX := g++
CXXFLAGS := -Wall -Werror
LDLIBS := -lraylib -lGL -lm -lpthread -ldl -lrt -lX11

COMPILE_COMMAND = bear -- $(CXX) $(CXXFLAGS) $(SRC) $(LDLIBS) -o $(TARGET)

.PHONY: all debug build_dir clean

all: build_dir
	$(COMPILE_COMMAND)


debug: build_dir
	$(COMPILE_COMMAND) -g

build_dir:
	mkdir -p build

clean:
	test -d build && rm -r build || true
	test -d .cache && rm -r .cache || true
	test -f compile_commands.json && rm compile_commands.json || true
