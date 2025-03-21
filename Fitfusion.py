import streamlit as st
import time
import random

# Function to estimate calories burned
def estimate_calories(workout_type, duration, heart_rate, weight, age, height, gender, body_temperature):
    MET_values = {
        "Running🏃": 9.8,
        "Cycling🚴🏻‍♀️": 7.5,
        "Swimming🏊": 7.0,
        "Walking🚶🏼": 3.8,
        "Yoga🧘": 2.5,
        "Weightlifting🏋‍♀": 6.0
    }

    MET = MET_values.get(workout_type, 4.0)

    # BMR calculation based on gender
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5  # Mifflin-St Jeor for male
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161  # Mifflin-St Jeor for female

    # Adjust based on body temperature
    temperature_factor = 1.1 if body_temperature > 37 else 1.0

    # Calories burned formula
    calories_burned = (bmr * MET * duration) / 1440 * temperature_factor
    return calories_burned

# Function to display workout summary
def display_workout_summary(workout_type, duration, calories, heart_rate, weight, height, age, gender, body_temperature):
    st.subheader("_Training Log_")
    st.write(f"**Workout Type❓:** {workout_type}")
    st.write(f"**Duration⏳:** {duration} minutes")
    st.write(f"**Calories Burned (Predicted)🔥:** {calories:.2f} kcal")
    st.write(f"**Heart Rate💓:** {heart_rate} bpm")
    st.write(f"**Weight⚖️:** {weight} kg")
    st.write(f"**Height🧍↕:** {height} cm")
    st.write(f"**Age🎂:** {age} years")
    st.write(f"**Gender⚤:** {gender}")
    st.write(f"**Body Temperature🌡️:** {body_temperature} °C")

# Function to generate personalized recommendations
def generate_recommendations(calories_burned, workout_type):
    recommendations = []
    if calories_burned > 500:
        recommendations.append("💡 You're doing great! Consider adding strength training to build muscle.")
    if workout_type == "Running🏃":
        recommendations.append("🏃‍♂️ Try interval running to boost endurance and burn more calories.")
    if workout_type == "Cycling🚴🏻‍♀️":
        recommendations.append("🚴🏻‍♀️ Push your limits with speed drills to improve your cycling performance.")
    if workout_type == "Swimming🏊":
        recommendations.append("🏊 Focus on your stroke technique to swim more efficiently.")
    if workout_type == "Walking🚶🏼":
        recommendations.append("🚶🏼 Track your steps to stay motivated and set new walking goals.")            
    if workout_type == "Yoga🧘":
        recommendations.append("🧘‍♀️ Incorporate advanced yoga poses to improve flexibility and strength.")
    if workout_type == "Weightlifting🏋‍♀":
        recommendations.append("🏋‍♀ Gradually increase weights to challenge your muscles and build strength")    
    return recommendations

# Function to award badges
def award_badges(calories_burned):
    badges = []
    if calories_burned > 3000:
        badges.append("💪 Fitness Warrior")
    if calories_burned > 2500:
        badges.append("🏋️‍♀️ Strength Prodigy")
    if calories_burned > 2000:
        badges.append("⚡️ Energy Dynamo")
    if calories_burned > 1500:
        badges.append("🌟 Health Hero")
    if calories_burned > 1000:
        badges.append("🏆 Calorie Crusher")
    if calories_burned > 500:
        badges.append("🔥 Burn Master")    
    return badges

# Streamlit app layout
st.set_page_config(page_title="AI-based Personal FitFusion", page_icon="🏋️", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stProgress>div>div>div {
        background-color: #4CAF50;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #2c3e50;
    }
    .stMarkdown p {
        color: #34495e;
    }
    .image-container {
        text-align: center;
        margin-top: 20px;
    }
    .title-container {
        background: rgba(0, 0, 0, 0.7); /* Semi-transparent black background */
        padding: 2px;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 3px;
    }
    .title-container h1 {
        color: white; /* White text for better visibility */
        font-size: 1.9rem;
        font-weight: bold;
    }
    .social-share {
        text-align: center;
        margin-top: 50px;
    }
    .social-share a {
        margin: 0 10px;
        text-decoration: none;
        color: #4CAF50;
        font-weight: bold;
    }
    .recommendations-container, .achievements-container {
        background: linear-gradient(135deg, #4CAF50, #2196F3);
        padding: 5px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .recommendations-container h2, .achievements-container h2 {
        background: linear-gradient(135deg, #4CAF50, #2196F3);
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin: -20px -20px 20px -20px; /* Extend to container edges */
    }
    .social-logo {
        width: 40px;
        height: 40px;
        margin: 0 10px;
    }
    .video-section {
        margin-top: 30px;
    }
    .video-section h2 {
        color: #2c3e50;
        text-align: center;
    }
    .video-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
    }
    .video-container iframe {
        margin: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Motivational Quotes
motivational_quotes = [
    "⚡️The harder you work for something, greater you’ll feel when you achieve it.",
    "🏋️‍♀️Push yourself because no one else is going to do it for you.",
    "🔥Don’t stop when you’re tired, stop when you’re done.",
    "💪Believe in yourself and all that you are.",
    "🎯Success starts with self-discipline.",
]

# Fitness Images
fitness_images = [
    "https://images.unsplash.com/photo-1594737625785-a6cbdabd333c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
    "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
    "https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
]

# Highlighted Title
st.markdown("""
    <div class="title-container">
        <h1>FitFusion: Track, Train, Transform</h1>
    </div>
""", unsafe_allow_html=True)

# Define the layout: two sections (left for motivational quotes, right for form)
col1, col2 = st.columns([1, 1])  # Two columns of equal width

# Left side (Motivational Quotes and Images)
with col1:
    st.markdown("<div class='quote-section'>", unsafe_allow_html=True)
    for quote in motivational_quotes:
        st.write(f"**{quote}**")
    st.markdown("</div>", unsafe_allow_html=True)

    # Display Fitness Images
    st.markdown("<div class='image-container'>", unsafe_allow_html=True)
    st.image(random.choice(fitness_images), width=400)
    st.markdown("</div>", unsafe_allow_html=True)

# Right side (Workout Form with transparent background)
with col2:
    with st.form(key='workout_form'):
        st.markdown("<div class='transparent-background'>", unsafe_allow_html=True)

        workout_type = st.selectbox("Select Exercise Type👇:", ["Running🏃", "Cycling🚴🏻‍♀️", "Swimming🏊", "Walking🚶🏼", "Yoga🧘", "Weightlifting🏋‍♀"])
        duration = st.number_input("Duration (in minutes)⏳:", min_value=1, step=1)
        heart_rate = st.number_input("Heart Rate (in bpm)💓:", min_value=30, max_value=200, step=1)
        weight = st.number_input("Weight (in kg)⚖️:", min_value=30, max_value=200, step=1)
        height = st.number_input("Height (in cm)🧍↕:", min_value=100, max_value=250, step=1)
        age = st.number_input("Age🎂:", min_value=1, max_value=120, step=1)
        gender = st.selectbox("Gender⚤:", ["Male", "Female", "Other"])
        body_temperature = st.number_input("Body Temperature🌡️:", min_value=30.0, max_value=45.0, step=0.1)

        submit_button = st.form_submit_button(label='Submit✔️')

        if submit_button:
            # Check if all fields are filled
            if workout_type and duration and heart_rate and weight and height and age and gender and body_temperature is not None:
                # Estimate calories burned based on the inputs and body temperature
                with st.spinner('Calculating calories burned...'):
                    time.sleep(2)  # Simulate some delay for calculation
                    calories_burned = estimate_calories(workout_type, duration, heart_rate, weight, age, height, gender, body_temperature)

                    # Display the workout summary and predicted calories
                    display_workout_summary(workout_type, duration, calories_burned, heart_rate, weight, height, age, gender, body_temperature)

                    # Show workout progress bar
                    st.progress(int(calories_burned) % 100)  # Show a progress bar based on calories

                    # Generate and display personalized recommendations
                    recommendations = generate_recommendations(calories_burned, workout_type)
                    if recommendations:
                        with col1:
                            st.markdown("<div class='recommendations-container'>", unsafe_allow_html=True)
                            st.markdown("<h2>Personalized Recommendations</h2>", unsafe_allow_html=True)
                            for rec in recommendations:
                                st.write(f"🌟 {rec}")
                            st.markdown("</div>", unsafe_allow_html=True)

                    # Award badges
                    badges = award_badges(calories_burned)
                    if badges:
                        with col1:
                            st.markdown("<div class='achievements-container'>", unsafe_allow_html=True)
                            st.markdown("<h2>Achievements</h2>", unsafe_allow_html=True)
                            for badge in badges:
                                st.write(f"🎖️ {badge}")
                            st.markdown("</div>", unsafe_allow_html=True)

                st.success("💪 Your workout details have been logged successfully!")
            else:
                st.error("Please fill in all fields before submitting.")

        st.markdown("</div>", unsafe_allow_html=True)  # Close the transparent background div

# Add a footer with social sharing options
st.markdown("""
    <div class="social-share">
        <h3>Share Your Progress</h3>
        <a href="https://twitter.com/intent/tweet?text=I%20just%20logged%20my%20workout%20on%20FitFusion!%20%F0%9F%8F%8B%EF%B8%8F" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Logo_of_Twitter.svg" alt="Twitter" class="social-logo">
        </a>
        <a href="https://www.facebook.com/sharer/sharer.php?u=https://fitfusion.com" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook" class="social-logo">
        </a>
        <a href="https://www.instagram.com/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram" class="social-logo">
        </a>
    </div>
""", unsafe_allow_html=True)

# Fitness YouTube Links Section
st.markdown("""
    <div class="video-section">
        <h3>Fitness Related Videos</h3>
        <p><b>Fitness Tips Videos:</b></p>
        <ul>
            <li><a href="https://www.youtube.com/watch?v=AzV3EA-1-yM" target="_blank">Workout Routine for Beginners</a></li>
            <li><a href="https://www.youtube.com/watch?v=kA8EpHvrt68" target="_blank">Beginners Workout for Weight Loss</a></li>
        </ul>
        <p><b>Fitness Diet Videos:</b></p>
        <ul>
            <li><a href="https://www.youtube.com/watch?v=XMcab1MFaLc" target="_blank">A healthy diet</a></li>
        </ul>
    </div>
""", unsafe_allow_html=True)

