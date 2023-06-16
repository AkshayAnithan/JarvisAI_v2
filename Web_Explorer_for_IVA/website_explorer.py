import webbrowser
import urllib
import urllib.request

def wikipedia_explorer(data):
	pass

def find_hyperlinks(data):
#objectives of find_hyperlink function
#1. Find all hyperlinks in a website (the html document is passed as string in data variable to this function)
#2.Function returns a python dictionary, where key => link's name(the text acting as links) , value => href value of anchor tag

	links_dict = {}
	link_count = 0

	for x in range(len(data)):
		href_value = ''
		link_name = ''
		
		if data[x] == '<':
			if data[x+1] == 'a':
				x = x+2
				
				#when trying to visit google, string index out of range is shown
				if x == len(data):
					break
					
				while data[x] != '>':
					if data[x] == 'h' and data[x+1] == 'r' and data[x+2] == 'e' and data[x+3] == 'f':	
						#updating link counter, as we found an href link
						link_count += 1
						
						#loop to pass chars until first ' or " after href to find value of href
						while data[x] != '\'' and data[x] != '"':  
							x = x+1
						
						x = x+1
						
						while data[x] != '\'' and data[x] !='"':
							href_value += data[x]
							x = x+1
					x = x+1
				
				if data[x] == '>':
					x = x+1
					
				while data[x] != '<':
					link_name += data[x]
					x = x+1	
			
			#to store the details in a python dict for easy access in program
			links_dict[link_name] = href_value
				

	#printing the links in console
	print('\nNumber of hyperlinks found : '+str(link_count))
		
	return links_dict

	

