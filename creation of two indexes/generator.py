print('Hello, World!')

f=open('index_data/main0.xml')
data=f.read()
f.close()

import os
print(os.listdir('index_data'))

objects=[]
misc=[]
person=[]
animals=[]
place=[]

print(data)

import xml.etree.ElementTree as ET

for elem in os.listdir('index_data'):

	tree = ET.parse('index_data/'+elem)
	root = tree.getroot()

	category=root[1].get('category')

	if category=='object':
		objects.append(elem)
	elif category=='Misc':
		misc.append(elem)
	elif category=='person':
		person.append(elem)
	elif category=='animals':
		animals.append(elem)
	elif category=='place':
		place.append(elem)
	else:
		misc.append(elem)


	# print(objects)

#OK it needs to go in TWO places.

categories=[objects,person,animals,place,misc]
#print(categories)

#Initialize the xml tree and set everything up
#then append in your stuff

#Let's first make one file

from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

file1=os.listdir('index_data')

files=[]

for elem in file1:
	files.append(elem[:-4])


#need to add 5 elements. The other xml files
files.append('Animals')
files.append('MiscEntries')
files.append('People')
files.append('Places')
files.append('Objects')

fil=[]
fil.append('Objects')
fil.append('People')
fil.append('Animals')
fil.append('Places')
fil.append('MiscEntries')


_buffer=[]

import xml.etree.ElementTree as ET

true_buffer=[]

i=0
for category in categories:

	true_buffer.append(fil[i]+'.xml')

	print('We\'re at ' + str(i))

	i+=1
	_buffer=[]
	for elem in category:
		print(elem)
		tree = ET.parse('index_data/'+elem)
		root = tree.getroot()
		ans=root[1][0][0][0].text
		print('starting')
		if ans[:4] == 'The ':
			_buffer.append((root[1][0][0][0].text[4:]+'BENIN',elem))
		else:
			_buffer.append((root[1][0][0][0].text,elem))
		print(_buffer)

	_buffer.sort()
	print(_buffer)
	for (elem,unrelated) in _buffer:
		true_buffer.append(unrelated)
	print(true_buffer)
	print('Done')

actual_buffer=[]

print(true_buffer)

for elem in true_buffer:
	actual_buffer.append(elem[:-4])

print('\n\n\n\n')
print(actual_buffer)

# Add line literally
doc.asis(r'<?xml version="1.0" encoding="UTF-8"?>')
with tag('package', xmlns="http://www.idpf.org/2007/opf", version="2.0", uniqueDASHidentifier="PrimaryID"):
	with tag('metadata', XMLNSSdc="http://purl.org/dc/elements/1.1/", XMLNSSopf="http://www.idpf.org/2007/opf",XMLNSSxsi="http://www.w3.org/2001/XMLSchema-instance",XMLNSSdcterms="http://purl.org/dc/terms/"):
		doc.asis(
			'<dc:title>Great Expectations</dc:title>',
			'<dc:creator opf:role="aut" opf:file-as="Dickens, Charles">Charles Dickens</dc:creator>',
			'<dc:identifier id="PrimaryID" opf:scheme="URN">urn:uuid:91d9832a-4f5f-11e6-be34-4c72b9252ec6</dc:identifier>',
			'<dc:publisher>Feedbooks</dc:publisher>',
			'<dc:description>r of 1840.</dc:description>',
			'<dc:coverage/>',
			'<dc:source>Wikisource</dc:source>',
			'<dc:date>1861-08-15T08:00:00+00:00</dc:date>',
			'<dc:date opf:event="ops-publication">2006-12-30</dc:date>',
			'<dc:rights/>',
			'<dc:subject>Fiction</dc:subject>',
			'<dc:language>en</dc:language>',
			'<dc:identifier opf:scheme="calibre">af1fe065-9d31-4e1c-b8bc-512092ef390c</dc:identifier>',
			'<dc:identifier opf:scheme="URI">http://www.feedbooks.com/book/70</dc:identifier>',
			'<meta name="cover" content="book-cover"/>',
			'<meta name="calibre:title_sort" content="Great Expectations"/>',
			'<meta name="calibre:author_link_map" content="{&quot;Charles Dickens&quot;: &quot;&quot;}"/>',
		)
	with tag('manifest'):
		for elem in actual_buffer:
			doc.asis('<item id="'+elem+'" href="'+elem+'.xml" media-type="application/xhtml+xml" />')
		doc.asis(
			'<item id="main-css" href="css/main.css" media-type="text/css" />',
			'<item id="book-cover" href="images/cover.png" media-type="image/png" />',
			'<item id="ncx" href="fb.ncx" media-type="application/dtbncx+xml" />'
		)
	with tag('spine', toc='ncx'):
		for elem in actual_buffer:
			doc.asis('<itemref idref="'+elem+'" linear="yes" />')
	with tag('guide'):
		for elem in actual_buffer:
			doc.asis('<reference type="text" title="'+elem+'" href="'+elem+'.xml" />')

result = indent(
	doc.getvalue().replace('DASH','-').replace('XMLNSS','xmlns:'),
	indentation = ' '*4,
	newline = '\r'
)

f=open('fb.opf','w+')
f.write(result)
f.close()