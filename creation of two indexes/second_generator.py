print('Hello, World!')

import os

objects=[]
misc=[]
person=[]
animals=[]
place=[]

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

categories=[objects,person,animals,place,misc]


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
sorted_buffer=[]

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
	sorted_buffer.append(_buffer)
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
print(len(actual_buffer))


from yattag import Doc, indent
import codecs

doc, tag, text = Doc().tagtext()

doc.asis(r'<?xml version="1.0" encoding="UTF-8"?>')

with tag('ncx'):
	doc.asis(
		'<head>',
			'<meta name="dtb:uid" content="91d9832a-4f5f-11e6-be34-4c72b9252ec6"/>',
			'<meta name="dtb:depth" content="2"/>',
			'<meta name="dtb:totalPageCount" content="0"/>',
			'<meta name="dtb:maxPageNumber" content="0"/>'
		'</head>'
	)
	
	with tag('docTitle'):
		with tag('text'):
			text('Pottermore - An Archive')
	
	with tag('docAuthor'):
		with tag('text'):
			text('JK Rowling')

	order=1
	with tag('navMap'):

		'''
		with tag('navPoint', replace_with_class='chapter', playOrder=order):
			with tag('navLabel'):
				with tag('text'):
					text('main0heah')

			with tag('content', src='main0.xml'):
				pass

			import xml.etree.ElementTree as ET
			tree = ET.parse('index_data/main0.xml')
			root = tree.getroot()
			print(root[1][0][0][0].text)



		with tag('navPoint', replace_with_class='chapter', playOrder=order):
			with tag('navLabel'):
				with tag('text'):
					text('main0headh')

			with tag('content', src='main1.xml'):
				pass
		'''

		'''
		fil.append('Objects')
		fil.append('People')
		fil.append('Animals')
		fil.append('Places')
		fil.append('MiscEntries')
		'''

		with tag('navPoint', replace_with_class='chapter', playOrder=order):
			with tag('navLabel'):
				with tag('text'):
					text('Objects')

			with tag('content', src='Objects.xml'):
				pass

			for name,index in sorted_buffer[0]:
				with tag('navPoint', replace_with_class='chapter', playOrder=order):

					print(name)
					tmp=name
					if 'BENIN' in name:
						tmp='The '+name[:-5]
					with tag('navLabel'):
						with tag('text'):
							text(tmp)

					with tag('content', src=index):
						pass
					print(tmp)

		order+=1

		with tag('navPoint', replace_with_class='chapter', playOrder=order):
			with tag('navLabel'):
				with tag('text'):
					text('People')	

			with tag('content', src='People.xml'):
				pass

			for name,index in sorted_buffer[1]:
				with tag('navPoint', replace_with_class='chapter', playOrder=order):

					print(name)
					tmp=name
					if 'BENIN' in name:
						tmp='The '+name[:-5]
					with tag('navLabel'):
						with tag('text'):
							text(tmp)

					with tag('content', src=index):
						pass
					print(tmp)

		order+=1

		with tag('navPoint', replace_with_class='chapter', playOrder=order):
			with tag('navLabel'):
				with tag('text'):
					text('Animals')

			with tag('content', src='Animals.xml'):
				pass

			print(sorted_buffer[2])
			for name,index in sorted_buffer[2]:
				with tag('navPoint', replace_with_class='chapter', playOrder=order):

					tmp=name
					if 'BENIN' in name:
						tmp='The '+name[:-5]
					with tag('navLabel'):
						with tag('text'):
							text(tmp)

					with tag('content', src=index):
						pass

		order+=1

		with tag('navPoint', replace_with_class='chapter', playOrder=order):
			with tag('navLabel'):
				with tag('text'):
					text('Places')
			
			with tag('content', src='Places.xml'):
				pass

			for name,index in sorted_buffer[3]:
				with tag('navPoint', replace_with_class='chapter', playOrder=order):

					tmp=name
					if 'BENIN' in name:
						tmp='The '+name[:-5]
					with tag('navLabel'):
						with tag('text'):
							text(tmp)

					with tag('content', src=index):
						pass

		order+=1

		with tag('navPoint', replace_with_class='chapter', playOrder=order):
			with tag('navLabel'):
				with tag('text'):
					text('Miscellaneous Entries')
			
			with tag('content', src='MiscEntries.xml'):
				pass

			for name,index in sorted_buffer[4]:
				with tag('navPoint', replace_with_class='chapter', playOrder=order):

					tmp=name
					if 'BENIN' in name:
						tmp='The '+name[:-5]
					with tag('navLabel'):
						with tag('text'):
							text(tmp)

					with tag('content', src=index):
						pass

		'''
		import os
		for elem in os.listdir('index_data'):
			with tag('navPoint', replace_with_class='chapter', playOrder=order):
				with tag('navLabel'):
					with tag('text'):
						text('main'+str(order))
				with tag('content', src=elem):
					pass
			order+=1


		order+=1
		'''
result = indent(
	doc.getvalue().replace('replace_with_class','class').replace('replace_with_epub_type','epub:type'),
	indentation = ' '*4,
	newline = '\r'
)

f=codecs.open('fb.ncx','w+',encoding='utf-8')
f.write(result)
f.close()