import streamlit as st
import joblib

# Set page title
st.set_page_config(page_title="Emotion Detection Tool", page_icon="😊")

# 1. Load the models silently using cache
@st.cache_resource
def load_models():
    model = joblib.load('model.pkl')
    tfidf = joblib.load('columns.pkl')
    return model, tfidf

model, tfidf = load_models()

# 2. Your specific mapping
emotion_mapping = {
    0: 'sadness',
    1: 'anger',
    2: 'love',
    3: 'surprise',
    4: 'fear',
    5: 'joy'
}

# 3. Clean UI Layout
st.title("😊 Emotion Sentiment Analysis")
st.markdown("---") # Adds a visual divider

user_input = st.text_area("Type your sentence here:", placeholder="e.g., I am feeling wonderful today!")

if st.button("Predict Emotion"):
    if user_input.strip():
        # Transform and Predict
        vectorized_text = tfidf.transform([user_input])
        prediction_num = model.predict(vectorized_text)[0]
        emotion_name = emotion_mapping.get(prediction_num, "Unknown")

        # 1. Display Result
        st.success(f"The detected emotion is: **{emotion_name.upper()}**")

        # 2. Trigger Visuals based on Result
        if emotion_name == 'joy' or emotion_name == 'surprise':
            st.balloons()  # Fun celebration for positive emotions
        elif emotion_name == 'love':
            st.snow()      # A "softer" effect for love/peaceful emotions
        elif emotion_name in ['sadness', 'anger', 'fear']:
            # No balloons for sad/angry results—it keeps the UI respectful!
            st.toast(f"Detected {emotion_name} sentiment.", icon="⚠️")
            
    else:
        st.warning("Please enter some text to analyze.")