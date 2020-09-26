# Fast Food Demand Predciton
<p> A computer system which can predict consumer demand for fast food sector. </p>

<p color = "red"> Note: This solution developed using the scratch level of python language usage. The aim is to achieve higher accuracy as much as possible in consumer demand statistics prediction in the fast-food sector. Overall goal of this application not succeeded 100%. But able to achieve closer accuracywhen camparing with the actual data.</p>

<h3>Description</h3>
<p>
Lack of fast food fulfillment to the consumer, excesses of fast food over the estimated demand, and business loss profit cause by inaccurate demand prediction are common nowadays in fast food centers and fast food base businesses(based on local context - Sri Lanka). Therefore, proposes a solution to avoid this problem by predicting consumer demand for the fast-food sector. Used a forecasting algorithm known as CatBoost with a data categorization technique. Fast food demand is affected by several independent variables such as seasonality, trend, price fluctuation, and length of historical data. A combination of these selected variables was used to calculate demand prediction using parameter tuning in the CatBoost algorithm and other algorithms (slightly different but the same domain) used for the experiment (Such as Linear Regression, LGBM, and XGBoost). However, CatBoost was the best performing model that was selected. Therefore, windows based standalone solution was developed to yield fast-food demand prediction statistics.</p>

<h3>Link to the application demonstration video</h3> 
https://youtu.be/qMAt5fyCOyQ

<h3>Explanation of the proposed solution</h3>

<h4> Dataset Selection and configuration to the system </h4>

<p>
Dataset derived from the Kaggle (https://www.kaggle.com/ghoshsaptarshi/av-genpact-hack-dec2018).
One dataset is a combination of three single information files. One file consists of historical demand information for each center, another file consists of data center information and another file consist of meal information. Additional file related to test information also used for the demand prediction through the final solution.
</p>

<h6>1. Historical demand information file – trainForLearnInformation.csv </h6>
<p>Consist with the historical information of demand for each center. Defined variables listed with brief description in below,</p>
<li>
<ol>•base_price: - Average price of the meal</ol>
<ol>•checkout_price: - Sold price of the meal</ol>
<ol>•meal_id: - Id of the meal</ol>
<ol>•center_id: - Id of the meal center</ol>
<ol>•week: - Week number of the sold meal</ol>
<ol>•id: - Id of the record</ol>
<ol>•emailer_for_promotion: - Removed this variable from the implementation usage </ol>
<ol>•homepage_featured: - Removed this variable from the implementation usage</ol>
<ol>•num_orders: - Demand for the meal</ol>
</li>

<h6>2. Historical center information file – centerInformation.csv</h6>
<p>Consist historical data for each center. Defined variables listed with brief description in below,</p>
<li>
<ol>•center_id: - Id of the meal center</ol>
<ol>•city_code: - Code of the center located city </ol>
<ol>•region_code: - Removed this variable from the implantation usage </ol>
<ol>•center_type: - Centre type </ol>
<ol>•op_area: - Removed this variable from the implementation usage</ol> 
</li>	

<h6>3. Historical meal information file – mealInformation.csv</h6>
<p>Consist historical data of meal information. Defined variables listed with brief description in below,</p>
<li>
<ol>•meal_id: - Specific Id for the meal</ol>
<ol>•category: - Categorized name for the meal</ol>
<ol>•cuisine: - Type of the cuisine for the meal</ol>
</li>

<h6>4. Test Information file data from 146th week to 155th week – testInformation.csv</h6>
<p>Consist with test data for model validation purpose. Same variables included as mentioned in the Historical demand information file (trainForLearnInformation file) except for target variable “num_orders”.</p>

<h4> Use of data preprocessing from the extracted information </h4>

<p>
When user input files to the system, all information on the submitted files merged into a separate one dataset. Therefore, not having null values or missing values is compulsory. After this validation prediction process will initiate. Therefore, merging information is required to be validated. As an example, when merging files “trainForLearnInformation” file specific variable name and its contents should be matched to the same name and contents in the other file. Such as trainToLearn file “meal_id” should match in the mealInfromation file “meal_id” variable. Figure 1 shows how this achieved step by step below,
 </p>
 

 <img style="display:block;text-align:center" src="Data preprocessing code.PNG" alt="Data preprocessing code" >
 <figcaption> Figure 1. Data preprocessing code </figcaption>


<h4> Use of exploratory data analysis for the dataset</h4>

<p>
This is a process, performing initial investigation on data. Such as identify patterns, identify anomalies, test hypothesis and validate assumptions with the help of graphical statistics representation or statistical information. Beginning of the exploratory data analysis process, it is compulsory to identify and remove unnecessary variables that are not contributing to the prediction process. Therefore, four variables were removed. Such as region_code, op_area, emailer_for_promotion and homepage_featured. emailer_for_promotion and homepage_featured column with data were dropped by updating the file. However, region_code, op_area kept in the dataset for identifying its necessity for the implementation. Information regarding the number of entries for each variable and their data types in each data files shown below,
</p>
 
<img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
<figcaption>Figure 2. Train information dataset contents</figcaption>
<br></br>	 
<img style="display:block;text-align:center" src="Center information dataset contents.PNG" alt="Center information dataset contents" >   
<figcaption>Figure 3. Center information dataset contents</figcaption>
<br></br>
<img style="display:block;text-align:center" src="Meal information dataset contents.PNG" alt="Meal information dataset contents" > 
<figcaption>Figure 4. Meal information dataset contents</figcaption>
<br></br>
<img style="display:block;text-align:center" src="Test information dataset contents.PNG" alt="Test information dataset contents" >
<figcaption>Figure 5. Test information dataset contents</figcaption>
<br></br>

<p>
The next process of the exploratory data analysis is to standardization of features that are  used for the demand prediction process. Standardization is a technique used to change the values of numeric columns in the dataset to a common scale, without altering differences in the ranges of values. standardization of the created features is necessary due to the accuracy of the model is not acceptable and high deviation of the values was observed during the implementation. Sample of the standardized dataset shown in figure 6 below,
</p>

<img style="display:block;text-align:center" src="Sample of standardized dataset.PNG" alt="Sample of standardized dataset" >
<figcaption>Figure 6. Sample of standardized dataset</figcaption>

<p>
The final process of the exploratory data analysis is to identify the correlation of each variable. Correlation is a statistical technique that represents relationships of variables between each other. There are three methods available to calculate the correlation. Such as Pearson correlation coefficient, Kendall rank correlation coefficient and Spearman's rank correlation coefficient. Pearson correlation coefficient was chosen since it is widely used and most suited for this study. Generated heatmap of pairwise calculation with the use of Pearson correlation coefficient method shows in figure 7 below,
</p>
 
<img style="display:block;text-align:center" src="Generated heatmap for identify variable correlation.png" alt="Generated heatmap for identify variable correlation" > 
<figcaption>Figure 7. Generated heatmap for identify variable correlation</figcaption>

<p>
According to the above figure 7 above, it is possible to identify “base_price” and “checkout_price” highly correlated variables with each other. Therefore, using these variables might be enough to create final model. But before adding to the final model it was decided to validate with “num_orders” variable. Therefore, it was decided to subtract “base_price” variable value from “checkout_price” variable value and store result as special price. After special price calculation, relationship between “num_orders” variable and special price variable displayed in the scatterplot as shown in figure 11,
</p> 

<img style="display:block;text-align:center" src="Scatter plot for observe relationship of selected variables.png" alt="Scatter plot for observe relationship of selected variables" >
<figcaption>Figure 8. Scatter plot for observe relationship of selected variables</figcaption>

<p>
However, according to the above figure 8, it was observed that relationship between each variable is non-linear and not good correlation for final model. Therefore, it was decided to focus on other techniques rather than depending on specific variable selection according to linearity and correlation. 
</p>

<h4> Use of feature engineering from the extracted information</h4>

<p>
This is a method to create features according to the domain knowledge that enables to enhance performance and accuracy of the machine learning models using dataset. Therefore, below table clarify about the features that is used for model creation from the available dataset,
</p>

<table>
<tr>
<th>Created Feature</th>
<th>Feature Description</th>
</tr>
<tr>	
<td>Special Price</td>
<td>Price defined by subtracting “checkout_price” variable by “base_price” variable.</td>
</tr>
<tr>
<td>Special Price Percent</td>	
<td>Percentage of the special price.</td>
</tr>
<tr>
<td>Special Price T/F</td>
<td>Defines special price included or not. If special price is true, then value will be -1 if special price is false, then value will be 0.</td>
</tr>
<tr>
<td>Weekly Price Comparison</td>
<td>This is a price comparison of the selected weeks about rise or fall of the meal for a specific each center.</td>
</tr>
<tr>
<td>Weekly Price Comparison T/F</td>
<td>Defines price comparison increased or not. If increase true, then value will be -1 if it is false, then value will be 0.</td>
</tr>
<tr>
<td>Year</td>
<td>This defined according to the dataset, number of weeks.</td>
</tr>
<tr>
<td>Quarter</td>
<td>According to the dataset, number of weeks defines as one-fourth of a year.</td>
</tr>
</table>
	
<h4>Use of data transformation for eliminate outliers</h4>

<p>
In the demand prediction context, it is compulsory to outlier data to be 0% on targeted variable called “num_orders”. Therefore, this necessity achieved by using Interquartile range method. Log transformation is the most popular among the different types of transformations used to transform skewed data to approximately conform to normality in feature engineering. Therefore, in the target variable called “num_orders” is not aligned with normality and non-use of transformation methods will reduce performance of the data model. Therefore, it was decided to include log transformation on targeted variable “num_orders”. Which is data approximately conform to normality. Implementation of it shown in figure 9 below,
</p>

<img style="display:block;text-align:center" src="Outlier detection code.PNG" alt="Outlier detection code" >
<figcaption>Figure 9. Outlier detection code</figcaption>

<h4>  Elaboration of used ML algorithms for demand prediction </h4>

<p>
Multiple data modeled using gradient boosting algorithms (such as XGBoost, LightGBM and CatBoost) and linear regression algorithm. Those algorithms implemented with feature extraction, data transformation and data preprocessing for achieve better accuracy on predicted result.  Therefore, in this section only elaborate way of algorithm implementation.
</p>

<img style="display:block;text-align:center" src="Get data through DataFrame.PNG" alt="Get data through DataFrame" >
<figcaption>Figure 10. Get data through DataFrame</figcaption>

<p>
After above process, it was decided to encode categorical features and manipulate data received through above process to data standardization as shown in the figure 11 below, Reason for using “astype” method is to convert column data to object type. Which is helps to reduce usage of memory space. 
</p> 

<img style="display:block;text-align:center" src="Encoding categorical features.PNG" alt="Encoding categorical features" >
<figcaption>Figure 11. Encoding categorical features</figcaption>

<p>
After above process as displayed in the figure 11, it was decided to categorize dataset “week” values into created feature called “Quarter” and “Year” as shown in the figure 16. Reason for categorizing, train dataset contain 146 weeks of data which is approximately 11 quarters and one quarter consist with approximately 13 weeks. That is the reason for week divided by 13 for quarter and purpose of the calculation it was defined to 12 quarters. And year consist with approximately 52 weeks. Therefore, when it comes to years, it was identified 3 years of data. That is the reason for week divided by 52.  Goal of the mapping those related data using map method is to return list of the results according to the calculated outcome.  Then manipulated those data accordingly for the detection outlier purpose.
</p>

<img style="display:block;text-align:center" src="Categorizing year and quarter aspects.PNG" alt="Categorizing year and quarter aspects" >
<figcaption>Figure 12. Categorizing year and quarter aspects</figcaption>

<p>
Before the outlier detection, it was observed necessity of using log transformation on the target feature on the train dataset. Therefore, log transformation included for the target feature as shown in the figure 13 below,
</p>

<img style="display:block;text-align:center" src="Applying log transformation on the target feature.PNG" alt="Applying log transformation on the target feature" >
<figcaption>Figure 13. Applying log transformation on the target feature</figcaption>

<p>
Reason for outlier detection is, without log transformation there is deviation occurred in the trained dataset. Therefore, outlier detection implemented with Interquartile range method as mentioned above. Result of the outlier detection shows in the below figure 18,
</p>  

<img style="display:block;text-align:center" src="Result of outlier detection.PNG" alt="Result of outlier detection" >
<figcaption>Figure 14.Result of outlier detection</figcaption>

<p>
Since, tuning the data as explained in the above section succeeded. It was decided to use CatBoostRegressor as final model for the predict demand.  Therefore, it was decided to test accuracy of the algorithm using train data before finalizing the model. Train dataset contains 146 weeks of data. Therefore, it was decided to split 1st week to 136th week data as train data and from 136th week to 146th data as test data. As shown in figure 15 below,
</p>
 
<img style="display:block;text-align:center" src="Dataset splitting as test set and trains set.PNG" alt="Dataset splitting as test set and trains set" > 
<figcaption>Figure 15. Dataset splitting as test set and trains set</figcaption>

<p>
It was necessary to drop some variable that is not affect to the prediction for improve prediction result. Such as variable “id” and “city_code” are identified as irrelevant variables for train, “num_orders” is a target variable for prediction, “special price” variable calculation of base price and checkout price. but identified there are lack of correlation with the target variable, “week” variable categorized with quarter/year wise and “special price percent” also removed as unrelated variable.
</p>
 
<img style="display:block;text-align:center" src="Removing unwanted variables.PNG" alt="Removing unwanted variables" >
<figcaption>Figure 16. Removing unwanted variables</figcaption>

<p>
After removing irrelevant variables, it was decided to fit catboostRegressor model to the training data using fit method. Therefore, it was able to predict result based on this data using predict method as shown in figure 17 below,
</p>
 
<img style="display:block;text-align:center" src="Model training and data prediction.PNG" alt="Model training and data prediction" >
<figcaption>Figure 17. Model training and data prediction</figcaption>

<p>
Predicted result were evaluated according to the implemented standard evaluation metrics as shown figure 18. 
 </p>
 
<img style="display:block;text-align:center" src="Used evaluation metrics for model evaluation.PNG" alt="Used evaluation metrics for model evaluation" >
<figcaption>Figure 18. Used evaluation metrics for model evaluation</figcaption>

<p>
And result of the evaluation matrix shown in figure 19 below,
</p>

<img style="display:block;text-align:center" src="Model evaluation result from metrics.PNG" alt="Model evaluation result from metrics" >
<figcaption>Figure 19. Model evaluation result from metrics</figcaption>

<p>
In the figure 19, model training time and prediction time according to the following format,

HH – represent Hour.
MM – represent Minute.
SS – represent Second.
NS – represent Nano Second.
It was certified that implementation of this model prediction accuracy very similar to the actual results. Therefore, implemented scatterplot diagram to visualize relationship between actual values and predicted values to ensure above statement (refer figure 20).
</p>
 
<img style="display:block;text-align:center" src="Scatterplot to observe relationship between actual value and predicted values.png" alt="Scatterplot to observe relationship between actual value and predicted values" >
<figcaption>Figure 20. Scatterplot to observe relationship between actual value and predicted values</figcaption>

<p>
As shown in the figure 20, actual value tends to increase as the predicted values increases. Therefore, it is possible to say there is a linear positive correlation between those variables with little number of outliers. At last, it was decided to use this model for demand prediction process. Therefore, only two modification were needed to make. Such as adjust train data selected week range from 1st week to 146th week and adjust test data selected week range from 146th week to 156th week. As per choice, implemented a way to select time period selection for limit prediction demand. 
</p>  
  
<h4>  Domain logic layer summary</h4>

<p>
It was identified that catboost regressor able to predict data better than any other experimented gradient boosting algorithm. Which is implementation similar to this catboost regressor implementation.
</p>

<h4>Data Storage Layer </h4>

<p>
In this section, elaborate data storage mechanism of the CDP system.
</p>

<h4> Explanation of the implementation</h4>

<p>
There were two way of data can be store on the user’s local storage as considering data sharing possibility. Such as, 
• Store generated graph in the local storage - Matplotlib’s Pyplot consist with mechanism for save generated graph in PNG format. Therefore, it was decided to use that functionality rather than customized graph saving. 
• Numeric statistics generation on CSV file and store in the local storage - When prediction process finishes, results will be stored in the defined location on the local storage as implemented (refer figure 21).  
 </p>
 
 <img style="display:block;text-align:center" src="CSV file generation code.PNG" alt="CSV file generation code" >
<figcaption>Figure 21. CSV file generation code</figcaption>

