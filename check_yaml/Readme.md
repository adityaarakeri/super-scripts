## Check YAML

Kubernetes is difficult enough without having YAML fail to parse. This utility is a way to validate that the YAML is valid. Use it before ripping apart the program you are trying to load it into. This script will read a file and either pass the file as being a valid YAML file, or die a horrible death. But for all practical reasons, it tells me if the error is in the file or the program that I am trying to load the file into.

# Requirements:

This script requires the pyyaml plugin to be installed.

To install this plugin run the following command in the command prompt 

python3 -m pip install pyyaml
 
# To Run the Script:

Open command prompt.

python3 check_yaml.py <yaml file_name>

It returns Valid YAML if the file is a valid yaml file.