# LotSpotter 🅿️

> GPS-Localization and Parking Reservation — KSU Capstone UC-492

## Overview

Atlanta dedicates **25% of its downtown land** to parking, yet drivers still struggle to find available spaces. LotSpotter solves this by automatically detecting available parking spaces and routing drivers to the nearest open spot via GPS — reducing the time, stress, and accident risk that comes with searching for parking.

**Presented at KSU Computing Showcase — Fall 2023**

## Team
| Name | Email |
|------|-------|
| Julian Yankah | jyankah3@students.kennesaw.edu |
| Tripp Greene | egreen60@students.kennesaw.edu |
| Ghislain Dongbou Temgoua | gdongbou@students.kennesaw.edu |
| Jonathan Perry | jperry44@students.kennesaw.edu |
| Henrry Pham | tpham64@students.kennesaw.edu |

**Advisor:** Prof. Yan Huang — Assistant Professor of Software Engineering, Kennesaw State University

## How It Works

```
Street Cameras / Sensors → AWS Pipeline → DynamoDB → React Native App → GPS Navigation
```

1. Cameras and sensors detect lot occupancy automatically, refreshing every 10 seconds
2. Availability data is synced to AWS DynamoDB in real time
3. Users open the app, search for parking near their destination
4. After selecting a spot (filtered by location, price, features), they reserve it
5. The app navigates them directly to the reserved spot via Google Maps integration

## Features
- 🅿️ Real-time parking availability, updated every 10 seconds
- 📍 GPS navigation to reserved spot via Google Maps
- 💳 Reserve spots with one tap — filtered by location, price, and features
- 👤 User accounts with reservation history
- 🏢 Business owner registration portal to list parking lots
- ♿ Designed with accessibility as a priority — minimal typing, button-tap interface

## Impact
- Reduces accident risk by cutting driving time spent searching for parking
- Boosts the local economy through better utilization of existing parking
- Eliminates driver stress and anxiety (missed flights, late appointments)
- Creates jobs in parking management and tech support

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Edge / CV | Python, OpenCV |
| Hardware | RaspberryPi 4 + Camera Module |
| Database | AWS DynamoDB |
| API | AWS API Gateway + Lambda |
| Mobile | React Native (iOS & Android) |
| Navigation | Google Maps API |

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- AWS CLI configured

### Installation
```bash
git clone https://github.com/yankah-julian/lot-spotter.git
cd lot-spotter

# Backend / edge setup
cd edge
pip install -r requirements.txt

# Mobile app
cd ../mobile
npm install
npx expo start
```

### Environment Variables
```env
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=us-east-1
DYNAMODB_TABLE=lotspotter-spaces
```

## Project Structure
```
lot-spotter/
├── edge/               # RaspberryPi detection scripts
│   ├── detect.py       # Main CV + sensor loop
│   ├── sensor.py       # Ultrasonic sensor driver
│   ├── sync.py         # DynamoDB sync client
│   └── requirements.txt
├── cloud/              # AWS Lambda + API Gateway
│   └── lambda_handler.py
├── mobile/             # React Native app (original)
└── docs/               # Architecture diagrams & capstone poster
```

## Future Roadmap
- Voice assistant and screen reader for accessibility
- Automatic car counter (increment/decrement as cars enter/exit) to eliminate the need for images when a lot is full

## References
- [Atlanta Parking Research — Jalopnik / Parking Reform Network](https://jalopnik.com/with-25-percent-of-its-downtown-dedicated-to-parking-a1851007864)

## License
MIT © Julian Yankah & Team
