# EnergyPredictionML
Measuring renewable energy policy efficacy with machine learning

Neural networks provide opportunities to explore the relationship between energy policy and energy generation and offer a framework for discussing how legislators and regulators can measure and enhance policy efficacy. The final model 1) showcases the nonlinear relationship between energy policy and energy generation; 2) predicts probabilistic energy policy outcomes; 3) corroborates the correlation of year-over-year change in intrastate electricity generation, by fuel source. 

Neural networks are powerful computational tools that can generate exceptional performance in predicting non-linear relationships. Within the context of policymaking, neural networks can calculate relationships between policies and the desired outcome. Many types of neural networks exist, but this paper applies a specific type called a multilayer perceptron (MLP) to United States Energy Efficiency and Renewable Energy (EERE) policy at the state level. By applying an MLP to the EERE policy, the network learns the relationship between these policies and a particular state’s electricity generation. This MLP model trains itself using existing data from the North Carolina Clean Energy Technology Center’s Database of State Incentives for Renewables & Efficiency (DSIRE) using the U.S. Energy Information Administration (EIA)’s Open Data Application Programming Interface (API) to predict how differing energy efficiency and renewable energy policies affect real time energy generation.

This project applies an MLP and simple models to DSIRE and EIA data to predict whether net generation, by fuel source, increases year-over-year. The Python Notebook contains model development and data processing and loading can be found in the DataProcessing folder.

The website includes a deployed tensorflow.js model that user can test via inputs. For access, please visit: 
