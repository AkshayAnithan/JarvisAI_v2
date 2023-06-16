from chunkSR import *

choice = "yes"

while choice == "yes":
    link = input("Website Link: ")
    start_chunkSR(link)
    choice = input("Rerun the program? ")