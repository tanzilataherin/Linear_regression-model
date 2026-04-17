import streamlit as st
import pandas as pd
import pickle

# Load the best model (replace with the actual best model filename)
# For example, if best_model_name was 'linear_regression', then filename is 'linear_regression_model.pkl'
try:
    # This should dynamically pick up the filename from the last saved model
    # In a real scenario, you would have a more robust way to get this filename.
    # For now, let's assume 'random_forest_regressor_model.pkl' as it's often a good performer.
    # If you saved a different model name, please update this variable accordingly.
    model_filename = 'random_forest_regressor_model.pkl' # Adjust if your best model was different
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)
    st.success(f"Successfully loaded {model_filename}")
except FileNotFoundError:
    st.error(f"Error: Model file '{model_filename}' not found. Please ensure the model is saved correctly and that its filename matches this script.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.title('Salary Prediction App')
st.write('Enter employee details to predict their salary.')

# Input fields for features
age = st.slider('Age', 18, 65, 30)
years_of_experience = st.slider('Years of Experience', 0, 40, 5)

gender = st.selectbox('Gender', ['Male', 'Female'])
education_level = st.selectbox('Education Level', ['Bachelor\'s', 'Master\'s', 'PhD'])
job_title = st.selectbox('Job Title', [
    'Software Engineer', 'Data Analyst', 'Senior Manager', 'Sales Associate', 'Director',
    'Marketing Manager', 'Product Manager', 'HR Manager', 'Financial Analyst', 'Sales Manager',
    'Research Scientist', 'Operations Manager', 'Project Manager', 'Software Developer',
    'Customer Service Rep', 'IT Support', 'UI/UX Designer', 'Accountant', 'Business Analyst',
    'Sales Director', 'VP of Marketing', 'Training Specialist', 'Creative Director', 'IT Manager',
    'Data Scientist', 'Graphic Designer', 'Financial Manager', 'HR Generalist',
    'Web Developer', 'Research Analyst', 'Legal Counsel', 'Content Creator', 'IT Architect',
    'Digital Marketing Specialist', 'PR Manager', 'Operations Analyst', 'Financial Advisor',
    'Help Desk Analyst', 'Social Media Manager', 'Recruiting Coordinator', 'Consultant',
    'Copywriter', 'Network Engineer', 'Product Designer', 'Data Entry Clerk', 'Business Dev Manager',
    'Teacher', 'Geologist', 'Surgeon', 'Physician', 'Dentist', 'Nurse', 'Chemist', 'Biologist',
    'Librarian', 'Photographer', 'Film Director', 'Architect', 'Urban Planner', 'Economist',
    'Statistician', 'Journalist', 'Artist', 'Writer', 'Editor', 'Translator', 'Musician',
    'Actor', 'Dancer', 'Pilot', 'Astronaut', 'Archaeologist', 'Historian', 'Psychologist',
    'Sociologist', 'Anthropologist', 'Political Scientist', 'Graphic Designer', 'Paralegal',
    'Veterinarian', 'Physical Therapist', 'Occupational Therapist', 'Speech Therapist',
    'Dietitian', 'Pharmacist', 'Medical Doctor', 'Surgeon', 'Anesthesiologist', 'Radiologist',
    'Pathologist', 'Dermatologist', 'Cardiologist', 'Neurologist', 'Psychiatrist', 'Endocrinologist',
    'Gastroenterologist', 'Pulmonologist', 'Nephrologist', 'Urologist', 'Oncologist',
    'Hematologist', 'Rheumatologist', 'Immunologist', 'Allergist', 'Infectious Disease Spec',
    'Emergency Physician', 'Pediatrician', 'Geriatrician', 'Family Physician',
    'General Practitioner', 'Optometrist', 'Chiropractor', 'Podiatrist', 'Massage Therapist',
    'Acupuncturist', 'Nutritionist', 'Yoga Instructor', 'Personal Trainer', 'Coach',
    'Sports Psychologist', 'Sports Agent', 'Athlete', 'Referee', 'Umpire', 'Scout',
    'Athletic Trainer', 'Sports Reporter', 'Commentator', 'Broadcaster', 'Producer',
    'Director', 'Editor', 'Cinematographer', 'Sound Engineer', 'Lighting Designer',
    'Set Designer', 'Costume Designer', 'Makeup Artist', 'Hair Stylist', 'Fashion Designer',
    'Jewelry Designer', 'Interior Designer', 'Landscape Architect', 'Civil Engineer',
    'Mechanical Engineer', 'Electrical Engineer', 'Aerospace Engineer', 'Chemical Engineer',
    'Environmental Engineer', 'Computer Engineer', 'Software Architect', 'DevOps Engineer',
    'Cloud Engineer', 'Cybersecurity Analyst', 'Network Administrator', 'Database Administrator',
    'Systems Administrator', 'Technical Writer', 'Scrum Master', 'Agile Coach',
    'Business Intelligence Analyst', 'Data Engineer', 'Machine Learning Engineer',
    'AI Engineer', 'Robotics Engineer', 'Quantum Engineer', 'Nanotechnologist',
    'Biomedical Engineer', 'Genetics Counselor', 'Epidemiologist', 'Biostatistician',
    'Public Health Specialist', 'Health Educator', 'Community Health Worker',
    'Social Worker', 'Case Manager', 'Counselor', 'Therapist', 'Psychotherapist',
    'Art Therapist', 'Music Therapist', 'Drama Therapist', 'Dance Therapist',
    'Recreational Therapist', 'Rehabilitation Counselor', 'School Counselor',
    'Career Counselor', 'Substance Abuse Counselor', 'Family Therapist',
    'Marriage Counselor', 'Child Psychologist', 'Educational Psychologist',
    'Industrial-Organizational Psychologist', 'Forensic Psychologist',
    'Clinical Psychologist', 'Research Psychologist', 'Experimental Psychologist',
    'Cognitive Scientist', 'Neuroscientist', 'Linguist', 'Anthropologist',
    'Archaeologist', 'Historian', 'Political Scientist', 'Sociologist',
    'Economist', 'Geographer', 'Urban Planner', 'Librarian', 'Archivist',
    'Curator', 'Museum Technician', 'Conservator', 'Restorer', 'Art Historian',
    'Music Historian', 'Film Historian', 'Theatre Historian', 'Literary Critic',
    'Poet', 'Novelist', 'Playwright', 'Screenwriter', 'Journalist', 'Editor',
    'Publisher', 'Literary Agent', 'Book Publicist', 'Proofreader', 'Copy Editor',
    'Technical Editor', 'Legal Editor', 'Medical Editor', 'Science Writer',
    'Travel Writer', 'Food Writer', 'Fashion Writer', 'Sports Writer',
    'Music Critic', 'Art Critic', 'Film Critic', 'Theatre Critic', 'Book Reviewer',
    'Columnist', 'Blogger', 'Vlogger', 'Podcaster', 'Content Strategist',
    'Social Media Strategist', 'SEO Specialist', 'SEM Specialist',
    'PPC Specialist', 'Affiliate Marketing Manager', 'Email Marketing Specialist',
    'Marketing Automation Specialist', 'Growth Hacker', 'Brand Manager',
    'Product Marketing Manager', 'Market Research Analyst', 'Competitor Analyst',
    'Public Relations Specialist', 'Event Manager', 'Fundraiser', 'Grant Writer',
    'Lobbyist', 'Policy Analyst', 'Government Relations Manager',
    'International Relations Specialist', 'Diplomat', 'Ambassador', 'Consul',
    'Intelligence Analyst', 'Military Officer', 'Police Officer',
    'Firefighter', 'Paramedic', 'Emergency Medical Technician',
    'Security Guard', 'Private Investigator', 'Detective', 'Forensic Scientist',
    'Criminologist', 'Lawyer', 'Judge', 'Paralegal', 'Legal Assistant',
    'Court Reporter', 'Mediator', 'Arbitrator', 'Patent Attorney',
    'Corporate Counsel', 'Public Defender', 'Prosecutor', 'Immigration Lawyer',
    'Family Lawyer', 'Criminal Lawyer', 'Civil Rights Lawyer',
    'Environmental Lawyer', 'Real Estate Lawyer', 'Tax Lawyer',
    'Estate Planning Attorney', 'Intellectual Property Lawyer',
    'Labor Lawyer', 'Bankruptcy Lawyer', 'Mergers and Acquisitions Lawyer'
])


if st.button('Predict Salary'):
    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        'Age': [age],
        'Years of Experience': [years_of_experience],
    })

    # One-hot encode categorical features similar to training data
    # In a real scenario, you would save the list of all columns after one-hot encoding during training
    # and use it here to ensure consistency.

    # Create an empty DataFrame with all expected columns and fill with zeros
    # This assumes 'X' (the features dataframe used for training) is available or its columns are known.
    # For this to work correctly, `X` should be accessible or its column names should be hardcoded
    # or loaded from a separate file (e.g., a JSON file containing column names).
    # If `X` is not available, replace `X.columns` with the actual list of all feature columns
    # after one-hot encoding during your training process.
    try:
        all_columns = X.columns # Assuming X is the original encoded dataframe used for training
    except NameError:
        st.error("Error: `X` (the training features dataframe) is not defined. Please ensure the cells creating `X` and performing one-hot encoding are run.")
        st.stop()

    processed_input = pd.DataFrame(0, index=[0], columns=all_columns)

    # Fill in the numerical values
    processed_input['Age'] = age
    processed_input['Years of Experience'] = years_of_experience

    # Fill in the one-hot encoded categorical values
    # Gender
    if gender == 'Female':
        if 'Gender_Female' in processed_input.columns: # Check if column exists
            processed_input['Gender_Female'] = 1
    # Handle 'Other' if it was a category in your original dataset and used for training
    # elif gender == 'Other':
    #     if 'Gender_Other' in processed_input.columns:
    #         processed_input['Gender_Other'] = 1

    # Education Level
    if education_level == 'Master\'s':
        if 'Education Level_Master\'s' in processed_input.columns:
            processed_input['Education Level_Master\'s'] = 1
    elif education_level == 'PhD':
        if 'Education Level_PhD' in processed_input.columns:
            processed_input['Education Level_PhD'] = 1

    # Job Title (this will be long, so ensure it matches the trained model's columns)
    job_title_col = f'Job Title_{job_title}'
    if job_title_col in processed_input.columns:
        processed_input[job_title_col] = 1
    else:
        st.warning(f"Job Title '{job_title}' not recognized by the model. Prediction might be inaccurate. Ensure all job titles are present in the app's selectbox and matched with training data.")

    try:
        prediction = model.predict(processed_input)
        st.success(f'Predicted Salary: ${prediction[0]:,.2f}')
    except Exception as e:
        st.error(f"Error during prediction: {e}. Make sure the input features match the model's expected features (e.g., number of columns and their names).")
