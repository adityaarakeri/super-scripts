# python-scripts

There is a .bat file for each python script so it can be launched on Windows.
The yaml module isn't automatically loaded on all platforms, I see you Windows.

## checkjson and checkyaml

These files will validate if a file is validate YAML or JSON.
* Note yaml requires the pyyaml plugin to be installed (python3 -m pip install pyyaml)

## copy2clip

Copies the contents of whatever file is passed as an argument into the clipboard on a Mac or Windows host.

## convert2jpg

Need to convert images into jpg to upload into your old Dynamics expense reporting system like I do, well this tool does it.
* Note this requires the Image plugin to be installed (python3 -m pip install Image)

## cwd

Gets current working directory or the absolute path to a file name that is passed as an argument. The "-c" option automatically copies the output to the clipboard on a Mac or Windows host.


## json2yaml and yaml2json

Converts a file from either json or yaml to the other format. It can dump to stdout or a specified file.
* Note yaml requires the pyyaml plugin to be installed (python3 -m pip install pyyaml)


## quickmath

Allows to quickly perform a single math function on a list of numbers. Addition is the most common use case for me.
