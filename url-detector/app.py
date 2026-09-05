import streamlit as st
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, 'phishing_model.pkl'))

def clean_url(u):
    u = u.replace('https://', '').replace('http://', '')
    if u.startswith('www.'):
        u = u[4:]
    return u

st.title("🔗 Malicious URL Detector")
st.write("Koi bhi URL daalo aur pata karo ke wo safe hai ya malicious (phishing/malware/defacement).")

user_url = st.text_input("URL yahan daalo (jaise: bit.ly/xyz123 ya google.com)")

if st.button("Check URL"):
    if user_url.strip() == "":
        st.warning("Pehle koi URL likho.")
    else:
        cleaned = clean_url(user_url)
        prediction = model.predict([cleaned])[0]
        probability = model.predict_proba([cleaned])[0][1]

        if prediction == 1:
            st.error(f"⚠️ Ye URL MALICIOUS ho sakta hai (Risk: {probability:.1%})")
        else:
            st.success(f"✅ Ye URL SAFE lagta hai (Risk: {probability:.1%})")
