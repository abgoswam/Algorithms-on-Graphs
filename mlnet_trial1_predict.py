import pandas as pd
import pickle
import mlnet

from IPython.display import display
from mlnet.datasets import get_dataset
from mlnet.feature_extraction.text import NGramFeaturizer
from mlnet.feature_extraction.text.extractor import Ngram
from mlnet.ensemble import LightGbmBinaryClassifier
from mlnet import Pipeline, FileDataStream

# data input (as a FileDataStream)
path = get_dataset('infert').as_filepath()
print(path)

data = FileDataStream.read_csv(path)
print(data.head())

# Loading a TLC model using its zip file
model_tlc = Pipeline(model=r'H:\TLC_DRI_Oct2018\_tmp\1.model.zip')
print(model_tlc.__dict__)

model_tlc.predict(data).head(5)
