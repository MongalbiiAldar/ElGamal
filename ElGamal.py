#!/usr/bin/python
# -*- coding: utf-8 -*-

import bint as bint
import sys
import random

def is_prime(m):
	#Тест Миллера-Рабина на простоту числа
	t = m - 1 # наше число p-1
	s = 0#степень
	r=20 #кол-во раундов
	while t % 2 == 0:
		t = t / 2
		s = s + 1
	
	for repeat in xrange(r):       
		a = 0
		while a == 0:
			a = random.randrange(m)
		
		x = pow(a, t, m)
		if x == 1:
			return True
		for i in xrange(s - 1):
			if x == m - 1:
				return True
			x = (x * x) % m
		if x != m - 1:
			return False
	return True

def Generation_keys():
	File = open("p.txt","r") #открываем файл на чтение
	p = int(File.read())#считываем файл целиком
	File.close()
	
	# проверяем число p из файла на простоту с помощью теста Миллера
	if not is_prime(p): 
		raise ValueError("Выбранное число не является простым.")
	
	#выбор g	
	while True:
		g = random.randint(2, p - 1)#g - тоже случайное число 2<g<p-1

		if ((p - 1) % g) != 1:#чтоб g не равнялся p-1
			break

	x = random.randint(2, p - 1) #секретный ключ x, который равен 1<x<p

	p = bint.bint(str(p))#перевод типов в длинную арифметику

	g = bint.bint(str(g))

	x = bint.bint(str(x))

	y = p.powmod(g, x, p)#расчет y=g^x mod p
	
	#открытыми являются (p,g,y) а закрытым x
	return p, g, y, x

def Coding(msg,p,g,y,x):
	msg = bint.bint(str(msg))
	if msg > p:
		raise ValueError("Неверная длина сообщения")
	pp = p.st()#копируем содержимое p в pp

	pp = int(pp)#преобразование типов bigint в int

	k = random.randint(2, pp - 1)# 1<k<p-1

	k = bint.bint(str(k))#k переведем в большие числа

	a = p.powmod(g, k, p)      #a=g^k mod p                             # A

	b = p.powmod(y, k, p)      #b=y^k mod p                             # B
	b = (msg * b) % p         #b=(msg * y^k mod p)
	#print(a)
	#print(b)
	return a,b
def Decoding(p, x, a, b):
	                                 
	h=1
	h = bint.bint(str(h))#k переведем в большие числа, чтоб второй аргумент ф-ии powmod был bint	
	Decode_message = (b*p.powmod(a,p-h-x,p))%p	
	#print(Decode_message)

	return Decode_message

def usage():
	print "\nИспользование: python ElGamal.py msg.txt\n"

	sys.exit(-1)


if __name__ == "__main__":           #главная функция main
	if len(sys.argv) != 2:
		usage()

	f = open(sys.argv[1]) #открываем входной файл
	
	msg = int(f.read())#Встроенная функция прочтения содержимого файла и инициализации msg
	
	f.close()

	p, g, y, x = Generation_keys()#генерирование ключей

	a,b = Coding(msg,p,g,y,x)#закодируем сообщение при помощи пары (a,b)	
	Decode_message = Decoding(p, x, a, b)

	f = open("Decode_message.txt", "w")

	f.write(Decode_message.st())#запись расшифрованного текста

	f.close()
