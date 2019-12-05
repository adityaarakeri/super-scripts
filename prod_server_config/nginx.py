from execute import execute_command
import sys

domain_name_without_www = sys.argv[1]
project_name = sys.argv[2]

# Write the config to file
nginx_config_str = """server {{
    server_name {} {};

    location / {{
        include proxy_params;
        proxy_pass http://unix:/tmp/{}.sock;
    }}
}} """.format(domain_name_without_www, 'www.' + domain_name_without_www, project_name)

config_filename = "/etc/nginx/sites-available/{}".format(project_name) 

f = open(config_filename, "w+")
f.write(nginx_config_str)
f.close()

# Enable the config
print(" ".join(["sudo", "ln", "-s", "/etc/nginx/sites-available/".format(project_name), "/etc/nginx/sites-enabled"]))
output, returncode = execute_command(["sudo", "ln", "-s", "/etc/nginx/sites-available/".format(project_name), "/etc/nginx/sites-enabled"])
print(output)
if returncode != 0:
    exit(0) 

# Restart nginx 
print(" ".join(["sudo", "systemctl", "restart", "nginx"]))
output, returncode = execute_command(["sudo", "systemctl", "restart", "nginx"])
print(output)
if returncode != 0:
    exit(0)
