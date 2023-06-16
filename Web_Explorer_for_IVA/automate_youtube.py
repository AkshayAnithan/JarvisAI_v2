import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = False
Path = "D:\Akshay\S7\Project\Jarvis 3.0\Database\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = False
Path = "D:\Akshay\S7\Project\Jarvis 3.0\Database\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)


from Body.speak import Speak
from Body.listen import MicExecution
# from Body.print import print

import win32gui
import win32.lib.win32con as win32con

def bring_window_to_front():
    driver = webdriver.Chrome()
    browser_handle = driver.current_window_handle

    # Get the window handle of the Chrome browser
    chrome_handle = win32gui.FindWindow(None, driver.title)

    # Bring the Chrome window to the front
    win32gui.ShowWindow(chrome_handle, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(chrome_handle)

    # Switch back to the Selenium driver window
    driver.switch_to.window(browser_handle)

def activate_youtube_controls(website_url):

	# chrome_options = Options()
	# chrome_options.add_argument('--log-level=3')
	# chrome_options.headless = False
	# Path = "D:\Akshay\S7\Project\Jarvis 3.0\Database\chromedriver.exe"
	# driver = webdriver.Chrome(Path,options=chrome_options)
 
	Speak('Since you are visiting youtube, you can skip the ad, forward, backward, increase, decrease the speed and volume of the video. In short, you can listent to whatever way you like...')
   	
	driver.get(website_url)
    
	# print('Since you are visiting youtube, you can skip the ad, forward, backward, increase, decrease the speed and volume of the video. In short, you can listent to whatever way you like...')
	
    
	#Initialize Firefox driver
	#driver = webdriver.Firefox()
	driver.get(website_url)
	
	#wait for the video player to load
	time.sleep(3)
	
	#finding the video element
	video = ''
	try:
		video = driver.find_element('css selector', 'video.html5-main-video')
		#print('Video variable value: ', video)
		#print('Video element got successfully!')

	except Exception as e:
		#print('Error occured while getting the video element!')
		print(e)
		#sys.exit()
		
	
	print("""
		Entered to Youtube Video Control Section. Just say exit to quit controlling the video!
	""")
	#command = input('Enter what you want to do with video: ')
	Speak('Say what you want to do with video: ')
	command = ''
		
 
	while 'exit' not in command:
		#bring_window_to_front()
		command = MicExecution()
		try:
			if 'pause' in command:
				video.send_keys('k')
				print('Video is now Paused')
				Speak("Video is now Paused")

			elif 'play' in command:
				video.send_keys('k')
				print('Playing the Video')
				Speak("Playing the Video")

			elif 'skip ad' in command:
				skip_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ytp-ad-skip-button')]")))
				skip_button.click()
				print('Ad Skipped')
			
			elif 'forward' in command:
				video.send_keys(Keys.ARROW_RIGHT)
				print('Video is Forwarded')
			
			elif 'backward' in command:
				video.send_keys(Keys.ARROW_LEFT)
				print('Video Backwarded')
			
			elif 'full screen' in command:
				video.send_keys('f')
				print('Full Screen Activated')

			elif 'toggle mute' in command:
				video.send_keys('m')
				print('Audio Muted/unmuted.')
   
			elif 'normal screen' in command:
				video.send_keys('f')
				print('Back to normal screen')

			elif 'increase speed' in command:
				video.send_keys(Keys.SHIFT, '>')
				time.sleep(1)
				print('Video Speed Increased')

			elif 'decrease speed' in command:
				video.send_keys(Keys.SHIFT, '<')
				time.sleep(1)
				print('Video speed decreased')
				
			elif 'increase volume' in command:
				video.send_keys(Keys.ARROW_UP)
				time.sleep(1)
				print('Volume increased')
				
			elif 'decrease volume' in command:
				video.send_keys(Keys.ARROW_DOWN)
				time.sleep(1)
				print('Volume decreased')
			
			else:
				print('Sorry, could not understand your command!')
		
		except Exception as e:
			print(e)
			print('Some error occured while carrying out the execution!')

		#print("Enter what you want to do with the video")
		#command = MicExecution()
		
  		#command = input('Enter what you want to do with video: ')
	
	#print("'Do you want to close youtube video as well? (Just say yes or no): ")
	Speak("'Do you want to close youtube video as well? (Just say yes or no): ")
	choice = MicExecution()
	#want_to_close_yt_video = MicExecution()
 
	if 'yes' in choice:
		driver.quit()


#activate_youtube_controls('https://www.youtube.com/watch?v=wSUDODrYw5U&ab_channel=JustChillin%27')