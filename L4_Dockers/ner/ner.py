import requests
import os

API_URL = os.getenv("HF_API_KEY")
headers = {"Authorization": os.getenv("HF_TOKEN")}

class Ner:
  def __init__(self, pdfText):
    self.text = pdfText
    self.sentence = ""
    self.output=[]

  def ner(self):
    try:
      print("Starting NER Task.....\n\n")
      self.output = self.query({
	    "inputs": f"{self.text}"})
      
      print("NER performed successfully.")

      # print("self.output was : ", self.output)
      
    except Exception as err:
      print(f"Error occurred while reading pdf : {err}")

  def printNER(self):
    
    # print('The following NER tags are found:')
    ner_dict = {}
    for dicts in self.output:
      ner_dict[dicts["word"]] = [dicts["entity_group"], dicts["score"]]
    
    # print(ner_dict)
    hashable_ner_dict = tuple(ner_dict.items())
    return ner_dict

      
  @staticmethod
  def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
