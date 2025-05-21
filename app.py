import streamlit as st

# Title
st.title("🌀 Personality Fusion Portal")

# Create a form for inputs
with st.form("personality_form"):
    # MBTI 
    mbti_types = [
        "",  # Allow empty
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]

    mbti = st.selectbox(
        "Select your MBTI type", 
        mbti_types
    )
    
    # Inputs for Big Five traits (OCEAN model)
    st.markdown("### Big Five Personality Traits")
    openness = st.slider("Openness", 0, 100, value=50)
    conscientiousness = st.slider("Conscientiousness", 0, 100, value=50)
    extraversion = st.slider("Extraversion", 0, 100, value=50)
    agreeableness = st.slider("Agreeableness", 0, 100, value=50)
    neuroticism = st.slider("Neuroticism", 0, 100, value=50)

    zodiac = st.selectbox("Choose your Zodiac sign", ["", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                                                      "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    enneagram = st.selectbox("Pick your Enneagram type", ["", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                                           "1w2", "2w3", "3w4", "4w5", "5w6", "6w7", "7w8", "8w9", "9w1"])

    # Submit button
    submitted = st.form_submit_button("Submit")

# When submitted, display what was entered
if submitted:
    st.subheader("🎯 You Entered:")
    
    if mbti:
        st.write(f"**MBTI:** {mbti}")
    if zodiac:
        st.write(f"**Zodiac Sign:** {zodiac}")
    if enneagram:
        st.write(f"**Enneagram:** {enneagram}")
    
    # Only display Big Five if values are different from the neutral default (optional)
    st.write("**Big Five Traits:**")
    st.write(f"- Openness: {openness}")
    st.write(f"- Conscientiousness: {conscientiousness}")
    st.write(f"- Extraversion: {extraversion}")
    st.write(f"- Agreeableness: {agreeableness}")
    st.write(f"- Neuroticism: {neuroticism}")

    if not any([mbti, zodiac, enneagram]) and openness == 50 and conscientiousness == 50:
        st.warning("Hmm, you didn't really give me anything to work with 😅")