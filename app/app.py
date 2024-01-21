from threading import Lock
from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO, emit
import requests
import datetime

from form.forms import PatientRegistrationForm
from wait_time.wait_time import WaitTime
from hospitals.hospitals import hospitals

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'secret_key'

async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

@app.route('/')
def index():
    return render_template('index.html', hospitals=hospitals)

@app.route('/hospital/<string:hospital_id>')
def hospital_detail(hospital_id):
    hospital = next((h for h in hospitals if h["id"] == hospital_id), None)
    if hospital:
        return render_template('hospital.html', hospital=hospital)
    else:
        return "Hospital not found", 404

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    form = PatientRegistrationForm()

    if form.validate_on_submit():
        print("Form submitted with the following data:")
        print("First Name:", form.first_name.data)
        print("Last Name:", form.last_name.data)
        print("Date of Birth:", form.date_of_birth.data)
        print("Gender:", form.gender.data)
        print("Address:", form.address.data)
        print("Phone Number:", form.phone_number.data)
        print("Emergency Contact Name:", form.emergency_contact_name.data)
        print("Emergency Contact Phone:", form.emergency_contact_phone.data)
        print("Insurance Provider:", form.insurance_provider.data)
        print("Policy Number:", form.policy_number.data)
        print("Group Number:", form.group_number.data)
        print("Allergies:", form.allergies.data)
        print("Medications:", form.medications.data)
        print("Pre-existing Conditions:", form.pre_existing_conditions.data)
        print("Past Surgeries:", form.past_surgeries.data)
        print("Primary Care Physician:", form.primary_care_physician.data)
        print("Brief Description of Emergency:", form.brief_description_of_emergency.data)
        print("Symptoms:", form.symptoms.data)
        print("Time of Onset:", form.time_of_onset.data)
        print("Consent for Treatment:", form.consent_for_treatment.data)
        print("Financial Responsibility:", form.financial_responsibility.data)
        print("Patient Signature:", form.patient_signature.data)
        print("Date and Time of Arrival:", form.date_and_time_of_arrival.data)

        # redirect to another page or render a confirmation page
        return redirect(url_for('confirmation_page'))

    # if form validation fails or there are errors, render the form page again
    return render_template('patient_registration.html', form=form)

@app.route('/confirmation')
def confirmation_page():
    # render a confirmation page or redirect to another page
    return render_template('confirmation.html')

@app.route('/hospital')
def hospital_page():
    # render a hospital page or redirect to another page
    return render_template('hospital.html', hospitals=hospitals)



wait_times = []
for hospital_data in hospitals:
    wait_times.append(WaitTime(hosp_id=hospital_data["id"], hospital_name=hospital_data["name"], wait_time=hospital_data["wait_time"]))

def wait_times_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        
        socketio.sleep(5)
        count += 1
        data = {}
        for wait_time_data in wait_times:
            data[wait_time_data.get_id()] = wait_time_data.get_data()

        socketio.emit('wait_time_update',
                      {'data': data})

@socketio.on('connect')
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(wait_times_thread)
    data = {}
    for wait_time_data in wait_times:
        data[wait_time_data.get_id()] = wait_time_data.get_data()
    emit('connected', {'data': data})

if __name__ == '__main__':
    socketio.run(app, debug=True)