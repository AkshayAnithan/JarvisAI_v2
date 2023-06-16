import webbrowser
import requests

from googlesearch import search
import random

from Web_Explorer_for_IVA.website_explorer import find_hyperlinks
from Web_Explorer_for_IVA.website_explorer import wikipedia_explorer

from Web_Explorer_for_IVA.automate_youtube import activate_youtube_controls


from Body.speak import Speak
from Body.listen import MicExecution

from ScreenReader.chunkSR import start_chunkSR


def extract_domain_name(website_url):

	website_domain = ''
	for x in range(len(website_url)):
		if website_url[x] == 'h' and website_url[x+1] == 't' and website_url[x+2] == 't' and website_url[x+3] == 'p':
			
			while True:
				if website_url[x] == '/':
					if website_url[x+1] == '/':
						break	
				x = x+1
			
			x = x+2
			
			while website_url[x] != '/':
				website_domain += website_url[x]
				x = x+1
			break
	return website_domain
				

def initiate_web_explorer():

	Speak('Entering into web exploration module. I will guide you in this ocean of web...')

	while True:
		command_contains_goto_visit = 0
  
		#uncomment this for actual working, commented this to check other parts of the program
		#Speak('What you want to do in the web, sir? ')
		#query = MicExecution()
  
		ask = [
			"What can I help you find online, sir?",
			"How can I assist you in searching the web, sir?",
			"What are you looking to explore on the internet, sir?",
			"What kind of information are you seeking, sir?",
			"How may I assist you with your web search, sir?",
			"What specific topic or query would you like me to look up for you, sir?"
		]
  
		Speak(random.choice(ask))
		query = MicExecution()
		#query = input('What would you like to do searching the web, sir? ')
  
		try:
		
			if 'exit' in query:
				break
			
			search_results = search(query, tld = 'co.in', num=10, stop=10, pause=2)
			

			#since search_results is a 'generator' datatype, we have to use an iterator to access it's elements.
			#So the below loop is for accessing the first element only
			website_url = ''
			
			
			for x in search_results:
				website_url = x
				break
				
				
			#to extract domain name from website url	
			website_domain = extract_domain_name(website_url)
			#Speak('Domain name of the website is: ', website_domain)
			Speak('The title of the webpage we are visiting is ' + str(website_domain))
			
			if website_domain == 'www.youtube.com':
				activate_youtube_controls(website_url)
				continue
					
				
			website_name = website_url	
			
			#Speak('Visting  '+website_url)
			
			try:
				response = requests.get(website_url) #for getting status codes, html document of the page etc. 
				webbrowser.open_new_tab(website_url)  #to open the site in a new tab
			
			except Exception as e:
				Speak('Some error occured while getting the web page. Try going to the site once more or another website...')
				#Speak(e)
					
			if response.status_code == 200:
       
				
				#Speak('Url successfully visited...')
				data = str(response.text)
				
				#to write the html contents to file named '[destination_name].txt'
				#web_file = open('explored_sites/'+website_name+'.txt', 'w')
				#web_file.write(str(data))
				#web_file.close()
				  
				#for test purposes
				#sample_file = open('sample_website.txt', 'r')
				#sample_file.seek(0)
				#data = sample_file.read()
				
				links_dict = {}
				
				links_dict = find_hyperlinks(data)
						
				link_file = open('explored_sites/current_links.txt', 'w')
						
				count = 0
				for key in links_dict:
					count = count + 1
					link_file.write(str(count)+'. '+key+'  ->  '+links_dict[key]+'\n')
				
				#Speak('\nWe found these hyperlinks in the website...\n ')
				count = 0
				for key in links_dict:
					count = count + 1
     
					#need to change below code. Should use Arjun's BeautifulSoup to extract domain and then show it
					if count < 5:
						break
					Speak(str(count)+'. '+key+': '+links_dict[key]+'\n')
    
					
     
				##Including Arjun's Chuckify
				want_summary = input('Do you want to the summary of the web page? Just say \'yes\' if you want it: ')
    
				if want_summary.lower() == 'yes':
					summary = start_chunkSR(website_url)
					Speak('Summary is: ', summary)
     
     
				#To goto one of the links
				while True:
					Speak('Do you want to goto a link or not? Just say yes or no: ')
					#uncomment below code for final execution ppt
					#status = MicExecution()
     
					status = input('Enter you choice: ')
     
					if status.lower() == 'no':
						break
				
					else:
						try:
							Speak('Just say the link number you wish to goto')
       
							#number = MicExecution()
							#number = int(number)
							number = int(input('Enter or tell the link number: '))
						
							count = 1
							for key in links_dict:
								if count == number:
									Speak('Visiting ',key,'...\n')
									webbrowser.open_new_tab(links_dict[key])
									
									break
								count = count + 1
							break
						
						except Exception as e:
							Speak('Oops. There is no such link number...')
					
				else:
					Speak('Url parsing unsuccessful..')

		except Exception as e:
			#Speak(e)
			Speak("Some unknown error occured sir. The server of the website might be down. Try visiting another website sir...")

	Speak('Exiting the web module...')

