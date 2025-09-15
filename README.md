California Housing Price Prediction

This is a machine learning web application that predicts California housing prices based on user input features. It uses a linear regression model trained on the California Housing dataset, leveraging data preprocessing and scaling for accurate predictions.
Try the live app here: https://californiapricing.streamlit.app/

Features

User-friendly web interface built with Streamlit.

Input fields for all relevant house features.

Real-time median house price prediction.

Visualizations of dataset insights (correlations, scatter plots).

Model and scaler loading from saved pickle files.

Technologies Used

Python 3.x

Streamlit for UI and deployment

Scikit-learn for model training and preprocessing

Pandas and NumPy for data manipulation

Matplotlib and Seaborn for data visualization

Installation and Setup
Clone this repository:

bash
git clone https://github.com/Ankita175/CaliforniaPricing.git

cd CaliforniaPricing

Install dependencies:

bash
pip install -r requirements.txt
Run the Streamlit app:

bash
streamlit run deploy.py
Usage

Open the Streamlit app in your browser (usually at http://localhost:8501).

Enter the details for the features like Latitude, Longitude, House Age, Total Rooms, etc.

View the predicted median house price updated live.

Explore the data visualizations on the app.

Files

deploy.py: Main Streamlit application code.

regmodel.pkl: Pickled linear regression model.

scaler.pkl: Pickled StandardScaler instance.

requirements.txt: Python dependencies for the app.

Contributing

Feel free to fork the repo and make enhancements. Pull requests are welcome.

License

This project is licensed under the Apache 2.0 License.
