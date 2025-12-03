import streamlit as st
import joblib
import numpy as np
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Stress Level Predictor",
    page_icon="🧘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(to bottom right, #e0e7ff, #f3e8ff);
    }
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    .prediction-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .recommendation-box {
        background: #f0f9ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #3b82f6;
        margin: 10px 0;
    }
    h1 {
        color: #1e293b;
        text-align: center;
        padding: 20px 0;
    }
    .stSlider > div > div > div {
        background: linear-gradient(to right, #667eea, #764ba2);
    }
</style>
""", unsafe_allow_html=True)

# Load models
@st.cache_resource
def load_models():
    try:
        model = joblib.load("notebook/models/StressPredictor.pkl")
        scaler = joblib.load("notebook/models/scaler.pkl")
        return model, scaler
    except:
        st.warning("⚠️ Model files not found. Using demo mode.")
        return None, None

model, scaler = load_models()

# Helper functions
def get_stress_category(stress_level):
    if stress_level < 1 and stress_level >= 0:
        return "Low", "#10b981", "🟢"
    elif stress_level < 1.4 and stress_level >= 1:
        return "Moderate", "#f59e0b", "🟡"
    else:
        return "High", "#ef4444", "🔴"

def get_recommendations(stress_level):
    if stress_level < 1 and stress_level >= 0:
        return [
            "✅ Great job! Keep maintaining your healthy lifestyle.",
            "✅ Continue your regular exercise routine.",
            "✅ Your environment is well-balanced."
        ]
    elif stress_level < 1.4 and stress_level >= 1:
        return [
            "⚠️ Consider taking short breaks throughout the day.",
            "⚠️ Try to increase your daily step count to 8,000-10,000.",
            "⚠️ Monitor your environment comfort levels.",
            "⚠️ Practice relaxation techniques like deep breathing."
        ]
    else:
        return [
            "🚨 Take immediate steps to reduce stress.",
            "🚨 Increase physical activity significantly (aim for 10,000+ steps).",
            "🚨 Optimize your environment (temperature & humidity).",
            "🚨 Consider relaxation techniques like meditation or yoga.",
            "🚨 Consult a healthcare professional if stress persists."
        ]

def create_gauge_chart(stress_level):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=stress_level,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Stress Level", 'font': {'size': 24, 'color': '#1e293b'}},
        number={'font': {'size': 50, 'color': '#1e293b'}},
        gauge={
            'axis': {'range': [None, 2], 'tickwidth': 1, 'tickcolor': "#1e293b"},
            'bar': {'color': get_stress_category(stress_level)[1]},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#e2e8f0",
            'steps': [
                {'range': [0, 0.9], 'color': '#d1fae5'},
                {'range': [1, 1.4], 'color': '#fef3c7'},
                {'range': [1.5, 2], 'color': '#fee2e2'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 8
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=300,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    return fig

# Header
st.markdown("<h1>🧘 Stress Level Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 18px;'>Monitor your stress based on environmental and activity data</p>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar for information
with st.sidebar:
    st.header("📊 About This App")
    st.info("""
    This app predicts your stress level based on:
    - **Humidity**: Environmental moisture levels
    - **Temperature**: Ambient temperature
    - **Step Count**: Your daily physical activity
    """)
    
    st.header("📈This app Categorizes Stress on a scale of 0 to 2")
    st.success("🟢 **Low (0-1)**: Minimal stress, great balance")
    st.warning("🟡 **Moderate (1-1.4)**: Some stress, room for improvement")
    st.error("🔴 **High (1.4-2)**: Significant stress, take action")
    
    st.header("💡 Tips")
    st.markdown("""
    - Aim for 8,000-10,000 steps daily
    - Maintain comfortable room temperature (20-24°C)
    - Keep humidity between 30-50%
    - Regular exercise reduces stress
    """)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Enter Your Data")
    
    # Humidity input
    st.markdown("### 💧 Humidity")
    humidity = st.slider(
        "Humidity Level (%)",
        min_value=0,
        max_value=100,
        value=50,
        help="Current humidity level in your environment"
    )
    st.caption(f"Current: **{humidity}%** {'(Dry)' if humidity < 30 else '(Comfortable)' if humidity < 60 else '(Humid)'}")
    
    st.markdown("---")
    
    # Temperature input
    st.markdown("### 🌡️ Temperature")
    temperature = st.slider(
        "Temperature (°C)",
        min_value=-0,
        max_value=100,
        value=25,
        help="Current temperature in your environment"
    )
    st.caption(f"Current: **{temperature}°C** {'(Cold)' if temperature < 18 else '(Comfortable)' if temperature < 28 else '(Hot)'}")
    
    st.markdown("---")
    
    # Steps input
    st.markdown("### 👟 Daily Steps")
    steps = st.slider(
        "Step Count",
        min_value=0,
        max_value=1500,
        value=500,
        step=100,
        help="Number of steps you've taken today"
    )
    st.caption(f"Current: **{steps:,}** steps {'(Sedentary)' if steps < 5000 else '(Lightly Active)' if steps < 7500 else '(Active)' if steps < 10000 else '(Very Active)'}")

with col2:
    st.subheader("📊 Your Metrics Summary")
    
    # Display current values in cards
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        st.metric(
            label="💧 Humidity",
            value=f"{humidity}%",
            delta="Optimal" if 30 <= humidity <= 50 else "Adjust"
        )
    
    with metric_col2:
        st.metric(
            label="🌡️ Temperature",
            value=f"{temperature}°C",
            delta="Optimal" if 20 <= temperature <= 24 else "Adjust"
        )
    
    with metric_col3:
        st.metric(
            label="👟 Steps",
            value=f"{steps:,}",
            delta="Good" if steps >= 8000 else "Increase"
        )
    
    st.markdown("---")
    
    # Predict button
    predict_button = st.button("🔮 Predict Stress Level", use_container_width=True, type="primary")

# Prediction section
if predict_button:
    with st.spinner("🔄 Analyzing your data..."):
        if model is not None and scaler is not None:
            # Actual prediction
            X = scaler.transform([[humidity, temperature, steps]])
            prediction = model.predict(X)[0]
        else:
            # Demo prediction
            normalized_humidity = (humidity - 30) / 40
            normalized_temp = (temperature - 15) / 20
            normalized_steps = (10000 - steps) / 10000
            prediction = max(0, min(10, (normalized_humidity * 2 + normalized_temp * 3 + normalized_steps * 5)))
        
        st.markdown("---")
        
        # Results
        st.subheader("🎯 Prediction Results")
        
        result_col1, result_col2 = st.columns([1, 1])
        
        with result_col1:
            # Gauge chart
            fig = create_gauge_chart(prediction)
            st.plotly_chart(fig, use_container_width=True)
        
        with result_col2:
            category, color, emoji = get_stress_category(prediction)
            
            st.markdown(f"""
            <div class="prediction-box">
                <h2 style="margin: 0; font-size: 48px;">{emoji}</h2>
                <h3 style="margin: 10px 0;">Stress Level: {prediction:.2f} / 2</h3>
                <h2 style="margin: 10px 0; font-size: 32px;">{category} Stress</h2>
                <p style="margin: 0; opacity: 0.9;">Based on your current environment and activity</p>
            </div>
            """, unsafe_allow_html=True)
            
    
        
        # Recommendations
        st.markdown("---")
        st.subheader("💡 Personalized Recommendations")
        
        recommendations = get_recommendations(prediction)
        
        for rec in recommendations:
            st.markdown(f"""
            <div class="recommendation-box">
                {rec}
            </div>
            """, unsafe_allow_html=True)
        
        # Environmental factors analysis
        st.markdown("---")
        st.subheader("🔍 Factor Analysis")
        
        analysis_col1, analysis_col2, analysis_col3 = st.columns(3)
        
        with analysis_col1:
            humidity_status = "✅ Optimal" if 30 <= humidity <= 50 else "⚠️ Needs Adjustment"
            st.info(f"""
            **Humidity Impact**
            
            Status: {humidity_status}
            
            High humidity can increase stress and discomfort. Aim for 30-50%.
            """)
        
        with analysis_col2:
            temp_status = "✅ Optimal" if 20 <= temperature <= 24 else "⚠️ Needs Adjustment"
            st.info(f"""
            **Temperature Effect**
            
            Status: {temp_status}
            
            Extreme temperatures elevate stress levels. Aim for 20-24°C.
            """)
        
        with analysis_col3:
            steps_status = "✅ Active" if steps >= 8000 else "⚠️ Increase Activity"
            st.info(f"""
            **Activity Benefits**
            
            Status: {steps_status}
            
            More steps reduce stress naturally. Aim for 8,000-10,000 daily.
            """)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8;'>Made by Shabdika | Stay healthy and stress-free!</p>", unsafe_allow_html=True)