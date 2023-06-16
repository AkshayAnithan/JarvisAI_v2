import face_recognition
import os, sys
import cv2
import numpy as np
import math
import pyttsx3

# Create a TTS engine
engine = pyttsx3.init()

# Set the voice rate and volume
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

#engine.say("welcome")
#engine.runAndWait()
