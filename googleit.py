#!/usr/bin/python

import webbrowser
import sys

searchurl = 'https://www.google.com/#q='

def search(texto):
	global searchurl
	searchurl += montaurl(texto)
	webbrowser.open_new(searchurl)
	
def montaurl(texto):
	lista = texto.split()
	url = ""
	for nome in lista:
		if url == "":
			url += nome
		else:
			url += "+" + nome

	return url

search(sys.argv[1])
