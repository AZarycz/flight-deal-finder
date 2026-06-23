# CHEAP FLIGHT FINDER

## Overview
An application that sends SMS notifications about cheap flights within a specified 
travel period to destinations defined in a Google Sheet.

It searches for flights via [SerpAPI](https://serpapi.com/), compares prices with 
the lowest price defined in the Google Sheet, and alerts the user when a cheaper 
flight is found. The Google Sheet is then updated with the new lowest price.

SMS notifications are sent via [Twilio](https://www.twilio.com). 
Google Sheet communication is handled via [Sheety](https://sheety.co/).

## Tech Stack
- **Python**
- **SerpAPI** – fetching flight data from Google Flights
- **Sheety** – reading and updating Google Sheets via API
- **Twilio** – sending SMS notifications
- **requests-cache** – caching API responses to preserve free plan limits
- **GitHub Actions** – scheduled automatic runs every 4 days

## Setup
1. Clone the repository
    https://github.com/AZarycz/flight-deal-finder.git

2. Install dependencies
```
   pip install -r requirements.txt
```
3. Create a `.env` file in the root directory and fill in your credentials:
    `SHEETY_TOKEN=`
    `SHEETY_ENDPOINT=`
    `SERP_API_KEY=`
    `ACCOUNT_SID=`
    `AUTH_TOKEN_TWILIO=`
    `TWILIO_FROM=`
    `TWILIO_TO=`


4. Set up your Google Sheet with the following columns:
   - `city`
   - `iataCode`
   - `lowestPrice`

5. Run the script
```bash
   python main.py
```

## SMS Notification Example

<img width="1080" height="1219" alt="Screenshot_20260623_052431_Messages" src="https://github.com/user-attachments/assets/95b42630-ee2e-42e2-bbef-723358b1c8ab" />
