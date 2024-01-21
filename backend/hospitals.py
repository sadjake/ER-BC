from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for hospitals and their wait times
hospitals = [
    {"name": "Vancouver General Hospital", "location": "920 West 10th Ave Vancouver, BC, V5Z 1M9", "phone-number": "(604) 875-4111", "wait_time": 30},
    {"name": "Richmond Hospital", "location": "7000 Westminster Highway Richmond, BC, V6X 1A2", "phone-number": "(604) 278-9711", "wait_time": 45},
    {"name": "St. Paul's Hospital", "location": "1081 Burrard St Vancouver, BC, V6Z 1Y6", "phone-number": "(604) 682-2344", "wait_time": 45},
    {"name": "Lions Gate Hospital", "location": "231 East 15th St North Vancouver, BC, V7L 2L7", "phone-number": "(604) 988-3131", "wait_time": 20},
    {"name": "Mount Saint Joseph Hospital", "location": "3080 Prince Edward St Vancouver, BC, V5T 3N4", "phone-number": "(604) 874-1141", "wait_time": 15},
    {"name": "UBC Hospital (UBCH)", "location": "2211 Wesbrook Mall Vancouver, BC, V6T 2B5", "phone-number": "(604) 822-7121", "wait_time": 20},
    {"name": "BC Children's Hospital", "location": "4480 Oak St Vancouver, BC, V6H 3V4", "phone-number": "(604) 875-2345", "wait_time": 30},
    {"name": "Sechelt Hospital", "location": "5544 Sunshine Coast Highway Sechelt, BC V0N 3A0", "phone-number": "(604) 885-2224", "wait_time": 30},
    {"name": "Abbotsford Regional Hospital", "location": "32900 Marshall Road Abbotsford, BC, V2S 0C2", "phone-number": "(604) 851-4700", "wait_time": 30},
    {"name": "Burnaby Hospital", "location": "3935 Kincaid St Burnaby, BC, V5G 2X6", "phone-number": "(604) 434-4211", "wait_time": 30},
    {"name": "Chilliwack General Hospital", "location": "45600 Menholm Rd Chilliwack, BC, V2P 1P7", "phone-number": "(604) 795-4141", "wait_time": 30},
    {"name": "Delta Hospital", "location": "5800 Mountain View Blvd Delta, BC, V4K 3V6", "phone-number": "(604) 946-1121", "wait_time": 30},
    {"name": "Eagle Ridge Hospital", "location": "475 Guildford Way Port Moody, BC, V3H 3W9", "phone-number": "(604) 461-2022", "wait_time": 30},
    {"name": "Langley Memorial Hospital", "location": "22051 Fraser Hwy Langley, BC, V3A 4H4", "phone-number": "(604) 514-6000", "wait_time": 30},
    {"name": "Peace Arch Hospital", "location": "15521 Russell Avenue White Rock, BC, V4B 2R4", "phone-number": "(604) 531-5512", "wait_time": 30},
    {"name": "Ridge Meadows Hospital", "location": "11666 Laity St Maple Ridge, BC, V2X 7G5", "phone-number": "(604) 463-4111", "wait_time": 30},
    {"name": "Squamish General Hospital", "location": "38140 Behrner Dr Squamish, BC, V8B 0J3", "phone-number": "(604) 892-5211", "wait_time": 30},
    {"name": "Surrey Memorial Hospital", "location": "13750 96th Ave Surrey, BC, V3V 1Z2", "phone-number": "(604) 581-2211", "wait_time": 30},
    {"name": "Royal Columbian Hospital", "location": "330 East Columbia St New Westminster, BC, V3L 3W7", "phone-number": "(604) 520-4253", "wait_time": 30},
    {"name": "qathet General Hospital", "location": "5000 Joyce Avenue Powell River, BC V8A 5R3", "phone-number": "(604) 485-3211", "wait_time": 30},
    {"name": "Pemberton Health Centre", "location": "1403 Portage Road Pemberton, BC, V0N 2L0", "phone-number": "(604) 894-6939", "wait_time": 30},
    {"name": "Surrey Whalley UPCC", "location": "9639 137a St Unit G2 Surrey, BC V3T 0M1", "phone-number": "(604) 572-2610", "wait_time": 30},
    {"name": "Ridge Meadows UPCC", "location": "121-11900 Haney Place Maple Ridge, BC V2X 8R9", "phone-number": "(604) 476-4650", "wait_time": 30},
    {"name": "Port Moody UPCC", "location": "3105 Murray St Port Moody, BC V3H 1X3", "phone-number": "(604) 469-3123", "wait_time": 30},
    {"name": "Metrotown UPCC", "location": "Unit 102 - 4555 Kingsway Burnaby, BC V5H 4T8", "phone-number": "(604) 451-4888", "wait_time": 30},
    {"name": "Edmonds UPCC", "location": "Unit 201, 7315 Edmonds St Burnaby, BC V3N 1A7", "phone-number": "(604) 519-3787", "wait_time": 30},
]

if __name__ == '__main__':
    app.run(debug=True)
