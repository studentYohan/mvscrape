#Python script for creating .nfo files for music videos in Kodi
#Copyright Ben Okkema 2016
#Use it however you like, just buy me a beer if we ever meet
#Run the script in the directory containing all your music videos
#Filenames MUST be "ARTIST - TITLE.mp4"

#import stuff
from lxml import etree
from os.path import basename, splitext
from os import getcwd
from glob import glob

#get filenames in current directory
fname = glob(basename(getcwd() + "/*.mp4"))

#loop for all files
for i in range(len(fname)):
	
	#separate filename into title and artist
	track = splitext(fname[i])
	at = track[0].split(' - ')
	artist = at[0]
	title = at[1]
	
	#create .nfo xml file
	nfo = open(track[0] + '.nfo', 'w+')
	root = etree.Element('musicvideo')
	xtitle = etree.Element('title')
	xtitle.text = title
	root.append(xtitle)
	xartist = etree.Element('artist')
	xartist.text = artist
	root.append(xartist)
	s = etree.tostring(root, pretty_print=True)
	nfo.write(s)
	nfo.close()
