## Copy 2 Clip 

Copying the contents of a text file to the clipboard is an all-too-frequent task, whether it’s a log file someone wants to see, a configuration file you need to share, or even an ssh key. Getting to the file is easy enough on the command line, but then having to open it in an editor just to copy-and-paste takes time you don’t need to waste.

The following copy_2_clip script works on both Windows and Mac, and uses native functionality that is wrapped in a little bit of Python code to load the files into the clipboard.

# To Run the Script:

Open command prompt.

python3 copy_2_clip.py <file_name>

It copies the contents of whatever file is passed as an argument into the clipboard on a Mac or Windows host.