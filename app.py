import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import sys, platform

# ✅ Page config must be here at the very top
st.set_page_config(page_title="Sleep Quality Dashboard", layout="wide")

# (optional) show python version
st.caption(f"Python: {sys.version.split()[0]} • {platform.python_implementation()}")

# ---- rest of your code ----
try:
    df = pd.read_csv("ss_clean.csv")
    st.success("✅ Dataset loaded successfully!")
except Exception as e:
    st.error(f"❌ Failed to load dataset: {e}")

# ------------------- Load Models -------------------
model_sd, model_qs = None, None

try:
    model_sd = joblib.load("sleep_disorder_model.pkl")
    st.success("✅ Sleep Disorder model loaded successfully!")
except Exception as e:
    st.error(f"❌ Failed to load Sleep Disorder model: {e}")

try:
    model_qs = joblib.load("sleep_quality_model.pkl")
    st.success("✅ Sleep Quality model loaded successfully!")
except Exception as e:
    st.error(f"❌ Failed to load Sleep Quality model: {e}")

# ------------------- Dashboard UI -------------------
st.set_page_config(page_title="Sleep Quality Dashboard", layout="wide")
st.title("😴 Sleep Quality & Disorder Prediction Dashboard")

if df is not None and model_sd is not None and model_qs is not None:
    # Sidebar: user selection
    st.sidebar.header("Select User")
    user_index = st.sidebar.number_input(
        f"Row index (0 - {len(df)-1})", min_value=0, max_value=len(df)-1, value=0
    )
    user_data = df.iloc[user_index]

    # -------- Predictions --------
    st.subheader("🩺 Predictions")
    try:
        sd_pred = model_sd.predict([user_data.drop("Sleep Disorder")])[0]
        st.write(f"**Predicted Sleep Disorder:** {sd_pred}")
    except Exception as e:
        st.error(f"❌ Sleep Disorder prediction failed: {e}")

    try:
        qs_pred = model_qs.predict(
            [user_data.drop(["Sleep Disorder", "SleepQuality_Class"], errors="ignore")]
        )[0]
        st.write(f"**Predicted Sleep Quality:** {qs_pred}")
    except Exception as e:
        st.error(f"❌ Sleep Quality prediction failed: {e}")

    # -------- Suggestions --------
    st.subheader("💡 Personalized Suggestions")
    try:
        tips = generate_suggestions(user_data)
        for t in tips:
            st.write("- ", t)
    except Exception as e:
        st.error(f"❌ Suggestion generation failed: {e}")

    # -------- Visualizations --------
    st.subheader("📈 Visualizations")
    try:
        fig1 = px.histogram(df, x="Quality of Sleep", nbins=10, title="Distribution of Sleep Quality")
        st.plotly_chart(fig1, use_container_width=True)

        fig2 = px.histogram(df, x="Sleep Disorder", title="Distribution of Sleep Disorders")
        st.plotly_chart(fig2, use_container_width=True)

        fig3 = px.scatter(
            df, x="Stress Level", y="Quality of Sleep", color="Gender", title="Stress vs Sleep Quality"
        )
        st.plotly_chart(fig3, use_container_width=True)
    except Exception as e:
        st.error(f"❌ Visualization failed: {e}")
else:
    st.warning("⚠️ Some files (dataset or models) could not be loaded. Please check your repo.")
