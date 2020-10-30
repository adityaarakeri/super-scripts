# Go Binary Compiler

This script automates the compiling process for Go files into binary without explicitly specifying each files. The binary will output to `./bin` folder.

:warning: Running this script will clean the `./bin` folder before compiling the binaries.

## Use Case

In Go, build command are usually embedded into a Makefile, for example:

```Makefile
build:
	dep ensure -v
	env GOOS=linux go build -ldflags="-s -w" -o bin/helloworld cmd/helloworld/main.go
	env GOOS=linux go build -ldflags="-s -w" -o bin/timenow cmd/timenow/main.go
```

With this script, you can write it as:

```Makefile
build:
    bash main.sh ./cmd
```

## Additional features

1. Color formatted logging.
1. Compiling (loading) indicator.
1. Total time elapsed logging.
1. Trap exit logging.
