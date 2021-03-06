from sys import argv
import urllib
from urllib import request
from bs4 import BeautifulSoup
import datetime
import os
def ShowHelp():
	
	logo = """ _           _                                            _ _
(_)_ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___         __| | |
| | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \ _____ / _` | |
| | | | \__ \ || (_| | (_| | | | (_| | | | | | |_____| (_| | |
|_|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|      \__,_|_|
                      |___/"""
	
	
	print(logo)
	
	print('')
	print('Insta Image Downloader')
	print('')
	print('Usage:')
	print('insta.py [OPTION] [URL]')
	print('')
	print('Options:')
	print('-u [Instagram URL]\tDownload single photo from Instagram URL')
	print('-f [File path]\t\tDownload Instagram photo(s) using file list')
	print('-h, --help\t\tShow this help message')
	print('')
	print('Example:')
	print('python insta.py -u https://instagram.com/p/xxxxx')
	print('python insta.py -f filelist.txt')
	print('')
	print('Code by madewgn.my.id')
	exit()

def DownloadSingleFile(fileURL):
	print('Downloading image...')
	f = urllib.request.urlopen(fileURL)
	htmlSource = f.read()
	soup = BeautifulSoup(htmlSource,'html.parser')
	metaTag = soup.find_all('meta', {'property':'og:image'})
	imgURL = metaTag[0]['content']
	fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.jpg'
	urllib.request.urlretrieve(imgURL, fileName)
	print('Done. Image saved to disk as ', fileName)



if __name__ == '__main__':
	if len(argv) == 1:
		ShowHelp()

	if argv[1] in ('-h', '--help'):
		ShowHelp()
	
	elif argv[1] == '-u':
		instagramURL = argv[2]
		DownloadSingleFile(instagramURL)

	elif argv[1] == '-f':
		filePath = argv[2]
		f = open(filePath)
		line = f.readline()
		while line:
			instagramURL = line.rstrip('\n')
			DownloadSingleFile(instagramURL)
			
			line = f.readline()
		f.close()
