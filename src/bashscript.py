	#!/usr/bin/env bash
import subprocess
import sys
# working committing->pushing script
import random
import os
from time import time
from random import randint
from mk_copy import main_echo
import json
from shutil import copy
from colorama import Fore, Back, init ,Style
from commit_Random import commit_Str

# Set-ExecutionPolicy -ExecutionPolicy Unrestricted
# p = subprocess.Popen(['powershell.exe', command], stdout=sys.stdout)

# for retriving commit count
local = True
count_c = 0
if local == True:
	try:
		with open ("count.json" ,"r") as count_file:
			count_c = int(json.load(count_file))
			# print(count_c)
	except Exception as e:
		count = 0


# for saving commit count
def save_commits(num:int) -> None :
		with open('count.json' ,'w') as jsn:
			json.dump(num ,jsn)


# creates a file and returns the filename
def echo(base_scr:str ,base_D:str) -> str:
	global count_c
	filename = main_echo(base_scr ,base_D ,count_c)
	count_c += 1
	return filename


# creates the folder based on given path 
def create(base:str ,arg:int) -> 'Explicit Return':
	# check for existing folder
	# os.path.exists()
	if os.path.exists(base + str(arg)):
		return 
	create_here = subprocess.run(['mkdir' ,str(arg)] ,shell = True)


# changes the current working directory
def cd_in(base:str ,local:str) -> str:
	os.chdir(base+local)
	return base + local +'//'


# same like cd_in but reverse 
def cd_out(par_base:str) -> 'Explicit Return':
	os.chdir(par_base)


# calls the ps1 script with all required arguments
def ps_script(Y:int ,M:int ,D:int ,H:int ,file:str ,base_cur:str ,commit_string:str) -> 'Explicit Return':
	filename = file
	file = base_cur + file
	proc = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                            '-ExecutionPolicy',
                            'Bypass',
                            f'./script_cmt.ps1 {Y} {M} {D} {H} {file} {filename} "{commit_string}"'], 
							stdout=sys.stdout)
	proc.wait()


# called by main , this sets the path correct and calls ps_script()
def call_script(base_scr:str ,Y:int ,M:int ,D:int ,H:int ,file:str ,base_cur:str) -> 'Explicit Return':
	global count_c
	# print(os.getcwd().replace('\\','//') + '//')
	os.chdir(base_scr) # problem
	# print(os.getcwd().replace('\\','//') + '//')
	commit_string = commit_Str(base_scr , count_c)
	ps_script(Y ,M ,D ,H ,file ,base_cur ,commit_string) #searching on main
	os.chdir(base_cur)


# git rm . -rf (basically)
def cleanup() -> 'Explicit Return':
	proc_clean = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                            '-ExecutionPolicy','Bypass',
                            './script_clean.ps1'],stdout=sys.stdout)
	proc_clean.wait()


# you know it
def main():
	global count_c
	try:
		base_scr = os.getcwd().replace('\\','//') + '//'
		folder = 'main_dir'
		create(base_scr, folder) # base + folder for checking
		base = cd_in(base_scr ,folder)
		# ste Y,M,D ranges correspondingly
		# year_start , year_end = map(int , input('>>> Input Year [start , end] * {with comma}\n').split(','))
		# for Y in range(2020 ,2021):
		for Y in range(2020 ,2021):
			create(base ,Y)
			base_Y = cd_in(base ,str(Y))

			for M in range(6 ,7):
				create(base_Y ,M)
				base_M = cd_in(base_Y ,str(M))

				for D in range(1 ,31): 
					# for random day commits
					if randint(1,5)%4 >= 1: # more chances:
						create(base_M ,D)
						base_D = cd_in(base_M ,str(D))

						for H in range(0,8):

							if randint(1,7) % 5 >= 2:
								count_c += 1
								filename = echo(base_scr ,base_D)
								call_script(base_scr,Y,M,D,H,filename ,base_D) # base_scr -> base
								print(commit_Str(base_scr , count_c))

							else: 
								pass
						cd_out(base_M)
					else: 
						pass
				cd_out(base_Y)
			cd_out(base)

		cd_out(base_scr)
		# cleanup() # off turn on accordingly
	except Exception as err:
		print(err)
		# return
	finally:
		if local :save_commits(count_c)
		print(Fore.WHITE ,Back.GREEN +f'\n\n\nTotal commits -> {count_c}')
	

if __name__ == '__main__':
	os.system('color 9')
	s = time()
	main()
	print(Fore.WHITE ,Back.GREEN + f'time taken -> {time()-s}')
	print(Style.RESET_ALL)
	exit()
