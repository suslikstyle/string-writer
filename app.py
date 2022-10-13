import os
import sys
from time import sleep
from random import randint


def main():
	match sys.argv:
		case (_, '-h'|'--help'):
			print_help()
		case (_, filename):
			try:
				show(filename)
			except KeyboardInterrupt:
				print('\nПрервано пользователем...')
		case (_, '-s', speed, filename) if int(speed) > 0 and int(speed) <= 100:
			try:
				show(filename, int(speed))
			except KeyboardInterrupt:
				print('\nПрервано пользователем...')
		case _:
			print_help()


def show(filename: str, speed=42) -> None:
	print(filename)
	with open(filename, 'r', encoding='utf-8') as file:
		for line in file:
			if line == "\n":
				continue
			write_line(line.rstrip(), speed)
			print('')
			sleep(.4)

def write_line(line: str, speed) -> None:
	for char in line:
		print(char, end='', flush=True)
		if char == ' ':
			sleep(.05)
		sleep(randint(10, 33)/(speed*10))

def print_help()-> None:
	hlp_str = "Скрипт для посимвольного вывода текстов\n" + \
	'\nКак использовать:\n' + \
	f'python {os.path.basename(__file__)} [OPTIONS] <full filename>\n' + \
	'\nOPTIONS:\n' + \
	'-h 			Показ этого сообщения.\n' + \
	'-s 			Скорость вывода текста от 1 до 100\n'
	
	print(hlp_str)


if __name__ == '__main__':
	main()
