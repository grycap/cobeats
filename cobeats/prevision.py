from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import pandas as pd

class prevision:

	name=""
	yhat=0
	s=pd.Series()
	#m=1
	def __init__(self,name):
		self.name=name
		yhat=0
		
	def add(self,value):
		self.s.loc[self.s.count()] = value
	def calculate(self):
		#if self.s.count()>20:
		try:
			model = ARIMA(self.s, order=(5,1,0))
			model_fit = model.fit(disp=0)
			#model_fit = model.fit(model='bfgs')
			output = model_fit.forecast()
			self.yhat = output[0]
			print (self.yhat)
			prev=self.yhat
		except :
			print("CALC")
			prev=self.s[self.s.count()-1]
		return prev


	def print(self):
		#print(self.name)
		print(self.s)
		print(self.s.count())
		print(self.yhat)
