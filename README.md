## MLFlow Pipeline Project

MLFLOW_TRACKING_URI=https://dagshub.com/snehaburman/MachineLearningProject.mlflow \
MLFLOW_TRACKING_USERNAME=snehaburman \
MLFLOW_TRACKING_PASSWORD=275507d115bb010006d74cd584035f56f24e528c \
python script.py

#### Overview
Welcome to the MLFlow Pipeline Project! This repository contains the source code and files for building an end-to-end machine learning pipeline using MLFlow. The project includes data ingestion, transformation, model training, and deployment components, all integrated with MLFlow for tracking experiments and model versions.

#### Project Structure
The project is structured as follows:

src/: Contains the source code for the MLFlow pipeline project.
MachineLearningProject/: Main package containing project-specific modules.
components/: Sub-package for data ingestion, transformation, and model training.
pipelines/: Sub-package for training and prediction pipelines.
exception.py: Module for defining custom exceptions.
logger.py: Module for logging messages and errors.
utils.py: Module containing utility functions.
main.py: Main entry point for executing the project.
app.py: File for initializing and running the application.
copy_csv_file.py: Script for copying CSV files.
Dockerfile: Configuration file for building a Docker image.
main.py: Main Python script for running the project.
README.md: This file, containing project overview and instructions.
requirements.txt: File listing project dependencies.
setup.py: Configuration file for setuptools.
template.py: Script for generating project template files.

#### Getting Started
To get started with the MLFlow Pipeline Project, follow these steps:

Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Set up the environment variables specified in README.md.
Run the main script using python main.py.

#### Environment Variables
The project relies on the following environment variables:

MLFLOW_TRACKING_URI: MLflow tracking server URI.
MLFLOW_TRACKING_USERNAME: MLflow tracking server username.
MLFLOW_TRACKING_PASSWORD: MLflow tracking server password.
Ensure these variables are properly configured before running the project.

#### Dataset
The project uses a dataset containing information about students' performance in exams. The dataset includes features such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, and scores in math, reading, and writing.

### Exploratory Data Analysis (EDA)
Before training the models, exploratory data analysis (EDA) was performed to gain insights into the dataset. This involved analyzing the distribution of scores, identifying correlations between features, and visualizing trends using techniques such as histograms, scatter plots, and correlation matrices.

#### Model Training
Several machine learning models were trained using the dataset to predict students' math scores. Models such as Random Forest, Gradient Boosting, and XGBoost were evaluated using techniques like cross-validation and hyperparameter tuning to improve performance.

#### Conclusion
Based on the EDA and model training results, it was found that certain factors such as parental level of education and test preparation course had a significant impact on students' math scores. The best-performing model achieved an R-squared value of X.XX, indicating a good fit to the data.

#### Usage
The MLFlow Pipeline Project can be used for various machine learning tasks, including:

Data ingestion from SQL databases and CSV files.
Data transformation and preprocessing.
Model training and evaluation.
Deployment of trained models using Flask and Docker.