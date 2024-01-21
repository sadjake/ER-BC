from wtforms import StringField, DateField, SelectField, TextAreaField, IntegerField, BooleanField, SubmitField, validators
from flask_wtf import FlaskForm

class PatientRegistrationForm(FlaskForm):
    # Personal Information
    first_name = StringField('First Name: ', validators=[validators.DataRequired()])
    last_name = StringField('Last Name: ', validators=[validators.DataRequired()])
    date_of_birth = DateField('Date of Birth: ', format='%Y-%m-%d', validators=[validators.DataRequired()])
    gender = SelectField('Gender: ', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[validators.DataRequired()])

    # Contact Information
    address = StringField('Address: ', validators=[validators.DataRequired()])
    phone_number = StringField('Phone Number: ', validators=[validators.DataRequired()])
    emergency_contact_name = StringField('Emergency Contact Name: ', validators=[validators.DataRequired()])
    emergency_contact_phone = StringField('Emergency Contact Phone: ', validators=[validators.DataRequired()])

    # Insurance Information
    insurance_provider = StringField('Insurance Provider: ')
    policy_number = StringField('Policy Number: ')
    group_number = StringField('Group Number: ')

    # Medical History
    allergies = StringField('Allergies: ')
    medications = StringField('Medications: ')
    pre_existing_conditions = StringField('Pre-existing Conditions: ')
    past_surgeries = StringField('Past Surgeries: ')
    primary_care_physician = StringField('Primary Care Physician: ')

    # Emergency Information
    brief_description_of_emergency = TextAreaField('Brief Description of Emergency: xs', validators=[validators.DataRequired()])
    symptoms = TextAreaField('Symptoms: ', validators=[validators.DataRequired()])
    time_of_onset = StringField('Time of Onset: ', validators=[validators.DataRequired()])

    # Consent and Agreement
    consent_for_treatment = BooleanField('Consent for Treatment: ', validators=[validators.DataRequired()])
    financial_responsibility = BooleanField('Financial Responsibility: ', validators=[validators.DataRequired()])

    # Signature
    patient_signature = StringField('Patient Signature', validators=[validators.DataRequired()])

    # Date and Time
    date_and_time_of_arrival = StringField('Date and Time of Arrival: ', validators=[validators.DataRequired()])

    # Submit
    submit = SubmitField('Submit')