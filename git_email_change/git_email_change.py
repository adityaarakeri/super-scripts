import os
import subprocess


# Change these to respective values
p_email='personal_email@gmail.com'
w_email='work_email@gmail.com'

bash_command_1='git config user.email'
bash_command_2=f'git config user.email {p_email}'
current_dirpath=os.path.dirname(os.path.abspath(__file__))

def change_dir(dirpath):
    os.chdir(dirpath)
    process_1 = subprocess.Popen(bash_command_1.split(), stdout=subprocess.PIPE)
    output_1, error_1 = process_1.communicate()
    if output_1 == f'{w_email}\n'.encode() and not error_1:
        print(f'exists in directory: {dirpath}')
        print('updating...')
        process_2 = subprocess.Popen(bash_command_2.split(), stdout=subprocess.PIPE)
        output_2, error_2 = process_2.communicate()
        if not error_2:
            print(f'updated to : {output_2}')
        else:
            print(f'Error occured: {error_2}')        
    os.chdir(current_dirpath)

for dirpath, dirnames, filenames in os.walk(current_dirpath, topdown=True):
    if '.git' in dirnames:
        change_dir(dirpath)
