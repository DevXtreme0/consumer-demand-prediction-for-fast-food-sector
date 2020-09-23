# Fast Food Demand Predciton
<p> A computer system which can predict consumer demand for fast food sector. </p>

<p color = "red"> Note:  </p>

<h3>Desription</h3>
<p>
Lack of fast food fulfillment to the consumer, excesses of fast food over the estimated demand, and business loss profit cause by inaccurate demand prediction are common nowadays in fast food centers and fast food base businesses(based on local context - Sri Lanka). Therefore, proposes a solution to avoid this problem by predicting consumer demand for the fast-food sector. Used a forecasting algorithm known as CatBoost with a data categorization technique. Fast food demand is affected by several independent variables such as seasonality, trend, price fluctuation, and length of historical data. A combination of these selected variables was used to calculate demand prediction using parameter tuning in the CatBoost algorithm and other algorithms (slightly different but the same domain) used for the experiment (Such as Linear Regression, LGBM, and XGBoost). However, CatBoost was the best performing model that was selected. Therefore, windows based standalone solution was developed to yield fast-food demand prediction statistics.</p>

<h3>Link for Application Demostration Video</h3> 
https://youtu.be/qMAt5fyCOyQ

<h3>Explanation of the proposed solution</h3>

<h4> Dataset Selection and configuration to the system </h4>

<p>
One dataset is a combination of three single information files. One of file consist with historical demand information for each center. And another file consists data of center information and other file consist of meal information. Additional file related to test information also used for the demand prediction through the final solution.
</p>

1. Historical demand information file – trainForLearnInformation.csv
Consist with the historical information of demand for each center. Its defined variables listed with brief description in below,
•base_price: - Average price of the meal
•checkout_price: - Sold price for the meal
•meal_id: - Specific Id for the meal
•center_id: - Specific Id for the meal center
•week: - Week number for sold meal
•id: - Specific Id for the recorded single information
•emailer_for_promotion: - Removed this variable from the implantation usage 
•homepage_featured: - Removed this variable from the implantation usage
•num_orders: - Demand for the meal

2. Historical center information file – centerInformation.csv
Consist historical data for each center. Its defined variables listed with brief description in below,
•center_id: - Specific Id for the meal center
•city_code: - Specific code for the center located city 
•region_code: - Removed this variable from the implantation usage 
•center_type: - Centre type for categorization purpose 
•op_area: - Removed this variable from the implementation usage 

3. Historical meal information file – mealInformation.csv
Consist historical data of meal information. Its defined variables listed with brief description in below,
•meal_id: - Specific Id for the meal
•category: - Categorized name for the meal
•cuisine: - Type of the cuisine for the meal

4. Test Information file data from 146th week to 155th week data – testInformation.csv
Consist with test data for model validation purpose. Same variables included as mentioned in the Historical demand information file (trainForLearnInformation file) except for target variable “num_orders”.

<h4> Use of data preprocessing from the extracted information </h4>

<p>
When user input files to the system, all information on the submitted files merged into a separate one dataset. Therefore, not having null values or missing values is compulsory. After this validation prediction process will initiate. Therefore, merging information required to be validated. As an example, when merging files “trainForLearnInformation” file specific variable name and its contents should be matched to the same name and contents in the other file. Such as trainToLearn file “meal_id” should match in the mealInfromation file “meal_id” variable. Figure 1 shows how this achieved step by step below,
 </p>
 
 <figure>
 <img style="display:block;text-align:center" src="Data preprocessing code.PNG" alt="Data preprocessing code" >
 <figcaption text-align = "center"> Figure 1. Data preprocessing code </figcaption>
 </figure>

<h4> Use of exploratory data analysis for the dataset</h4>
<p>
This is a process, performing initial investigation on data. Such as identify patterns, identify anomalies, test hypothesis and validate assumptions with the help of graphical statistics representation or statistical information. This process was taken through python language using libraries for display graphs and results.
Beginning of the exploratory data analysis process, it is compulsory to identify and remove unnecessary variables that is not contributing to prediction process. As shown in the section 6.3.2.3.3.  There are four variables are needed to be removed. Such as region_code, op_area, emailer_for_promotion and homepage_featured. Therefore, emailer_for_promotion and homepage_featured column with data was dropped by updating file. However, region_code, op_area kept in the dataset for identify its necessity to the implementation. Information regarding number of entries for each variable and their data types in each data files shown in the table 2 below,
 </p>
 
<img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 2. Train information dataset contents
	 
<img style="display:block;text-align:center" src="Center information dataset contents.PNG" alt="Center information dataset contents" >   
Figure 3. Center information dataset contents

<img style="display:block;text-align:center" src="Meal information dataset contents.PNG" alt="Meal information dataset contents" > 
Figure 4. Meal information dataset contents
 
<img style="display:block;text-align:center" src="Test information dataset contents.PNG" alt="Test information dataset contents" >
Figure 5. Test information dataset contents

<p>
According to the above figure 2, 3, 4 and 5, some of the variables contains objects defined by dataset. As shows in the figure 5 to fig 8, some of the variable contains numeric values for demand prediction purpose. In figure 5 shows, there is train dataset contains 456548 rows and 7 columns. In figure 6 shows, there is center information dataset contains 77 rows and 5 columns. In figure 7 shows, there is meal information dataset contains 51 rows and 3 columns. In figure 8 shows, there is test dataset contains 32573 rows and 6 columns.
Next process of the exploratory data analysis is to standardization of features that is used for demand prediction process. Which is briefly explained in section 6.3.2.3.4 regarding feature creation and its purpose. Standardization is a technique used to change the values of numeric columns in the dataset to a common scale, without altering differences in the ranges of values. standardization of the created features is necessary due to accuracy of the model is not acceptable and high deviation of the values were observed during the implementation. Sample of standardized dataset shown in figure X below,
</p>

<img style="display:block;text-align:center" src="Sample of standardized dataset.PNG" alt="Sample of standardized dataset" >
Figure 6. Sample of standardized dataset

<p>
Final process of the exploratory data analysis is to identify correlation of each variables. Correlation is a statistical technique that is represent relationships of variables between each other. There are three methods available for calculate correlation. Such as Pearson correlation coefficient, Kendall rank correlation coefficient and Spearman's rank correlation coefficient. Pearson correlation coefficient is measures linear correlation between two variables in statistics form. Its value ranges from -1 to +1. In the meaning of values viewpoint, value -1 indicates correlation is negative, value +1 indicates correlation is positive and value 0 means no correlation at all. Kendall rank correlation coefficient is an ordinal association between two measured quantities. Spearman's rank correlation coefficient is a nonparametric measure of rank correlation. It assesses how well the relationship between two variables can be described. Therefore, Pearson correlation coefficient was chosen since it is widely used and most suited for this study. Generated heatmap of pairwise calculation with the use of Pearson correlation coefficient method shows in figure 10 below, (refer appendix X for used code)
 </p>
 
<img style="display:block;text-align:center" src="Generated heatmap for identify variable correlation.PNG" alt="Generated heatmap for identify variable correlation" > 
Figure 7. Generated heatmap for identify variable correlation

<p>
According to the above figure 10 above, it is possible to identify “base_price” and “checkout_price” highly correlated variables with each other. Therefore, using these variables might be enough to create final model. But before adding to the final model it was decided to validate with “num_orders” variable. Therefore, it was decided to subtract “base_price” variable value from “checkout_price” variable value and store result as special price. After special price calculation, relationship between “num_orders” variable and special price variable displayed in the scatterplot as shown in figure 11,
</p> 

<img style="display:block;text-align:center" src="Scatter plot for observe relationship of selected variables.PNG" alt="Scatter plot for observe relationship of selected variables" >
Figure 8. Scatter plot for observe relationship of selected variables

<p>
However, according to the above figure 11 it was observed that relationship between each variable is non-linear and not good correlation for final model. Therefore, it was decided to focus on other techniques rather than depending on specific variable selection according to linearity and correlation. 
</p>

<h4> Use of feature engineering from the extracted information</h4>

<p>
This is a method to create features according to the domain knowledge that enables to enhance performance and accuracy of the machine learning models using dataset. Therefore, below table 12 clarify about the features that is used for model creation from the available dataset,
</p>
Created Feature	Feature Description
Special Price	Price defined by subtracting “checkout_price” variable by “base_price” variable.
Special Price Percent	Percentage of the special price.
Special Price T/F	Defines special price included or not. If special price is true, then value will be -1 if special price is false, then value will be 0.
Weekly Price Comparison	This is a price comparison of the selected weeks about rise or fall of the meal for a specific each center. 
Weekly Price Comparison T/F	Defines price comparison increased or not. If increase true, then value will be -1 if it is false, then value will be 0.
Year	This defined according to the dataset, number of weeks.
Quarter	According to the dataset, number of weeks defines as one-fourth of a year.

<img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 9.created feature explanation

<h4>Use of data transformation eliminate outliers</h4>

<p>
In the demand prediction context, it is compulsory to outlier data to be 0% on targeted variable called “num_orders”. Therefore, this necessity achieved by using Interquartile range method. Log transformation is the most popular among the different types of transformations used to transform skewed data to approximately conform to normality in feature engineering. Therefore, in the target variable called “num_orders” is not aligned with normality and non-use of transformation methods will reduce performance of the data model. Therefore, it was decided to include log transformation on targeted variable “num_orders”. Which is data approximately conform to normality. Implementation of it shown in figure 12 below,
</p>

<img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 13. Outlier detection code

<h4>  Elaboration of used ML algorithms for demand prediction </h4>

<p>
Multiple data modeled using gradient boosting algorithms (such as XGBoost, LightGBM and CatBoost) and linear regression algorithm. Those algorithms implemented with feature extraction, data transformation and data preprocessing for achieve better accuracy on predicted result. In-depth explanation of those algorithm explained in the literature review. Therefore, in this section only elaborate way of algorithm implementation.
At first, it was decided to copy and merge dataset as dataframe into a variable and get top five of a data from data frame as shown in the figure 14. Reason behind is to get set of data continue process. Reason for using “head” method is to process of test if object has the right type of data in it or not.
</p>

<img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 14. Get data through DataFrame

<p>
After above process, it was decided to encode categorical features and manipulate data received through above process to data standardization as shown in the figure 15 below, Reason for using “astype” method is to convert column data to object type. Which is helps to reduce usage of memory space. 
</p> 

<img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 15. Encoding categorical features

<p>
After above process as displayed in the figure 15, it was decided to categorize dataset “week” values into created feature called “Quarter” and “Year” as shown in the figure 16. Reason for categorizing, train dataset contain 146 weeks of data which is approximately 11 quarters and one quarter consist with approximately 13 weeks. That is the reason for week divided by 13 for quarter and purpose of the calculation it was defined to 12 quarters. And year consist with approximately 52 weeks. Therefore, when it comes to years, it was identified 3 years of data. That is the reason for week divided by 52.  Goal of the mapping those related data using map method is to return list of the results according to the calculated outcome.  Then manipulated those data accordingly for the detection outlier purpose.
</p>

<img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 16. Categorizing year and quarter aspects

<p>
Before the outlier detection, it was observed necessity of using log transformation on the target feature on the train dataset. Therefore, log transformation included for the target feature as shown in the figure 17 below,
</p>

<img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 17. Applying log transformation on the target feature

<p>
Reason for outlier detection is, without log transformation there is deviation occurred in the trained dataset. Therefore, outlier detection implemented with Interquartile range method as mentioned in the section 6.3.2.3.5 and figure 13. Result of the outlier detection shows in the below figure 18,
</p>  

<p>
Since, tuning the data as explained in the above section succeeded. It was decided to use CatBoostRegressor as final model for the predict demand. Reason for the selection will explain in the testing chapter section X. Therefore, it was decided to test accuracy of the algorithm using train data before finalizing the model. Train dataset contains 146 weeks of data. Therefore, it was decided to split 1st week to 136th week data as train data and from 136th week to 146th data as test data. As shown in fig 19 below,
 </p>
 
<img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" > 
Figure 19. Dataset splitting as test set and trains set

<p>
It was necessary to drop some variable that is not affect to the prediction for improve prediction result. Such as variable “id” and “city_code” are identified as irrelevant variables for train, “num_orders” is a target variable for prediction, “special price” variable calculation of base price and checkout price. but identified there are lack of correlation with the target variable (see section, figure X), “week” variable categorized with quarter/year wise and “special price percent” also removed as unrelated variable.
 </p>
 
 <img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 20. Removing unwanted variables

<p>
After removing irrelevant variables, it was decided to fit catboostRegressor model to the training data using fit method. Therefore, it was able to predict result based on this data using predict method as shown in figure 21 below,
 </p>
 
 <img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 21. Model training and data prediction

<p>
Predicted result were evaluated according to the implemented standard evaluation metrics as shown figure 22. In-depth explanation of the used evaluation metrics will discuss in testing chapter, section X. 
  </p>
 
 <img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 22. Used evaluation metrics for model evaluation

<p>
And result of the evaluation matrix shown in figure 23 below,

Figure 23. Model evaluation result from metrics
In the figure 23, model training time and prediction time according to the following format,
HH – represent Hour.
MM – represent Minute.
SS – represent Second.
NS – represent Nano Second.
It was certified that implementation of this model prediction accuracy very similar to the actual results. Therefore, implemented scatterplot diagram to visualize relationship between actual values and predicted values to ensure above statement (refer figure 24).
</p>
 
 <img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 24. Scatterplot to observe relationship between actual value and predicted values

<p>
As shown in the figure 24, actual value tends to increase as the predicted values increases. Therefore, it is possible to say there is a linear positive correlation between those variables with little number of outliers. At last, it was decided to use this model for demand prediction process. Therefore, only two modification were needed to make. Such as adjust train data selected week range from 1st week to 146th week and adjust test data selected week range from 146th week to 156th week. As per choice, implemented a way to select time period selection for limit prediction demand. 
</p>  
  
<h4>  Domain logic layer summary

It was identified that catboost regressor able to predict data better than any other experimented gradient boosting algorithm (refer section X). Which is implementation similar to this catboost regressor implementation. Result of the other experimented algorithm and comparison will be discussing in the testing chapter.

<h4>Data Storage Layer </h4>

<p>
In this section, elaborate data storage mechanism of the CDP system.
</p>

<h4> Explanation of the implementation

<p>
There were two way of data can be store on the user’s local storage as considering data sharing possibility. Such as, 
• Store generated graph in the local storage.
Matplotlib’s Pyplot consist with mechanism for save generated graph in PNG format. Therefore, it was decided to use that functionality rather than customized graph saving. 
• Numeric statistics generation on CSV file and store in the local storage.
When prediction process finishes, results will be stored in the defined location on the local storage as implemented (refer figure 25).  
 </p>
 
 <img style="display:block;text-align:center" src="Train information dataset contents.PNG" alt="Train information dataset contents" >
Figure 25. CSV file generation code


<h4>Data storage layer summary</h4>

<p>
It was decided not to use relational database for the system due to the nature of this application. But it is possible to add database if it is needed.</p>
