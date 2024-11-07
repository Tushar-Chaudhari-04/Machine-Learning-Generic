import sys
import os
import pickle

from src.logger import logging
from src.exception import CustomException

def save_object(file_path,obj):
   try:
      dir_path=os.path.dirname(file_path)

      os.makedirs(dir_path,exist_ok=True)

      with open(file_path,"wb") as file_obj:
         pickle.dump(obj,file_obj)
      
      logging.info("File is saved successfully...")
      
   except Exception as e:
      logging.info("Exception in obj saving in utils.py",e)
      raise CustomException(e,sys)
   

