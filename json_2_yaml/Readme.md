## JSON 2 YAML

This script converts a file from JSON to YAML. The output can either be sent to stdout or to a specified file. If we work with config files or need to expose YAML via an API, we’ll probably find ourselves needing to convert a file from JSON to YAML.

# Requirements:

This script requires the yaml plugin to be installed.

To install this plugin run the following command in the command prompt 

python3 -m pip install pyyaml

# To Run the Script:

Open command prompt.

python3 json_2_yaml.py <file_name>

It converts a file from json to the yaml format. It can dump to stdout or a specified file.