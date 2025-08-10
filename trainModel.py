from sampleText import data_train
from utilityFunctions import get_profiles




def trainModel():
   print("Training...")

   profiles=get_profiles(data_train) 
   return profiles

