#!/usr/bin/env bash
import subprocess
import sys
# working committing->pushing script
import random
import os
from time import time
from random import randint

# Set-ExecutionPolicy -ExecutionPolicy Unrestricted
# p = subprocess.Popen(['powershell.exe', command], stdout=sys.stdout)

def echo(st):
	fmt = '.txt'
	text = str(st)
	filename = str(st)+fmt
	subprocess.run(['echo' ,text ,'>' ,filename] ,shell = True)
	return filename


def create(arg):
	create_here = subprocess.run(['mkdir' ,str(arg)] ,shell = True)


def cd_in(base ,local):
	os.chdir(base+local)
	return base + local +'//'


def cd_out(par_base):
	os.chdir(par_base)


def ps_script(Y ,M ,D ,H ,file ,base_cur):
	file = base_cur + file
	proc = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                            '-ExecutionPolicy',
                            'Bypass',
                            f'./script_cmt.ps1 {Y} {M} {D} {H} {file}'], 
							stdout=sys.stdout)
	proc.wait()


def call_script(base_scr ,Y ,M ,D ,H ,file ,base_cur):
	os.chdir(base_scr)
	ps_script(Y ,M ,D ,H ,file ,base_cur) #searching on main
	os.chdir(base_cur)


def cleanup():
	proc_clean = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                            '-ExecutionPolicy','Bypass',
                            './script_clean.ps1'],stdout=sys.stdout)
	proc_clean.wait()


def main():
	cmmts = 0
	base_scr = os.getcwd().replace('\\','//') + '//'
	floder = 'main_folder'
	create(floder)
	base = cd_in(base_scr ,floder)
	for Y in range(2019 ,2020):
		create(Y)
		base_Y = cd_in(base ,str(Y))

		for M in range(1 ,3):
			create(M)
			base_M = cd_in(base_Y ,str(M))

			for D in range(1 ,3):
				# if randint(1,1000)%3 == randint(1,3):# for random day commits
				if randint(1,3)%3 <= 2: # more chances:
					create(D)
					base_D = cd_in(base_M ,str(D))

					for H in range(1,5):
						# if randint(1,1000) % 5 == randint(1,5):
						if randint(1,5) % 5 > 3:
							cmmts += 1
							filename = echo(H)
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
	print(f'\n\n\nTotal commits -> {cmmts}')

if __name__ == '__main__':
	s = time()
	main()
	print(f'>>>time taken -> {time()-s}')