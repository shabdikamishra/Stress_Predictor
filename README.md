## 🌿 Stress Level Prediction Web App

A machine-learning powered Streamlit application for assessing stress levels and providing personalized insights.

🚀 Overview

The Stress Level Prediction Web App enables users to input daily lifestyle parameters and instantly receive a predicted stress score powered by a trained machine-learning model.

Beyond predictions, the app provides:

✔ Real-time visualizations

✔ Personalized recommendations

✔ Factor-based analysis

✔ Beautiful modern UI

✔ Responsive layout and interactive controls

This project focuses on delivering an accurate, intuitive, and aesthetically rich experience for end-users.

🧠 Features
🎨 UI/UX Enhancements

This version includes a beautifully redesigned interface:

🌈 Modern gradient background with smooth color transitions

🖱 Interactive sliders with real-time feedback and live status indicators

📱 Fully responsive two-column layout

🎨 Custom CSS styling for a polished, professional UI

📊 Animated Plotly gauge chart for stress prediction

💬 Large emoji-based indicators for instant emotional clarity

📸 Screenshot Placeholder:

![UI Overview](screenshots/ui_overview.png)

✨ New Functional Modules

1️⃣ Sidebar Information Panel

Includes:

About section

Stress category legend

Helpful tips for input optimization

📸 Screenshot Placeholder:

![Sidebar Panel](screenshots/sidebar_info.png)

2️⃣ Metrics Dashboard

Interactive cards showing:

Current input values

Status labels (✔ Optimal | ⚠ Adjust | ⬆ Increase)

Real-time response to slider movement

📸 Screenshot Placeholder:

![Metrics Dashboard](screenshots/metrics_dashboard.png)

3️⃣ Prediction Result Dashboard

🎯 Animated Plotly gauge meter

🔵🟡🔴 Color-coded stress categories

📈 Progress bar visualization

Clear textual interpretation

📸 Screenshot Placeholder:

![Prediction Result](screenshots/prediction_result.png)

4️⃣ Personalized Recommendations

Recommendations dynamically adapt to the stress score, including:

Lifestyle adjustments

Work habits

Relaxation techniques

Health-focused advice

📸 Screenshot Placeholder:

![Recommendations](screenshots/recommendations.png)

5️⃣ Factor Analysis Section

For each input parameter:

Shows impact on stress

Displays optimal ranges

Provides educational info

Helps users understand why their stress level is high or low

📸 Screenshot Placeholder:

![Factor Analysis](screenshots/factor_analysis.png)

🧪 Tech Stack

Component	                  Technology

Frontend UI	-            Streamlit + Custom CSS

Visualization -       	Plotly, Streamlit native charts

Model -        	Machine Learning (trained regression/classification model)

Language-                      Python

Environment	-                  venv

Deployment -             Local execution


📁 Project Structure
StressPredictor/
│
├── data/
│   └── Stress-Lysis.csv
│
├── notebooks/
│   └── 1noteb.ipynb
|   └── models/
│       └── StressPredictor.pkl
|       └── scalar.pkl
│
├── app/
│   └── app.py
│
├── requirements.txt
├── README.md


▶️ How to Run the App
1. Clone the repository
git clone https://github.com/your-repo/stress-prediction-app.git
cd stress-prediction-app

2. Install dependencies
pip install -r requirements.txt

3. Run the Streamlit app
streamlit run app.py

📈 How the Model Works

The model takes the following inputs:
Humidity
Temperature
Step count

These values are scaled and passed into the trained Random Forest model, which outputs a predicted Stress Level.

Outputs a continuous stress score which is mapped into categories:

Score         Range	                          Category	                              Meaning
0– 1	        🟢                             Low Stress	                         Balanced & healthy
1- 1.4	      🟡                            Moderate Stress	                      Needs attention
1.4- 2	      🔴                            High Stress	                   Requires immediate relief measures

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

🙏 Acknowledgements

Thanks to **Laavanya Rachakonda (Kaggle)** and the authors of the IEEE paper for making this research possible.

🤝 Contributing

Contributions are welcome!
Please fork the repo, open a PR, and ensure your code follows project guidelines.

👨‍💻 Author

Shabdika Mishra

Second-Year CSE (AIML) Student

⭐ Support

If you find this project helpful, consider giving it a ⭐ star on GitHub!
