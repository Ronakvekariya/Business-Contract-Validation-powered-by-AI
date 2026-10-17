from flair.data import Sentence
from flair.models import SequenceTagger
import os

tagger = SequenceTagger.load("flair/ner-english-ontonotes-large")

# API_URL = os.getenv("HF_API_KEY")
# headers = {"Authorization": os.getenv("HF_TOKEN")}

class Ner:
  def __init__(self, pdfText):
    self.text = pdfText
    self.sentence = ""
    self.output=[]

  def ner(self):
    try:
      print("Starting NER Task.....\n\n")
      # self.output = self.query({
	    # "inputs": f"{self.text}"})

      print("self text is :", self.text)


      self.sentence = Sentence(self.text)
      tagger.predict(self.sentence)
      print("NER performed successfully.")
      print('The following NER tags are found:')

      # print("self.output was : ", self.output)
      
    except Exception as err:
      print(f"Error occurred while reading pdf : {err}")

  def printNER(self):
    
    print('The following NER tags are found:')
    ner_dict = {}
    # iterate over entities and print
    for entity in self.sentence.get_spans('ner'):
      ner_dict[entity.text] = [entity.get_label('ner').value, entity.score]
    
    # print(ner_dict)
    return ner_dict

      
  # @staticmethod
  # def query(payload):
    # response = requests.post(API_URL, headers=headers, json=payload)
    # return response.json()
