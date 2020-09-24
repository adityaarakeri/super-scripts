from execute import execute_command
import sys

domain_name_without_www = sys.argv[1]

print(" ".join(["sudo", "add-apt-repository", "ppa:certbot/certbot"]))
output, returncode = execute_command(["sudo", "add-apt-repository", "ppa:certbot/certbot"])
print(output)
if returncode != 0:
    exit(0)

print(" ".join(["sudo", "apt", "install", "python-certbot-nginx"]))
output, returncode = execute_command(["sudo", "apt", "install", "python-certbot-nginx"])
print(output)
if returncode != 0:
    exit(0)

print(" ".join(["sudo", "certbot", "--nginx", "-d", domain_name_without_www, "www." + domain_name_without_www]))
output, returncode = execute_command(["sudo", "certbot", "--nginx", "-d", domain_name_without_www, "www." + domain_name_without_www])
print(output)
if returncode != 0:
    exit(0)
