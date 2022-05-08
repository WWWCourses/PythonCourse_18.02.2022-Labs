# TASK: print stat of current script file
import os

script_name = __file__

stat_res = os.stat(script_name)
print(f'stat_res.st_size: {stat_res.st_size}')
print(f'stat_res.st_mode: {stat_res.st_mode}')
