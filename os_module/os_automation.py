import os
import random 
from Body.speak import Speak
from Body.listen import MicExecution

def list_files_in_directory():
    
    files = os.listdir()
    if files:
        file_list = []
        for file in files:
            file_list.append(file)
        file_list = ', '.join(file_list)
            
        Speak("Files in the current directory are:")
        Speak(file_list)
        
    else:
        Speak("The current directory is empty.")

def make_file(filename):
    try:
        with open(filename, 'w'):
            Speak(f"File '{filename}' created successfully.")
    except OSError:
        Speak(f"Failed to create file '{filename}'.")

def make_directory(directory_name):
    try:
        os.mkdir(directory_name)
        Speak(f"Directory '{directory_name}' created successfully.")
    except OSError:
        Speak(f"Failed to create directory '{directory_name}'.")

def delete_file(filename):
    try:
        os.remove(filename)
        Speak(f"File '{filename}' deleted successfully.")
    except OSError:
        Speak(f"Failed to delete file '{filename}'.")

def delete_file_in_directory(directory, filename):
    try:
        os.remove(os.path.join(directory, filename))
        Speak(f"File '{filename}' deleted successfully from directory '{directory}'.")
    except OSError:
        Speak(f"Failed to delete file '{filename}' from directory '{directory}'.")


def change_the_directory(directory):
    try:
        os.chdir(directory)
    except OSError:
        Speak('Directory changed to '+str(directory))
        
def process_command(command):
    if "list files" in command:
        list_files_in_directory()
        
    elif "make file" in command or "create file" in command:
        filename = command.split("called")[1].strip()
        make_file(filename)
        
    elif "make directory" in command or "create directory" in command:
        directory_name = command.split("named")[1].strip()
        make_directory(directory_name)
        
    elif "delete file" in command:
        filename = command.split("called")[1].strip()
        delete_file(filename)
        
    elif "delete file in directory" in command:
        directory = command.split("directory")[1].split("called")[0].strip()
        filename = command.split("called")[1].strip()
        delete_file_in_directory(directory, filename)
        
    elif "change directory" in command:
        directory = command.split("directory")[1].split("called")[0].strip()
        change_the_directory(directory)
        
    else:
        Speak("Command not recognized.")

# Main program loop

def initaite_os_module():
    
    Speak('Entering into OS operations...')
    Speak('You can now create, delete, list files and folders')
    
    commands = [
        'What you want to do: ',
        'Say the operation to do: ',
    ]
    
    
    while True:
        
        prompt = random.choice(commands)
       
        #uncomment below line in actual implementation process, for testing this, I am skipping MicExecution
        #command = MicExecution()
        command = input('Enter the OS commands: ')

        if "exit" in command:
            Speak("Exiting the OS section...")
            break
        process_command(command)
