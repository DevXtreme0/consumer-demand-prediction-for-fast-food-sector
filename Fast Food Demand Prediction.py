#!/usr/bin/env python
# coding: utf-8
import sys
import os

import itertools
import threading
import time

import ctypes

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QComboBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

import numpy as numpyLib
import pandas as pandasLib
from IPython.display import display
from IPython import get_ipython
import datetime
pandasLib.set_option('display.max_columns', None)
import matplotlib.pyplot as pyplot
import seaborn as seanborn
from sklearn.preprocessing import StandardScaler
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
from sklearn.metrics import explained_variance_score
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_log_error

class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle("Consumer Demand Prediction - About Page")
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "aboutView.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)

class HomeViewController(QWidget):
    def __init__(self):
        super(HomeViewController, self).__init__()
        self.load_ui()
        self.setWindowTitle("Consumer Demand Prediction - Prediction Page")


        cb = self.findChild(QComboBox, 'comboBox')
        cb.addItems(['2 Weeks', '4 Weeks', '6 Weeks', '8 Weeks', '10 Weeks'])

        btn = self.findChild(QPushButton, 'predictButton')
        btn.clicked.connect(self.btn_clk)

        btn1 = self.findChild(QPushButton, 'aboutButton')
        btn1.clicked.connect(self.btn_clk1)

        btn2 = self.findChild(QPushButton, 'exitButton')
        btn2.clicked.connect(self.btn_clk2)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "predictionView.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def btn_clk1(self):
        self.w = Window2()
        self.w.show()

    def btn_clk2(self):
        sys.exit()

    def btn_clk(self):
        centerInfo = self.findChild(QLineEdit, 'centreInfoLineEdit')
        mealBevInfo = self.findChild(QLineEdit, 'mealBevInfoLineEdit')
        testInfo = self.findChild(QLineEdit, 'testInfoLineEdit')
        trainInfo = self.findChild(QLineEdit, 'trainInfoLineEdit')
        demandStatisticsLocation = self.findChild(QLineEdit, 'statisticsStoreLocation')

        warnings.filterwarnings('ignore')

        learnFromTrainData = pandasLib.read_csv(trainInfo.text())
        centerInformation = pandasLib.read_csv(centerInfo.text())
        mealInformation = pandasLib.read_csv(mealBevInfo.text())
        testInformation = pandasLib.read_csv(testInfo.text())

        combo = self.findChild(QComboBox, 'comboBox')
        predictionTimePeriod = 000

        if combo.currentText() == '2 Weeks':

         predictionTimePeriod = 148

        elif combo.currentText() == '4 Weeks':

         predictionTimePeriod = 150

        elif combo.currentText() == '6 Weeks':

         predictionTimePeriod = 152

        elif combo.currentText() == '8 Weeks':

         predictionTimePeriod = 154

        elif combo.currentText() == '10 Weeks':

         predictionTimePeriod = 156

        else:
         exit()
         #predictionTimePeriod = 156

        done = False

        def animate():
            for c in itertools.cycle(["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]):
                if done:
                    break
                #sys.stdout.write('\rloading ' + c)
                ctypes.windll.user32.MessageBoxW(0, 'Prediction Calculating, Please wait!' + "\r"+"Progressing..."+c, "Calculation Commenced on", 0)
                sys.stdout.flush()
                time.sleep(0.1)
            #sys.stdout.write('\rDone!     ')
            #ctypes.windll.user32.MessageBoxW(0, 'Thank You for Your Patience. Results Available Now', "Calculation Finished", 0)

        t = threading.Thread(target=animate)
        t.start()

# Data Preprocessing
# Output counted Rows and Columns (Rows,Colmns)
        print("Shape of train information dataset :", learnFromTrainData.shape)
        learnFromTrainData.info()
        print("Shape of center information dataset :", centerInformation.shape)
        centerInformation.info()
        print("Shape of meal information dataset :", mealInformation.shape)
        mealInformation.info()
        print("Shape of test information dataset :", testInformation.shape)
        testInformation.info()
# Return top "n" of a data
        learnFromTrainData.head()

        testInformation['num_orders']=123456

# Return top "n" of a data
        testInformation.head()
        centerInformation.head()
        mealInformation.head()

# Validate to return dataframe
        learnFromTrainData = pandasLib.concat([learnFromTrainData, testInformation], axis=0)

# Merging data to defined configurations
        learnFromTrainData = learnFromTrainData.merge(centerInformation, on='center_id', how='left')
        learnFromTrainData = learnFromTrainData.merge(mealInformation, on='meal_id', how='left')

# Return top "n" of a data and returns the sum
        learnFromTrainData.head()
        learnFromTrainData.isnull().sum()

##Deriving New Features

# Special Price
        learnFromTrainData['special price'] = learnFromTrainData['base_price'] - learnFromTrainData['checkout_price']

# Special Price Percent
        learnFromTrainData['special price percent'] = ((learnFromTrainData['base_price'] - learnFromTrainData['checkout_price']) / learnFromTrainData['base_price']) * 100

# Special Price T/F
        learnFromTrainData['special price t/f'] = [1 if x > 0 else 0 for x in (learnFromTrainData['base_price'] - learnFromTrainData['checkout_price'])]
        learnFromTrainData = learnFromTrainData.sort_values(['center_id', 'meal_id', 'week']).reset_index()

# Weekly Price Comparison
        learnFromTrainData['weekly_price_comparison'] = learnFromTrainData['checkout_price'] - learnFromTrainData['checkout_price'].shift(1)
        learnFromTrainData['weekly_price_comparison'][learnFromTrainData['week'] == 1] = 0
        learnFromTrainData = learnFromTrainData.sort_values(by='index').reset_index().drop(['level_0', 'index'], axis=1)

# Weekly Price Comparison T/F
        learnFromTrainData['weekly_price_comparison t/f'] = [1 if x > 0 else 0 for x in learnFromTrainData['weekly_price_comparison']]
        learnFromTrainData.head()
        learnFromTrainData.isnull().sum()

        trainStart = datetime.datetime.now()

        trainData = learnFromTrainData[learnFromTrainData['week'].isin(range(1, 146))]

# Copying to DataFrame
        dataFrameFromTrainData = learnFromTrainData.copy()
# Return top n (5 by default) rows of a data frame
        dataFrameFromTrainData.head()

# Encoding all the categorical features
        dataFrameFromTrainData['center_id'] = dataFrameFromTrainData['center_id'].astype('object')
        dataFrameFromTrainData['meal_id'] = dataFrameFromTrainData['meal_id'].astype('object')
#dataFrameFromTrainData['region_code'] = dataFrameFromTrainData['region_code'].astype('object')

        dataTypeOne = dataFrameFromTrainData[['center_id', 'meal_id', 'center_type', 'category', 'cuisine']]
        dataTypeTwo = dataFrameFromTrainData.drop(['center_id', 'meal_id', 'center_type', 'category', 'cuisine'], axis=1)

# Drop one dimension from the representation to avoid dependency among the variables and convert
        dummyVar = pandasLib.get_dummies(dataTypeOne, drop_first=True)

# Merge DataFrames by indexes
        dataFrameFromTrainData = pandasLib.concat([dataTypeTwo, dummyVar], axis=1)
        dataFrameFromTrainData.head()

# Returns the absolute value of data frame num_orders
        abs(trainData.corr()['num_orders']).sort_values(ascending=False)

        standardScaler = StandardScaler()
        dataTypeOne = dataFrameFromTrainData.drop(['checkout_price', 'base_price', 'special price', 'special price percent', 'weekly_price_comparison'], axis=1)
        dataTypeTwo = dataFrameFromTrainData[['checkout_price', 'base_price', 'special price', 'special price percent', 'weekly_price_comparison']]

# Data standardization
        standardizationData = pandasLib.DataFrame(standardScaler.fit_transform(dataTypeTwo), columns=dataTypeTwo.columns)
        concatData = pandasLib.concat([standardizationData, dataTypeOne], axis=1)

# Copy modified dataframe to concatDataFrame variable
        concatDataFrame = concatData.copy()

# Categorizing weeks to quarters
        concatDataFrame['Quarter'] = (concatData['week'] / 13).astype('int64')
        concatDataFrame['Quarter'] = concatDataFrame['Quarter'].map({0: 'Q1', 1: 'Q2', 2: 'Q3', 3: 'Q4', 4: 'Q1', 5: 'Q2', 6: 'Q3', 7: 'Q4', 8: 'Q1',
                                                             9: 'Q2', 10: 'Q3', 11: 'Q4'})
# Returns object containing counts of unique values in quarter
        concatDataFrame['Quarter'].value_counts()

# Categorizing weeks to years
        concatDataFrame['Year'] = (concatData['week'] / 52).astype('int64')
        concatDataFrame['Year'] = concatDataFrame['Year'].map({0: 'Y1', 1: 'Y2', 2: 'Y3'})

        dataPartOne = concatDataFrame[['Quarter', 'Year']]
        dataPartTwo = concatDataFrame.drop(['Quarter', 'Year'], axis=1)

# Drop one dimension from the representation to avoid dependency among the variables and convert
        dummyVar = pandasLib.get_dummies(dataPartOne, drop_first=True)
        dummyVar.head()

        concatDataFrame = pandasLib.concat([dataPartTwo, dummyVar], axis=1)
        concatDataFrame.head()

# Applying log transformation on the target feature
        concatDataFrame['num_orders'] = numpyLib.log1p(concatDataFrame['num_orders'])
        trainData = concatDataFrame[concatDataFrame['week'].isin(range(1, 146))]

# Detection for outliers
        def displayOutliersResult(dataColumn):
            calculateQuarterThree = round(trainData[dataColumn].quantile(0.75), 6)
            calculateQuarterOne = round(trainData[dataColumn].quantile(0.25), 6)
    # using interquartile range method
            interquartileRange = calculateQuarterThree - calculateQuarterOne
            lowerRange = calculateQuarterOne - (3 * interquartileRange)
            upperRange = calculateQuarterThree + (3 * interquartileRange)
            upperOutlier = trainData[trainData[dataColumn] > upperRange].shape[0]
            lowerOutlier = trainData[trainData[dataColumn] < lowerRange].shape[0]

            print('---Outliers Detection Result---')
            print('Upper Outliers :', upperOutlier)
            print('Lower Outliers :', lowerOutlier)
            print('Outliers(%):', ((upperOutlier + lowerOutlier) / trainData.shape[0]) * 100)

            displayOutliersResult('num_orders')
        concatDataFrame.head()

        testDataAnalysis = learnFromTrainData[learnFromTrainData['week'].isin(range(146, predictionTimePeriod))]


# Real Prediction for next defined weeks
        trainData = concatDataFrame[concatDataFrame['week'].isin(range(1, 146))]
        testData = concatDataFrame[concatDataFrame['week'].isin(range(146, predictionTimePeriod))]


        X_train = trainData.drop(['id', 'num_orders', 'week', 'special price', 'city_code', 'special price percent'],
                                 axis=1)
        y_train = trainData['num_orders']

        X_test = testData.drop(['id', 'num_orders', 'week', 'special price', 'city_code', 'special price percent'],
                               axis=1)
        y_test = testData['num_orders']

        CGB = CatBoostRegressor(learning_rate=0.3, loss_function='RMSE', max_depth=9, verbose=False)

        CGB.fit(X_train, y_train)

# Gets training time for the executed code
        trainingTime = datetime.datetime.now() - trainStart

 # Set prediction time for the executed code
        predictStart = datetime.datetime.now()

        CGBpred = CGB.predict(X_test)

# Gets prediction time for the executed code
        predictionTime = datetime.datetime.now() - predictStart

        done = True
        if done == True:
         ctypes.windll.user32.MessageBoxW(0, 'Thank You for Your Patience. Results Available Now', "Calculation Finished", 0)
# Train Time
        print("Training Time (HH:MM:SS:NS) ", trainingTime)
# Prediction Time
        print("Prediction Time (HH:MM:SS:NS)", predictionTime)

        predictedDemandResult = pandasLib.DataFrame(CGBpred)
        predictedDemandResult = numpyLib.expm1(predictedDemandResult).astype('int64')
        dataFile = pandasLib.DataFrame(columns=['id', 'num_orders', 'week'])

        dataFile['id'] = testData['id']
        dataFile['num_orders'] = predictedDemandResult.values
        dataFile['week'] = testData['week']

        pyplot.figureSize = pyplot.figure(figsize=(12, 7))
        seanborn.set_style("whitegrid")
        pyplot.title('Pattern of Predicted Demand', fontdict={'fontsize': 14})
        seanborn.pointplot(x=dataFile.groupby('week').sum().reset_index()['week'],
                           y=dataFile.groupby('week').sum().reset_index()['num_orders'], color='green')
        #seanborn.pointplot(x="week", y="num_orders", color='green', data=dataFile)
        pyplot.ylabel('Number of Orders', fontdict={'fontsize': 12})
        pyplot.xlabel('Week', fontdict={'fontsize': 12})
        pyplot.ticklabel_format(style='plain', axis='y')
        pyplot.tight_layout()
        pyplot.tick_params('y', gridOn = True, grid_alpha = 0.6, zorder=0)
        pyplot.tick_params('x', gridOn = True, grid_alpha = 0.6, zorder=0)
        seanborn.despine(bottom=True, left=True)

        predictedDemandResult = pandasLib.DataFrame(CGBpred)

        predictedDemandResult = numpyLib.expm1(predictedDemandResult).astype('int64')

        dataFile = pandasLib.DataFrame(columns=['id','num_orders','week','city_code','center_id','meal_id','checkout_price','base_price'])

        dataFile['id'] = testData['id']
        dataFile['num_orders'] = predictedDemandResult.values
        dataFile['week'] = testData['week']
        dataFile['city_code'] = testDataAnalysis['city_code']
        dataFile['center_id'] = testDataAnalysis['center_id']
        dataFile['meal_id'] = testDataAnalysis['meal_id']
        dataFile['checkout_price'] = testDataAnalysis['checkout_price']
        dataFile['base_price'] = testDataAnalysis['base_price']

        #dataFile.to_csv('Predicted Demand Result.csv', index=False)

        dataFile.head()

        pyplot.show()

        from subprocess import Popen
        #Popen('Predicted Demand Result.csv', shell=True)

        try:
            #myfile = open("myfile.csv", "r+")  # or "a+", whatever you need
            myfile = dataFile.to_csv('Predicted Demand Result.csv', index=False)
            myfile = Popen('Predicted Demand Result.csv', shell=True)

        except IOError:

            ctypes.windll.user32.MessageBoxW(0, 'Could not generate the file and open the file. Please close the opened excel file',
                                             "Running Excel File Detected", 0)

        with myfile:

            dataFile.to_csv('Predicted Demand Result.csv', index=False)
            Popen('Predicted Demand Result.csv', shell=True)



if __name__ == "__main__":
    app = QApplication([])
    widget = HomeViewController()
    widget.show()

    sys.exit(app.exec_())