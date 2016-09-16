print('Starting JSON parsing')

import json
from pprint import pprint

import codecs

f=codecs.open('input.json','r',encoding='utf-8')
input=f.read()
f.close()

true_input=json.loads(input)
# pprint(true_input)

print(true_input['_default']['3']['type'])

# for elem in true_input['_default']:
# 	tag=true_input['_default'][elem]['type']
# 	if tag not in ['Misc','place','object','person','animals']:
# 		print(tag)

#OK we have them sorted into FIVE categories. 
#We need to create title pages for them, then
#sort the inputs into them. That is done in the manifest

#Ok so the moral is it doesn't matter

#Misc,place,object,person,animals

# for elem in true_input['_default']:
	# tag=true_input['_default'][elem]['type']
	# if tag in ['Misc','place','object','person','animals']:
		# content=true_input['_default'][elem]['content'])
		# print(true_input['_default'][elem]['content1'])


from yattag import Doc, indent

num=0

for elem in true_input['_default']:

	#reparses differenly each time

	article_name=''
	content=''
	JKR_thoughts=''
	type=''
	link=''

	try:
		article_name=true_input['_default'][elem]['article_name']
	except:
		pass

	try:
		content=true_input['_default'][elem]['content']
	except:
		pass

	try:
		JKR_thoughts=true_input['_default'][elem]['JKR_thoughts']
	except:
		pass

	try:
		type=true_input['_default'][elem]['type']
	except:
		pass

	try:
		link=true_input['_default'][elem]['Pottermore_link']
	except:
		pass

	#need to split the content apart
	content=content.split('\n')
	content=list(filter(None, content))
	print(content)

	JKR_thoughts=JKR_thoughts.split('\n')
	JKR_thoughts=list(filter(None, JKR_thoughts))
	print(JKR_thoughts)

	print('Article Name',article_name)
	print('Content',content)
	print('JKR_thoughts',JKR_thoughts)
	print('Category',type)
	print('Link',link)

	doc, tag, text = Doc().tagtext()

	doc.asis(r'<?xml version="1.0" encoding="UTF-8"?>')

	with tag('html'):
		doc.asis(
			'<head>',
			'	<title>Pottermore - an Archive</title>',
			r'	<link rel="stylesheet" href="css/main.css" type="text/css"/>',
			r'	<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8"/>',
			'</head>',
		)
		with tag('body', category=type):
			with tag('div', replace_with_class='body'):
				with tag('div', id='chapter_2600', replace_with_class='chapter'):
				
					with tag('h1', style='text-align: center; line-height: 1.7;'):
						text(article_name)

					with tag('p'):
						text('   ')

					with tag('div', replace_with_class='text', category=type):
				

						#content
						for elem in content:
							with tag('p'):
								text(elem)

						#JKR's thoughts
						if len(JKR_thoughts) > 0:
							with tag('h3'):
								text('JKR\'s thoughts')

						for elem in JKR_thoughts:
							with tag('p'):
								text(elem)

						if link != 'no_link':
							with tag('p'):
								text('---')

							with tag('a', href=link):
								with tag('p'):
									text('Pottermore Link')


	result = indent(
		doc.getvalue().replace('replace_with_class','class').replace('replace_with_epub_type','epub:type'),
		indentation = ' '*4,
		newline = '\r'
	)

	f=codecs.open('in/main'+str(num)+'.xml','w+',encoding='utf-8')
	f.write(result)
	f.close()

	# f=codecs.open('main'+str(num)+'.html','w+',encoding='utf-8')
	# f.write(result)
	# f.close()

	num+=1

	# break
