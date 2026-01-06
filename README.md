## 🌿 Stress Level Prediction Web App

A machine-learning powered Streamlit application for assessing stress levels and providing personalized insights.
The Stress Level Prediction Web App enables users to input daily lifestyle parameters and instantly receive a predicted stress score powered by a trained machine-learning model.

 ## Beyond predictions, the app provides:

✔ Real-time visualizations

✔ Personalized recommendations

✔ Factor-based analysis

✔ Beautiful modern UI

✔ Responsive layout and interactive controls


## 🎨 UI/UX Enhancements

This version includes a beautifully redesigned interface:

🌈 Modern gradient background with smooth color transitions

🖱 Interactive sliders with real-time feedback and live status indicators

📱 Fully responsive two-column layout

🎨 Custom CSS styling for a polished, professional UI

📊 Animated Plotly gauge chart for stress prediction

💬 Large emoji-based indicators for instant emotional clarity


## ✨ New Functional Modules

1️⃣ Sidebar Information Panel

Includes:

About section

Helpful tips for input optimization

<img width="719" height="279" alt="Screenshot 2025-12-03 162833" src="https://github.com/user-attachments/assets/a43a522f-378d-4587-b122-ab46d7d383ce" />


2️⃣ Metrics Dashboard

Interactive cards showing:

Current input values

Status labels (✔ Optimal | ⚠ Adjust | ⬆ Increase)

Real-time response to slider movement

<img width="1870" height="899" alt="Screenshot 2025-12-03 163514" src="https://github.com/user-attachments/assets/ceac7033-253a-42b4-91bb-431583dcabf8" />


3️⃣ Prediction Result Dashboard

🎯 Animated Plotly gauge meter

🟢🟡🔴 Color-coded stress categories

Clear textual interpretation

<img width="1792" height="601" alt="Screenshot 2025-12-03 163610" src="https://github.com/user-attachments/assets/3a5ee67f-1006-4b6c-8fd6-69edea9d96bd" />


4️⃣ Personalized Recommendations

Recommendations dynamically adapt to the stress score, including:

Lifestyle adjustments

Work habits

Relaxation techniques

Health-focused advice

<img width="1553" height="669" alt="Screenshot 2025-12-03 163208" src="https://github.com/user-attachments/assets/e2f8c7e1-ab3c-4b66-b692-9dce920f2fb2" />


5️⃣ Factor Analysis Section

For each input parameter:

Shows impact on stress

Displays optimal ranges

Provides educational info

Helps users understand why their stress level is high or low

<img width="1501" height="333" alt="Screenshot 2025-12-03 163248" src="https://github.com/user-attachments/assets/1b2d05d3-96e6-48e3-9edc-6b7e31440687" />


## 🧪 Tech Stack

Frontend UI	-Streamlit + Custom CSS

Visualization -	Plotly, Streamlit native charts

Model -	Machine Learning (trained regression/classification model)

Language- Python

Environment	-venv

Deployment - Local execution



## ▶️ How to Run the App
1. Clone the repository
   
git clone https://github.com/your-repo/stress-prediction-app.git
cd stress-prediction-app

2. Install dependencies

pip install -r requirements.txt

3. Run the Streamlit app

streamlit run app.py


## 📈 How the Model Works

The model takes the following inputs:

Humidity,
Temperature,
Step count

These values are scaled and passed into the trained Random Forest model, which outputs a predicted Stress Level.

Outputs a continuous stress score which is mapped into categories:

0.0 – 1.0	🟢	Low Stress	Balanced & healthy

1.0 – 1.4	🟡	Moderate Stress	Needs attention

1.4 – 2.0	🔴	High Stress	Requires immediate relief measures

🚀 Future Enhancements

Add heart rate and sleep cycle data

Deploy the model on Render / HuggingFace Spaces

Convert Streamlit app into a mobile UI

Integrate with smartwatch APIs

📊 Results & Insights

Strong correlations were observed between temperature/humidity and stress

Step count played a moderate role

Random Forest captured non-linear relationships effectively

Model achieved ~99.998% accuracy


📚 Dataset & Research References

📊 Kaggle Dataset

This project uses the dataset from:
**“Human Stress Detection” — Laavanya Rachakonda (Kaggle)**

Citation :

L. Rachakonda, S. P. Mohanty, E. Kougianos, and P. Sundaravadivel, “Stress-Lysis: A DNN-Integrated Edge Device for Stress Level Detection in the IoMT,” IEEE Trans. Conum. Electron., vol. 65, no. 4, pp. 474–483, 2019.

L. Rachakonda, P. Sundaravadivel, S. P. Mohanty, E. Kougianos, and M. Ganapathiraju, “A Smart Sensor in the IoMT for Stress Level Detection”, in Proceedings of the 4th IEEE International Symposium on Smart Electronic Systems (iSES), 2018, pp. 141--145.

📄 IEEE Research Paper

The dataset includes an accompanying research paper:

Paper:*Stress-Lysis: A DNN-Integrated Edge Device for Stress Level Detection in the IoMT*

Publisher: IEEE

Citation (IEEE):

Laavanya Rachakonda, Student Member, IEEE, Saraju P. Mohanty, Senior Member, IEEE, Elias Kougianos,
Senior Member, IEEE, and Prabha Sundaravadivel, Member, IEEE


👨‍💻 Author

Shabdika Mishra

Second-Year CSE (AIML) Student

