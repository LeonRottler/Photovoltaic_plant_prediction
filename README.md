# Photovoltaic_plant_prediction

## Project

This is a project that was developed in the context of a grading in the subject Machine Learning of the master program BAM at Furtwangen University. 
The goal of the project is to predict the power of the photovoltaic system at my home based on weather data. 

## What was done

1. The data was obtained from various sources (folder Data)
	- PV system: downloaded from the inverter's web server
	- Weather: downloaded from a web portal of the German Weather Service (DWD)
2. The data was processed and merged (folder ETL)
3. The data was analyzed (folder Data_Vis)
4. Different machine learning algorithms have been compared (folder ML)
5. The XGBoost regressor was chosen and hyperparameter tuning was performed (folder ML)
6. The dashboard was developed

## How to start the streamlit dashboard

1. All required packages are listed in the requirements.txt. With the following command you can install these in your virtualenv or any other environment.
`pip install {path to the txt-file}\requirements.txt`
2. Activate your environment.
3. Adapt the file path of the data and model to be load in the main.py
4. In your CMD run the following command:
`streamlit run {path to the main file of this project}\main.py`