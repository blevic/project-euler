from pywebcopy import save_webpage
import time
import os

cwd = os.getcwd()
p_name = 'euler-problems'
MAX_PROBLEM = 785

url = 'https://projecteuler.net/minimal='
kwargs = {'bypass_robots': True, 'project_name': p_name, 'zip_project_folder': False}

for problem in range(1, MAX_PROBLEM + 1):
    save_webpage(url+str(problem), cwd, **kwargs)
    html_files = [i for i in os.listdir(os.path.join(cwd, p_name, "projecteuler.net")) if i.endswith("minimal.html")]
    if len(html_files) >= 1:
        os.rename(os.path.join(cwd, p_name, "projecteuler.net", html_files[0]), os.path.join(cwd, p_name, 'p' + str(problem).zfill(3) +'.html'))
    else:
        print(" ---> ERROR")
    time.sleep(1)
