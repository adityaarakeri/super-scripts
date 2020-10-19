## CURRENT WORKING DIRECTORY

Getting the present working directory is easy on Linux and Mac because it’s built into the shell as the pwd command. But pwd is a POSIX environmental variable, which means it won’t work on Windows. As a result, we can use the command called cwd so it will not interfere if you choose to use it on either Mac or Linux, but is primarily aimed at Windows.

Running this script on its own will display the current working directory. If we pass the -c flag it automatically copies the current working directory to the clipboard on Mac or Windows, which saves a lot of retyping and mouse movements.

In addition, we can pass a filename as an argument and have its full path copied to the clipboard, which is something we need to do often when running test cases.

# To Run the Script:

Open command prompt.

python3 current_working_directory.py <file_name>

python3 current_working_directory.py -c <file_name> (Path of the current working directory gets copied to ClipBoard)

It gets current working directory or the absolute path to a file name that is passed as an argument. The "-c" option automatically copies the output to the clipboard on a Mac or Windows host.

