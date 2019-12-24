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
from colorama import Fore, Back, init

# Set-ExecutionPolicy -ExecutionPolicy Unrestricted
# p = subprocess.Popen(['powershell.exe', command], stdout=sys.stdout)

count_c = 0

def echo(base_scr:str ,base_D:str) -> str:
	global count_c
	filename = main_echo(base_scr ,base_D ,count_c)
	count_c += 1
	return filename


def create(arg:int) -> 'Explicit Return':
	create_here = subprocess.run(['mkdir' ,str(arg)] ,shell = True)


def cd_in(base:str ,local:str) -> str:
	os.chdir(base+local)
	return base + local +'//'


def cd_out(par_base:str) -> 'Explicit Return':
	os.chdir(par_base)


def ps_script(Y:int ,M:int ,D:int ,H:int ,file:str ,base_cur:str) -> 'Explicit Return':
	filename = file
	file = base_cur + file
	proc = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                            '-ExecutionPolicy',
                            'Bypass',
                            f'./script_cmt.ps1 {Y} {M} {D} {H} {file} {filename}'], 
							stdout=sys.stdout)
	proc.wait()


def call_script(base_scr:str ,Y:int ,M:int ,D:int ,H:int ,file:str ,base_cur:str) _. 'Explicit Return:
	os.chdir(base_scr)
	ps_script(Y ,M ,D ,H ,file ,base_cur) #searching on main
	os.chdir(base_cur)


def cleanup() -> 'Explicit Return':
	proc_clean = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                            '-ExecutionPolicy','Bypass',
                            './script_clean.ps1'],stdout=sys.stdout)
	proc_clean.wait()


def main():
	cmmts = 0
	base_scr = os.getcwd().replace('\\','//') + '//'
	floder = 'main_dir'
	create(floder)
	base = cd_in(base_scr ,floder)
	# ste Y,M,D ranges correspondingly

	for Y in range(2019 ,2020):
		create(Y)
		base_Y = cd_in(base ,str(Y))

		for M in range(1 ,13):
			create(M)
			base_M = cd_in(base_Y ,str(M))

			for D in range(1 ,30): 
				# for random day commits
				if randint(1,5)%4 >= 1: # more chances:
					create(D)
					base_D = cd_in(base_M ,str(D))

					for H in range(0,8):

						if randint(1,5) % 5 >= 2:
							cmmts += 1
							filename = echo(base_scr ,base_D)
							call_script(base_scr,Y,M,D,H,filename ,base_D)
						else: 
							pass
					cd_out(base_M)
				else: 
					pass
			cd_out(base_Y)
		cd_out(base)

	cd_out(base_scr)
	cleanup()

	print(Fore.WHITE ,Back.GREEN +f'\n\n\nTotal commits -> {cmmts}')


if __name__ == '__main__':
	os.system('color 9')
	s = time()
	main()
	print(Fore.WHITE ,Back.GREEN + f'time taken -> {time()-s}')
	print(Style.RESET_ALL)
