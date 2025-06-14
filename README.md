# Webscraping Alternatives for RAG LLM

## Current Implementation
- Takes screenshots of webpage
- Uses OCR (Optical character recognition) on PDFs
However, for dropdown elements and others, this method can yield inconsistent results.

## New Implementation  
- Leverages Firefox browser's accessibility mode through a js library called "readibility"
- Extracts text from the accessibility mode in a cleaner and summarized format 
- Overall simpler and less computationally expensive

Currently, the selenium-readibility.py script outputs 2 .txt files in an "output" directory, one of the old implementation and one of the new, for the same specified url.


### Current Output for URL: https://flypittsburgh.com/pittsburgh-international-airport/parking/#parking-options
> ```Parking - Fly Pittsburgh Skip To Navigation Skip To Content Skip To Footer Open Accessibility Sidebar Close Reset Sidebar Settings Sidebar Size 1 2 3 4 5 Sidebar Position Left Right Sidebar Language English العربية বাংলা Dansk Deutsch Español Français עִבְרִית हिन्दी Bahasa Indonesia Italiano 日本語 한국어 Nederlands Português Русский 简体中文 Hide Sidebar Once Session Day Week Hide Now Hide the sidebar until the page is refreshed. Accessibility Profiles Accessibility Profile None Blindness Color Blindness Visual Impairment Motor Impairment Cognitive Disability Seizures & Epilepsy Dyslexia ADHD Select an accessibility profile. Screen Reader Screen Reader Mode Screen Reader Speed Slow Medium Fast Screen Reader Voice Use system default Match to sidebar language Albert (en-US) Bad News (en-US) Bahh (en-US) Bells (en-US) Boing (en-US) Bubbles (en-US) Cellos (en-US) Wobble (en-US) Eddy (English (US)) (en-US) Flo (English (US)) (en-US) Fred (en-US) Good News (en-US) Grandma (English (US)) (en-US) Grandpa (English (US)) (en-US) Jester (en-US) Junior (en-US) Kathy (en-US) Organ (en-US) Superstar (en-US) Ralph (en-US) Reed (English (US)) (en-US) Rocko (English (US)) (en-US) Samantha (en-US) Sandy (English (US)) (en-US) Shelley (English (US)) (en-US) Trinoids (en-US) Whisper (en-US) Zarvox (en-US) Alice (it-IT) Eddy (Italian (Italy)) (it-IT) Flo (Italian (Italy)) (it-IT) Grandma (Italian (Italy)) (it-IT) Grandpa (Italian (Italy)) (it-IT) Reed (Italian (Italy)) (it-IT) Rocko (Italian (Italy)) (it-IT) Sandy (Italian (Italy)) (it-IT) Shelley (Italian (Italy)) (it-IT) Alva (sv-SE) Amélie (fr-CA) Eddy (French (Canada)) (fr-CA) Flo (French (Canada)) (fr-CA) Grandma (French (Canada)) (fr-CA) Grandpa (French (Canada)) (fr-CA) Reed (French (Canada)) (fr-CA) Rocko (French (Canada)) (fr-CA) Sandy (French (Canada)) (fr-CA) Shelley (French (Canada)) (fr-CA) Amira (ms-MY) Anna (de-DE) Eddy (German (Germany)) (de-DE) Flo (German (Germany)) (de-DE) Grandma (German (Germany)) (de-DE) Grandpa (German (Germany)) (de-DE) Reed (German (Germany)) (de-DE) Rocko (German (Germany)) (de-DE) Sandy (German (Germany)) (de-DE) Shelley (German (Germany)) (de-DE) Carmit (he-IL) Damayanti (id-ID) Daniel (en-GB) Eddy (English (UK)) (en-GB) Flo (English (UK)) (en-GB) Grandma (English (UK)) (en-GB) Grandpa (English (UK)) (en-GB) Reed (English (UK)) (en-GB) Rocko (English (UK)) (en-GB) Sandy (English (UK)) (en-GB) Shelley (English (UK)) (en-GB) Daria (bg-BG) Eddy (Spanish (Spain)) (es-ES) Flo (Spanish (Spain)) (es-ES) Grandma (Spanish (Spain)) (es-ES) Grandpa (Spanish (Spain)) (es-ES) Mónica (es-ES) Reed (Spanish (Spain)) (es-ES) Rocko (Spanish (Spain)) (es-ES) Sandy (Spanish (Spain)) (es-ES) Shelley (Spanish (Spain)) (es-ES) Eddy (Spanish (Mexico)) (es-MX) Flo (Spanish (Mexico)) (es-MX) Grandma (Spanish (Mexico)) (es-MX) Grandpa (Spanish (Mexico)) (es-MX) Paulina (es-MX) Reed (Spanish (Mexico)) (es-MX) Rocko (Spanish (Mexico)) (es-MX) Sandy (Spanish (Mexico)) (es-MX) Shelley (Spanish (Mexico)) (es-MX) Eddy (Finnish (Finland)) (fi-FI) Flo (Finnish (Finland)) (fi-FI) Grandma (Finnish (Finland)) (fi-FI) Grandpa (Finnish (Finland)) (fi-FI) Reed (Finnish (Finland)) (fi-FI) Rocko (Finnish (Finland)) (fi-FI) Sandy (Finnish (Finland)) (fi-FI) Satu (fi-FI) Shelley (Finnish (Finland)) (fi-FI) Eddy (French (France)) (fr-FR) Flo (French (France)) (fr-FR) Grandma (French (France)) (fr-FR) Grandpa (French (France)) (fr-FR) Jacques (fr-FR) Rocko (French (France)) (fr-FR) Sandy (French (France)) (fr-FR) Shelley (French (France)) (fr-FR) Thomas (fr-FR) Eddy (Japanese (Japan)) (ja-JP) Flo (Japanese (Japan)) (ja-JP) Grandma (Japanese (Japan)) (ja-JP) Grandpa (Japanese (Japan)) (ja-JP) Kyoko (ja-JP) Reed (Japanese (Japan)) (ja-JP) Rocko (Japanese (Japan)) (ja-JP) Sandy (Japanese (Japan)) (ja-JP) Shelley (Japanese (Japan)) (ja-JP) Eddy (Korean (South Korea)) (ko-KR) Flo (Korean (South Korea)) (ko-KR) Grandma (Korean (South Korea)) (ko-KR) Grandpa (Korean (South Korea)) (ko-KR) Reed (Korean (South Korea)) (ko-KR) Rocko (Korean (South Korea)) (ko-KR) Sandy (Korean (South Korea)) (ko-KR) Shelley (Korean (South Korea)) (ko-KR) Yuna (ko-KR) Eddy (Portuguese (Brazil)) (pt-BR) Flo (Portuguese (Brazil)) (pt-BR) Grandma (Portuguese (Brazil)) (pt-BR) Grandpa (Portuguese (Brazil)) (pt-BR) Luciana (pt-BR) Reed (Portuguese (Brazil)) (pt-BR) Rocko (Portuguese (Brazil)) (pt-BR) Sandy (Portuguese (Brazil)) (pt-BR) Shelley (Portuguese (Brazil)) (pt-BR) Eddy (Chinese (China mainland)) (zh-CN) Flo (Chinese (China mainland)) (zh-CN) Grandma (Chinese (China mainland)) (zh-CN) Grandpa (Chinese (China mainland)) (zh-CN) Reed (Chinese (China mainland)) (zh-CN) Rocko (Chinese (China mainland)) (zh-CN) Sandy (Chinese (China mainland)) (zh-CN) Shelley (Chinese (China mainland)) (zh-CN) Tingting (zh-CN) Eddy (Chinese (Taiwan)) (zh-TW) Flo (Chinese (Taiwan)) (zh-TW) Grandma (Chinese (Taiwan)) (zh-TW) Grandpa (Chinese (Taiwan)) (zh-TW) Meijia (zh-TW) Reed (Chinese (Taiwan)) (zh-TW) Rocko (Chinese (Taiwan)) (zh-TW) Sandy (Chinese (Taiwan)) (zh-TW) Shelley (Chinese (Taiwan)) (zh-TW) Ellen (nl-BE) Ioana (ro-RO) Joana (pt-PT) Kanya (th-TH) Karen (en-AU) Lana (hr-HR) Laura (sk-SK) Lekha (hi-IN) Lesya (uk-UA) Linh (vi-VN) Majed (ar-001) Tünde (hu-HU) Melina (el-GR) Milena (ru-RU) Moira (en-IE) Montse (ca-ES) Nora (nb-NO) Rishi (en-IN) Sara (da-DK) Sinji (zh-HK) Tessa (en-ZA) Tina (sl-SI) Xander (nl-NL) Yelda (tr-TR) Zosia (pl-PL) Zuzana (cs-CZ) Select a screen reader mode. Navigation Tools Large Cursor Black White Focus Ring Focus Ring Page Structure Headings Landmarks Links Select a tab to view the page structure. No headings found. No landmarks found. No links found. Reading Tools Tooltip Small Medium Large Reading Guide Small Medium Large Reading Mask Small Medium Large Text Tools Text Font Sans-Serif Dyslexic Text Size Line Height Text Spacing Text Alignment Graphics Tools Color Saturation None Low High Color Contrast Invert Dark Light Hide Images Hide Images Created by Divi-Modules ... PITTSBURGH INTERNATIONAL AIRPORT ALLEGHENY COUNTY AIRPORT AIRPORT AUTHORITY PITTSBURGH INTERNATIONAL AIRPORT ALLEGHENY COUNTY AIRPORT AIRPORT AUTHORITY Flights Flight Status Nonstop Destinations Airlines Parking Parking Options Pre-Book Parking Accessible Parking Request a Receipt Security Current Wait Times Prohibited Items Real ID TSA Travel Tips Medication Accessibility Accessible, Adult and Family Restrooms Wheelchair Assistance Mother’s Nursing Lounge Sensory Room Airport Ambassador Escorts Sunflower Program Pet Relief Areas Grievance Procedure Terminal Info Interactive Airport Map International Travel Eat, Shop & More Arts & Culture Ground Transportation Car Rental Ride Sharing Public Transportation Vehicles for Hire Access ADA Paratransit Contact Us FAQs Flights Flight Status Nonstop Destinations Airlines Parking Parking Options Pre-Book Parking Accessible Parking Request a Receipt Security Current Wait Times Prohibited Items Real ID TSA Travel Tips Medication Accessibility Accessible, Adult and Family Restrooms Wheelchair Assistance Mother’s Nursing Lounge Sensory Room Airport Ambassador Escorts Sunflower Program Pet Relief Areas Grievance Procedure Terminal Info Interactive Airport Map International Travel Eat, Shop & More Arts & Culture Ground Transportation Car Rental Ride Sharing Public Transportation Vehicles for Hire Access ADA Paratransit Contact Us FAQs PITTSBURGH INTERNATIONAL AIRPORT ALLEGHENY COUNTY AIRPORT AIRPORT AUTHORITY PITTSBURGH INTERNATIONAL AIRPORT ALLEGHENY COUNTY AIRPORT AIRPORT AUTHORITY Flights Flight Status Nonstop Destinations Airlines Parking Parking Options Pre-Book Parking Accessible Parking Request a Receipt Security Current Wait Times Prohibited Items Real ID TSA Travel Tips Medication Accessibility Accessible, Adult and Family Restrooms Wheelchair Assistance Mother’s Nursing Lounge Sensory Room Airport Ambassador Escorts Sunflower Program Pet Relief Areas Grievance Procedure Terminal Info Interactive Airport Map International Travel Eat, Shop & More Arts & Culture Ground Transportation Car Rental Ride Sharing Public Transportation Vehicles for Hire Access ADA Paratransit Contact Us FAQs Flights Flight Status Nonstop Destinations Airlines Parking Parking Options Pre-Book Parking Accessible Parking Request a Receipt Security Current Wait Times Prohibited Items Real ID TSA Travel Tips Medication Accessibility Accessible, Adult and Family Restrooms Wheelchair Assistance Mother’s Nursing Lounge Sensory Room Airport Ambassador Escorts Sunflower Program Pet Relief Areas Grievance Procedure Terminal Info Interactive Airport Map International Travel Eat, Shop & More Arts & Culture Ground Transportation Car Rental Ride Sharing Public Transportation Vehicles for Hire Access ADA Paratransit Contact Us FAQs PIT AGC ACAA PIT AGC ACAA Flights Flight Status Nonstop Destinations Airlines Parking Parking Options Pre-Book Parking Accessible Parking Request a Receipt Security Current Wait Times Prohibited Items Real ID TSA Travel Tips Medication Accessibility Accessible, Adult and Family Restrooms Wheelchair Assistance Mother’s Nursing Lounge Sensory Room Airport Ambassador Escorts Sunflower Program Pet Relief Areas Grievance Procedure Terminal Info Interactive Airport Map International Travel Eat, Shop & More Arts & Culture Ground Transportation Car Rental Ride Sharing Public Transportation Vehicles for Hire Access ADA Paratransit Contact Us FAQs Flights Flight Status Nonstop Destinations Airlines Parking Parking Options Pre-Book Parking Accessible Parking Request a Receipt Security Current Wait Times Prohibited Items Real ID TSA Travel Tips Medication Accessibility Accessible, Adult and Family Restrooms Wheelchair Assistance Mother’s Nursing Lounge Sensory Room Airport Ambassador Escorts Sunflower Program Pet Relief Areas Grievance Procedure Terminal Info Interactive Airport Map International Travel Eat, Shop & More Arts & Culture Ground Transportation Car Rental Ride Sharing Public Transportation Vehicles for Hire Access ADA Paratransit Contact Us FAQs Parking Pittsburgh International Airport offers five convenient on-site parking options for all passengers and budgets. Parking Options 2161 SPACES Economy $13.00 Daily 10-20 minute walk to terminal Closed 1311 SPACES Extended (first hour is free) $15.00 Daily 5-10 minute shuttle to terminal Closed 999 SPACES Long Term $20.00 Daily 5-10 minute walk to terminal Closed 753 SPACES Short Term $36.00 Daily 1-5 minute walk to terminal Closed PIT Executive 2-5 min walk to terminal × Loading... Half Hour: Daily Max: Monthly Max: GET DIRECTIONS RESERVE NOW Reserve online to save vs. posted rates Book early to maximize savings Pre-Book Parking Make a reservation ahead of time to get the lowest possible price and ensure availability in your preferred lot. Enter and exit faster by scanning your QR code. Enter your travel dates and parking times below to calculate pricing and lock in your reservation. Additional Parking Information Accessible Parking All on-site parking lots have ample accessible parking, including van accessible spots. They are close to the terminal, moving walkway and shuttle stops. Click the button below to see where they are located in each lot. VIEW MAP EV Charging Stations FREE EV charging is offered to parking patrons in several locations: Ten stations in Long Term (Sections 8A, 8B) Six stations on the top level of Short Term garage (Sections 40C, 41C) Four stations on the second level of Short Term garage (Sections 24A, 24B, 24C, 24D) Click the button below to see where they are located. VIEW MAP Hyatt Regency Guests The hotel has limited parking next to the ground-level entrance on Airport Boulevard for those checking in and out. Overnight guests and event attendees are advised to park in sections 2-8 of the adjacent Long Term lot and access the hotel lobby via the moving walkway or the rear entrance to the hotel. Pay Stations Pay stations offer a convenient payment option and can be found on either end of the moving walkway between the terminal and parking lots. They accept cash, major credit cards and contactless payments. Click the button below to see where they are located. VIEW MAP PIT Express Pass Pay for parking on-the-fly by using a transponder tag – just like on the Turnpike. Already have an E-ZPass? It can be registered to serve as your PIT Express Pass as well. Click the button below for more information. LEARN MORE Oversized vehicles Parking of oversized vehicles and trailers is prohibited in the on-site lots at PIT. This includes, but is not limited to, occupying more than one parking space and obstructing lot traffic. Violators are subject to citation, additional fees and/or towing at the owner’s expense. Click the button below for additional details. VIEW POLICIES Parking Shuttle PIT operates a fleet of shuttles to move passengers between the Extended lot and the terminal as quickly and conveniently as possible. 9 Shuttles pick up at each shelter roughly every ten minutes 9 The shuttles are exclusive to the Extended parking lot. There are no shuttles for Short Term, Long Term, or PIT Executive lots 9 Shuttles operate 24/7/365, including holidays 9 Every shuttle is wheelchair accessible with an integrated lift 9 Drivers are available to assist with loading and unloading of luggage 9 Vehicles are frequently cleaned and sanitized for your safety and comfort 9 Those with mobility challenges can request assistance in several ways: Use the ‘Call’ button on gate terminals Use the intercoms at parking facilities, shuttle shelters and pay stations Dial 412-472-5050 Request a Parking Receipt Parking Receipt Name * Email Address * License Plate Number * Exit Date * Amount Paid * Last 4 Digits of Credit Card * Payment Process (choose one of the following) * Make selection Online Reservation PIT Express Pass Gate Ticket SUBMIT REQUEST If you are human, leave this field blank.  (412) 472-3525  info@flypittsburgh.com  1000 Airport Blvd, Pittsburgh, PA 15231 Resources PIT TRANSFORMED VISIT PITTSBURGH CAREERS FAQs CONTACT US Pittsburgh International Airport FLIGHTS PARKING SECURITY ACCESSIBILITY Allegheny County Airport BUSINESS OPPORTUNITIES AERONAUTICAL INFO LANDING FEES Airport Authority CAREER OPPORTUNITIES BUSINESS OPPORTUNITIES AIRPORT BADGING REPORTS @ 2025 Allegheny County Airport Authority Privacy Policy  (412) 472-3525  info@flypittsburgh.com  1000 Airport Blvd, Pittsburgh, PA 15231 Resources PIT TRANSFORMED VISIT PITTSBURGH CAREERS FAQs CONTACT US Pittsburgh International Airport FLIGHTS PARKING SECURITY ACCESSIBILITY Allegheny County Airport BUSINESS OPPORTUNITIES AERONAUTICAL INFO LANDING FEES Airport Authority CAREER OPPORTUNITIES BUSINESS OPPORTUNITIES AIRPORT BADGING REPORTS @ 2025 Allegheny County Airport Authority Privacy Policy Chat with PIT Hi! I’m Skylar, PIT’s virtual assistant. I’m here to answer any questions you have about the airport. How can I help you today? Generated by AI - verify all information with the source links provided. This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply | Disclaimer | Powered by Cognistx Disclaimer × This chat feature is powered by artificial intelligence, and as such, both the chatbot and its outputs may have limitations or contain inaccuracies. The output generated by the chatbot is therefore provided “as-is” and on an “as and when available” basis. Any actions you take using the outputs are at your own risk. Cognistx and FlyPitt disclaims all liability for any losses or damages arising or resulting from your use of, or reliance on, the chatbot and/or its outputs. The chatbot does not have the authority to bind Cognistx to any course of action or activity, including but not limited to activation or reactivation of service, refunds, account balance changes, payment plans, or deposit amounts. By using the FlyPitt chatbot, you acknowledge and agree to these terms. Thanks for your feedback! Would you be willing to help us a little bit more? × Please select an relevant option below. (This is optional) This field is required 0 / 1000 Cancel No thanks Submit Thanks for your feedback! × 1 Hi! I’m Skylar, your guide to Pittsburgh International Airport. Ask me anything! ×```

### New Implementation Output for URL: https://flypittsburgh.com/pittsburgh-international-airport/parking/#parking-options
```
Pittsburgh International Airport offers five convenient on-site parking options for all passengers and budgets.
Parking Options
10-20 minute walk to terminal
Extended (first hour is free)
$15.00 Daily
5-10 minute shuttle to terminal
5-10 minute walk to terminal
1-5 minute walk to terminal
PIT Executive
2-5 min walk to terminal
×
Loading...
Half Hour:
Daily Max:
Monthly Max:
Additional Parking Information
All on-site parking lots have ample accessible parking, including van accessible spots. They are close to the terminal, moving walkway and shuttle stops.
Click the button below to see where they are located in each lot.FREE EV charging is offered to parking patrons in several locations:
Ten stations in Long Term (Sections 8A, 8B)
Six stations on the top level of Short Term garage (Sections 40C, 41C)
Four stations on the second level of Short Term garage (Sections 24A, 24B, 24C, 24D)
Click the button below to see where they are located.
The hotel has limited parking next to the ground-level entrance on Airport Boulevard for those checking in and out. Overnight guests and event attendees are advised to park in sections 2-8 of the adjacent Long Term lot and access the hotel lobby via the moving walkway or the rear entrance to the hotel.
Pay stations offer a convenient payment option and can be found on either end of the moving walkway between the terminal and parking lots. They accept cash, major credit cards and contactless payments.
Click the button below to see where they are located.
Pay for parking on-the-fly by using a transponder tag – just like on the Turnpike. Already have an E-ZPass? It can be registered to serve as your PIT Express Pass as well. Click the button below for more information.
Parking of oversized vehicles and trailers is prohibited in the on-site lots at PIT. This includes, but is not limited to, occupying more than one parking space and obstructing lot traffic. Violators are subject to citation, additional fees and/or towing at the owner’s expense.
Click the button below for additional details.
Parking Shuttle
PIT operates a fleet of shuttles to move passengers between the Extended lot and the terminal as quickly and conveniently as possible.
Shuttles pick up at each shelter roughly every ten minutes
The shuttles are exclusive to the Extended parking lot. There are no shuttles for Short Term, Long Term, or PIT Executive lots
Shuttles operate 24/7/365, including holidays
Every shuttle is wheelchair accessible with an integrated lift
Drivers are available to assist with loading and unloading of luggage
Vehicles are frequently cleaned and sanitized for your safety and comfort
Those with mobility challenges can request assistance in several ways:
Use the ‘Call’ button on gate terminals
Use the intercoms at parking facilities, shuttle shelters and pay stations
Dial 412-472-5050
Request a Parking Receipt
```


### Current Output for URL: https://flypittsburgh.com/pittsburgh-international-airport/terminal-info/eat-shop-more/

>```Eat, Shop & More - Fly Pittsburgh Skip To Navigation Skip To Content Skip To Footer Open Accessibility Sidebar Close Reset Sidebar Settings Sidebar Size 1 2 3 4 5 Sidebar Position Left Right Sidebar Language English العربية বাংলা Dansk Deutsch Español Français עִבְרִית हिन्दी Bahasa Indonesia Italiano 日本語 한국어 Nederlands Português Русский 简体中文 Hide Sidebar Once Session Day Week Hide Now Hide the sidebar until the page is refreshed. Accessibility Profiles Accessibility Profile None Blindness Color Blindness Visual Impairment Motor Impairment Cognitive Disability Seizures & Epilepsy Dyslexia ADHD Select an accessibility profile. Screen Reader Screen Reader Mode Screen Reader Speed Slow Medium Fast Screen Reader Voice Use system default Match to sidebar language Albert (en-US) Bad News (en-US) Bahh (en-US) Bells (en-US) Boing (en-US) Bubbles (en-US) Cellos (en-US) Wobble (en-US) Eddy (English (US)) (en-US) Flo (English (US)) (en-US) Fred (en-US) Good News (en-US) Grandma (English (US)) (en-US) Grandpa (English (US)) (en-US) Jester (en-US) Junior (en-US) Kathy (en-US) Organ (en-US) Superstar (en-US) Ralph (en-US) Reed (English (US)) (en-US) Rocko (English (US)) (en-US) Samantha (en-US) Sandy (English (US)) (en-US) Shelley (English (US)) (en-US) Trinoids (en-US) Whisper (en-US) Zarvox (en-US) Alice (it-IT) Eddy (Italian (Italy)) (it-IT) Flo (Italian (Italy)) (it-IT) Grandma (Italian (Italy)) (it-IT) Grandpa (Italian (Italy)) (it-IT) Reed (Italian (Italy)) (it-IT) Rocko (Italian (Italy)) (it-IT) Sandy (Italian (Italy)) (it-IT) Shelley (Italian (Italy)) (it-IT) Alva (sv-SE) Amélie (fr-CA) Eddy (French (Canada)) (fr-CA) Flo (French (Canada)) (fr-CA) Grandma (French (Canada)) (fr-CA) Grandpa (French (Canada)) (fr-CA) Reed (French (Canada)) (fr-CA) Rocko (French (Canada)) (fr-CA) Sandy (French (Canada)) (fr-CA) Shelley (French (Canada)) (fr-CA) Amira (ms-MY) Anna (de-DE) Eddy (German (Germany)) (de-DE) Flo (German (Germany)) (de-DE) Grandma (German (Germany)) (de-DE) Grandpa (German (Germany)) (de-DE) Reed (German (Germany)) (de-DE) Rocko (German (Germany)) (de-DE) Sandy (German (Germany)) (de-DE) Shelley (German (Germany)) (de-DE) Carmit (he-IL) Damayanti (id-ID) Daniel (en-GB) Eddy (English (UK)) (en-GB) Flo (English (UK)) (en-GB) Grandma (English (UK)) (en-GB) Grandpa (English (UK)) (en-GB) Reed (English (UK)) (en-GB) Rocko (English (UK)) (en-GB) Sandy (English (UK)) (en-GB) Shelley (English (UK)) (en-GB) Daria (bg-BG) Eddy (Spanish (Spain)) (es-ES) Flo (Spanish (Spain)) (es-ES) Grandma (Spanish (Spain)) (es-ES) Grandpa (Spanish (Spain)) (es-ES) Mónica (es-ES) Reed (Spanish (Spain)) (es-ES) Rocko (Spanish (Spain)) (es-ES) Sandy (Spanish (Spain)) (es-ES) Shelley (Spanish (Spain)) (es-ES) Eddy (Spanish (Mexico)) (es-MX) Flo (Spanish (Mexico)) (es-MX) Grandma (Spanish (Mexico)) (es-MX) Grandpa (Spanish (Mexico)) (es-MX) Paulina (es-MX) Reed (Spanish (Mexico)) (es-MX) Rocko (Spanish (Mexico)) (es-MX) Sandy (Spanish (Mexico)) (es-MX) Shelley (Spanish (Mexico)) (es-MX) Eddy (Finnish (Finland)) (fi-FI) Flo (Finnish (Finland)) (fi-FI) Grandma (Finnish (Finland)) (fi-FI) Grandpa (Finnish (Finland)) (fi-FI) Reed (Finnish (Finland)) (fi-FI) Rocko (Finnish (Finland)) (fi-FI) Sandy (Finnish (Finland)) (fi-FI) Satu (fi-FI) Shelley (Finnish (Finland)) (fi-FI) Eddy (French (France)) (fr-FR) Flo (French (France)) (fr-FR) Grandma (French (France)) (fr-FR) Grandpa (French (France)) (fr-FR) Jacques (fr-FR) Rocko (French (France)) (fr-FR) Sandy (French (France)) (fr-FR) Shelley (French (France)) (fr-FR) Thomas (fr-FR) Eddy (Japanese (Japan)) (ja-JP) Flo (Japanese (Japan)) (ja-JP) Grandma (Japanese (Japan)) (ja-JP) Grandpa (Japanese (Japan)) (ja-JP) Kyoko (ja-JP) Reed (Japanese (Japan)) (ja-JP) Rocko (Japanese (Japan)) (ja-JP) Sandy (Japanese (Japan)) (ja-JP) Shelley (Japanese (Japan)) (ja-JP) Eddy (Korean (South Korea)) (ko-KR) Flo (Korean (South Korea)) (ko-KR) Grandma (Korean (South Korea)) (ko-KR) Grandpa (Korean (South Korea)) (ko-KR) Reed (Korean (South Korea)) (ko-KR) Rocko (Korean (South Korea)) (ko-KR) Sandy (Korean (South Korea)) (ko-KR) Shelley (Korean (South Korea)) (ko-KR) Yuna (ko-KR) Eddy (Portuguese (Brazil)) (pt-BR) Flo (Portuguese (Brazil)) (pt-BR) Grandma (Portuguese (Brazil)) (pt-BR) Grandpa (Portuguese (Brazil)) (pt-BR) Luciana (pt-BR) Reed (Portuguese (Brazil)) (pt-BR) Rocko (Portuguese (Brazil)) (pt-BR) Sandy (Portuguese (Brazil)) (pt-BR) Shelley (Portuguese (Brazil)) (pt-BR) Eddy (Chinese (China mainland)) (zh-CN) Flo (Chinese (China mainland)) (zh-CN) Grandma (Chinese (China mainland)) (zh-CN) Grandpa (Chinese (China mainland)) (zh-CN) Reed (Chinese (China mainland)) (zh-CN) Rocko (Chinese (China mainland)) (zh-CN) Sandy (Chinese (China mainland)) (zh-CN) Shelley (Chinese (China mainland)) (zh-CN) Tingting (zh-CN) Eddy (Chinese (Taiwan)) (zh-TW) Flo (Chinese (Taiwan)) (zh-TW) Grandma (Chinese (Taiwan)) (zh-TW) Grandpa (Chinese (Taiwan)) (zh-TW) Meijia (zh-TW) Reed (Chinese (Taiwan)) (zh-TW) Rocko (Chinese (Taiwan)) (zh-TW) Sandy (Chinese (Taiwan)) (zh-TW) Shelley (Chinese (Taiwan)) (zh-TW) Ellen (nl-BE) Ioana (ro-RO) Joana (pt-PT) Kanya (th-TH) Karen (en-AU) Lana (hr-HR) Laura (sk-SK) Lekha (hi-IN) Lesya (uk-UA) Linh (vi-VN) Majed (ar-001) Tünde (hu-HU) Melina (el-GR) Milena (ru-RU) Moira (en-IE) Montse (ca-ES) Nora (nb-NO) Rishi (en-IN) Sara (da-DK) Sinji (zh-HK) Tessa (en-ZA) Tina (sl-SI) Xander (nl-NL) Yelda (tr-TR) Zosia (pl-PL) Zuzana (cs-CZ) Select a screen reader mode. Navigation Tools Large Cursor Black White Focus Ring Focus Ring Page Structure Headings Landmarks Links Select a tab to view the page structure. No headings found. No landmarks found. No links found. Reading Tools Tooltip Small Medium Large Reading Guide Small Medium Large Reading Mask Small Medium Large Text Tools Text Font Sans-Serif Dyslexic Text Size Line Height Text Spacing Text Alignment Graphics Tools Color Saturation None Low High Color Contrast Invert Dark Light Hide Images Hide Images Created by Divi-Modules ... PITTSBURGH INTERNATIONAL AIRPORT ALLEGHENY COUNTY AIRPORT AIRPORT AUTHORITY PITTSBURGH INTERNATIONAL AIRPORT ALLEGHENY COUNTY AIRPORT AIRPORT AUTHORITY Flights Flight Status Nonstop Destinations Airlines Parking Parking Options Pre-Book Parking Accessible Parking Request a Receipt Security Current Wait Times Prohibited Items Real ID TSA Travel Tips Medication Accessibility Accessible, Adult and Family Restrooms Wheelchair Assistance Mother’s Nursing Lounge Sensory Room Airport Ambassador Escorts Sunflower Program Pet Relief Areas Grievance Procedure Terminal Info Interactive Airport Map International Travel Eat, Shop & More Arts & Culture Ground Transportation Car Rental Ride Sharing Public Transportation Vehicles for Hire Access ADA Paratransit Contact Us FAQs Flights Flight Status Nonstop Destinations Airlines Parking Parking Options Pre-Book Parking Accessible Parking Request a Receipt Security Current Wait Times Prohibited Items Real ID TSA Travel Tips Medication Accessibility Accessible, Adult and Family Restrooms Wheelchair Assistance Mother’s Nursing Lounge Sensory Room Airport Ambassador Escorts Sunflower Program Pet Relief Areas Grievance Procedure Terminal Info Interactive Airport Map International Travel Eat, Shop & More Arts & Culture Ground Transportation Car Rental Ride Sharing Public Transportation Vehicles for Hire Access ADA Paratransit Contact Us FAQs PIT AGC ACAA PIT AGC ACAA Flights Flight Status Nonstop Destinations Airlines Parking Parking Options Pre-Book Parking Accessible Parking Request a Receipt Security Current Wait Times Prohibited Items Real ID TSA Travel Tips Medication Accessibility Accessible, Adult and Family Restrooms Wheelchair Assistance Mother’s Nursing Lounge Sensory Room Airport Ambassador Escorts Sunflower Program Pet Relief Areas Grievance Procedure Terminal Info Interactive Airport Map International Travel Eat, Shop & More Arts & Culture Ground Transportation Car Rental Ride Sharing Public Transportation Vehicles for Hire Access ADA Paratransit Contact Us FAQs Flights Flight Status Nonstop Destinations Airlines Parking Parking Options Pre-Book Parking Accessible Parking Request a Receipt Security Current Wait Times Prohibited Items Real ID TSA Travel Tips Medication Accessibility Accessible, Adult and Family Restrooms Wheelchair Assistance Mother’s Nursing Lounge Sensory Room Airport Ambassador Escorts Sunflower Program Pet Relief Areas Grievance Procedure Terminal Info Interactive Airport Map International Travel Eat, Shop & More Arts & Culture Ground Transportation Car Rental Ride Sharing Public Transportation Vehicles for Hire Access ADA Paratransit Contact Us FAQs Eat, Shop & More POI Map Accessibility ATM Bar Breakfast Coffee Food Shop Open Now Open 24 hrs Show All All Locations Pre-Security Terminal Post-Security Terminal American Airlines Admirals Club OPEN NOW | Closes at 9:15 PM Post-Security Terminal / Mezzanine LEARN MORE Interfaith Reflection Room OPEN NOW | Open 24hrs Post-Security Terminal / Mezzanine LEARN MORE Hudson Booksellers OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Auntie Anne's OPEN NOW | Closes at 10:00 PM Post-Security Terminal / Concourse LEARN MORE Cinnabon OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE ATM - PNC Bank OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Hudson OPEN NOW | Closes at 8:30 PM Post-Security Terminal / Concourse LEARN MORE Sambazon Acai Bowls OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Hudson News OPEN NOW | Closes at 4:00 PM Post-Security Terminal / Concourse LEARN MORE Vino Volo OPEN NOW | Closes at 6:00 PM Post-Security Terminal / Concourse LEARN MORE Hudson Booksellers OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Sound & Mobile Accessories Vending Machine OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Bruegger's Bagels OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Burgh Sportz Bar OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE CNN Newsstand OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Burgh Sportz Bar OPEN NOW | Closes at 6:00 PM Post-Security Terminal / Concourse LEARN MORE Pet Relief Area OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Family Restroom OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Johnston & Murphy OPEN NOW | Closes at 5:00 PM Post-Security Terminal / Concourse LEARN MORE Sunglass Hut OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Lids OPEN NOW | Closes at 7:30 PM Post-Security Terminal / Concourse LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Starbucks OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Beercode OPEN NOW | Closes at 9:00 PM Post-Security Terminal / Concourse LEARN MORE Hudson OPEN NOW | Closes at 9:30 PM Post-Security Terminal / Concourse LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE InMotion Entertainment OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE ATM - PNC Bank OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Auntie Anne's OPEN NOW | Closes at 10:00 PM Post-Security Terminal / Concourse LEARN MORE ATM - PNC Bank OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Chick-fil-A OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Hudson Booksellers OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Martini OPEN NOW | Closes at 7:30 PM Post-Security Terminal / Concourse LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE SmarteCartes OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE SmarteCartes OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE SmarteCartes OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE ATM - PNC Bank OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE ATM - PNC Bank OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE ShopAll TravelWell Vending Machine OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE Security Checkpoint OPEN NOW | Closes at 10:30 PM Pre-Security Terminal / Transit LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE SmarteCartes OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE USPS Mailbox OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE ATM - PNC Bank OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Airport Ambassador Desk OPEN NOW | Closes at 7:00 PM Pre-Security Terminal / Baggage Claim LEARN MORE Visit Pittsburgh OPEN NOW | Closes at 9:00 PM Pre-Security Terminal / Baggage Claim LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE SmarteCartes OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Pet Relief Area OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Pet Relief Area OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Extended Parking Shuttle Stop OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Hotel Courtesy Shuttles OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE The Strip Market OPEN NOW | Closes at 12:00 PM Post-Security Terminal / Concourse LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE The Club Lounge OPEN NOW | Closes at 7:30 PM Post-Security Terminal / Concourse LEARN MORE Marathon Diner Temporarily closed for renovation OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Dunkin' Donuts OPEN NOW | Closes at 6:00 PM Pre-Security Terminal / Transit LEARN MORE Penn Brewery OPEN NOW | Closes at 7:30 PM Post-Security Terminal / Concourse LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Bicycle Assembly Station OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Charging Station OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Charging Station OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Self Service Check-In Kiosk OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE 7 Eleven OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE SmarteCartes OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE SmarteCartes OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE River Market by Hudson OPEN NOW | Closes at 11:00 PM Pre-Security Terminal / Transit LEARN MORE Charging Station OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE ATM - PNC Bank OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Joe & The Juice OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Hudson OPEN NOW | Closes at 10:00 PM Post-Security Terminal / Concourse LEARN MORE Vino Volo OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Dunkin' Donuts OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Gaby et Jules OPEN NOW | Closes at 6:00 PM Post-Security Terminal / Concourse LEARN MORE Local Craft Kitchen & Brewery OPEN NOW | Closes at 7:30 PM Post-Security Terminal / Concourse LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Wigle Whiskey OPEN NOW | Closes at 9:00 PM Post-Security Terminal / Concourse LEARN MORE Sarris Candies OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Primanti Bros. OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE FuelRod OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Kidsport Play Area OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE FuelRod OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE TGI Friday's Pub OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE ATM - PNC Bank OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Kylie Cosmetics Vending Machine OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Sound & Mobile Accessories Vending Machine OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Vendmobility Mobile Accessories Vending Machine OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE SmarteCartes OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE FuelRod OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE FuelRod OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Vendmobility Mobile Accessories Vending Machine OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE USPS Mailbox OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE ShopAll TravelWell Vending Machine OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE PIT Information Desk/Lost and Found OPEN NOW | Closes at 7:00 PM Pre-Security Terminal / Transit LEARN MORE USPS Mailbox OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Jabbrrbox OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE LEGO Vending Machine OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Hyatt Regency OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE PIT Information Desk OPEN NOW | Closes at 7:00 PM Post-Security Terminal / Concourse LEARN MORE Heinz History Center Statues OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE Meadowcroft Rock Shelter and Historic Village Display OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Miss Pittsburgh OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE T-Rex Cast OPEN NOW | Open 24hrs Post-Security Terminal / Trains LEARN MORE Prosegur wheelchair services OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Bellfarm Kitchen | Bar OPEN NOW | Closes at 11:45 PM Pre-Security Terminal / Ticketing LEARN MORE ACTS Airport Security OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE SmarteCartes OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE 7 Eleven with Sunoco Gas Station OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Farmer's Fridge OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Farmer's Fridge OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Farmer's Fridge OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Farmer's Fridge OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE EV Auto Charging Stations OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Bike Rack OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Montour Trail Airport Connector OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE FuelRod OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE EV Auto Charging Station OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE EV Auto Charging Station OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Presley's Place Sensory Sensitivities Room OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Accessible Parking (Short Term Garage) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Short Term Garage) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Short Term Garage) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Short Term Garage) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Extended Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Extended Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Extended Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Extended Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Extended Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Economy Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Long Term Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Long Term Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Long Term Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Long Term Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Long Term Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Long Term Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Accessible Parking (Long Term Lot) OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Nursing Room OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Accessible Restroom with Universal Changing Table OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE All Gender Restroom OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Family Restroom OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE InMotion OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Family Restroom OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C29 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C31 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C28 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C26 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C27 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE TDD Device for the Deaf OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C23 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C33 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C36 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE TDD Device for the Deaf OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C40 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C41 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C39 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE TDD Device for the Deaf OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C38 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C30 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C35 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Nursing Room OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Accessible restroom with universal changing table OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Sneak Peek of new terminal OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Convert cash to a prepaid card OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Convert cash to a prepaid card OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Historical Airport Presentation OPEN NOW | Open 24hrs Post-Security Terminal / Trains LEARN MORE Airport Courtesy Phone C10 OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Self Service Check-In Kiosk OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE Airport Courtesy Phone C18 OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Airport Courtesy Phone C17 OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Airport Courtesy Phone C15 OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Airport Courtesy Phone C13 OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Airport Courtesy Phone C12 OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE All Gender Restroom OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport courtesy phone C25 OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Airport Courtesy Phone C32 OPEN NOW | Open 24hrs Post-Security Terminal / Trains LEARN MORE Self Service Check-In Kiosk OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Self Service Check-In Kiosk OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Airport Courtesy Phone C8 OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Public Phone OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Public Phone OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Accessible Restroom with Universal Changing Table OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Champion City OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Duquesne Supply Co. OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Hudson OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE FuelRod OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Water Refill Station OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE All Gender Restroom OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Family Restroom OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE MAC Cosmetics OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE Accessible Restroom with Universal Changing Table OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Nursing Room OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE TDD Device for the Deaf OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Off Site Parking Shuttles OPEN NOW | Open 24hrs Pre-Security Terminal / Baggage Claim LEARN MORE Nursing Room OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Accessible Restroom with Universal Changing Table OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Family Restroom OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Prospect wheelchair service OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE All Gender Restroom OPEN NOW | Open 24hrs Post-Security Terminal / Concourse LEARN MORE Public Phone OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE Parking pay station OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE Parking pay station OPEN NOW | Open 24hrs Pre-Security Terminal / Transit LEARN MORE Accessibility Lane OPEN NOW | Closes at 10:30 PM Pre-Security Terminal / Transit LEARN MORE TDD Device for the Deaf OPEN NOW | Open 24hrs Pre-Security Terminal / Ticketing LEARN MORE Tumi OPEN NOW | Closes at 8:00 PM Post-Security Terminal / Concourse LEARN MORE No Results Found Try to limit the amount of filters applied to find more results Clear All Filters  (412) 472-3525  info@flypittsburgh.com  1000 Airport Blvd, Pittsburgh, PA 15231 Resources PIT TRANSFORMED VISIT PITTSBURGH CAREERS FAQs CONTACT US Pittsburgh International Airport FLIGHTS PARKING SECURITY ACCESSIBILITY Allegheny County Airport BUSINESS OPPORTUNITIES AERONAUTICAL INFO LANDING FEES Airport Authority CAREER OPPORTUNITIES BUSINESS OPPORTUNITIES AIRPORT BADGING REPORTS @ 2025 Allegheny County Airport Authority Privacy Policy  (412) 472-3525  info@flypittsburgh.com  1000 Airport Blvd, Pittsburgh, PA 15231 Resources PIT TRANSFORMED VISIT PITTSBURGH CAREERS FAQs CONTACT US Pittsburgh International Airport FLIGHTS PARKING SECURITY ACCESSIBILITY Allegheny County Airport BUSINESS OPPORTUNITIES AERONAUTICAL INFO LANDING FEES Airport Authority CAREER OPPORTUNITIES BUSINESS OPPORTUNITIES AIRPORT BADGING REPORTS @ 2025 Allegheny County Airport Authority Privacy Policy Chat with PIT Hi! I’m Skylar, PIT’s virtual assistant. I’m here to answer any questions you have about the airport. How can I help you today? Generated by AI - verify all information with the source links provided. This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply | Disclaimer | Powered by Cognistx Disclaimer × This chat feature is powered by artificial intelligence, and as such, both the chatbot and its outputs may have limitations or contain inaccuracies. The output generated by the chatbot is therefore provided “as-is” and on an “as and when available” basis. Any actions you take using the outputs are at your own risk. Cognistx and FlyPitt disclaims all liability for any losses or damages arising or resulting from your use of, or reliance on, the chatbot and/or its outputs. The chatbot does not have the authority to bind Cognistx to any course of action or activity, including but not limited to activation or reactivation of service, refunds, account balance changes, payment plans, or deposit amounts. By using the FlyPitt chatbot, you acknowledge and agree to these terms. Thanks for your feedback! Would you be willing to help us a little bit more? × Please select an relevant option below. (This is optional) This field is required 0 / 1000 Cancel No thanks Submit Thanks for your feedback! × 1 Hi! I’m Skylar, your guide to Pittsburgh International Airport. Ask me anything! × ```

### New Implementation Output for URL: https://flypittsburgh.com/pittsburgh-international-airport/terminal-info/eat-shop-more/

```American Airlines Admirals Club
OPEN NOW
| Closes at 9:15 PM
Post-Security Terminal / Mezzanine
Interfaith Reflection Room
OPEN NOW | Open 24hrs
Post-Security Terminal / Mezzanine
Hudson Booksellers
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Auntie Anne's
OPEN NOW
| Closes at 10:00 PM
Post-Security Terminal / Concourse
Cinnabon
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
ATM -  PNC Bank
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Hudson
OPEN NOW
| Closes at 8:30 PM
Post-Security Terminal / Concourse
Sambazon Acai Bowls
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Hudson News
OPEN NOW
| Closes at 4:00 PM
Post-Security Terminal / Concourse
Vino Volo
OPEN NOW
| Closes at 6:00 PM
Post-Security Terminal / Concourse
Hudson Booksellers
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Sound & Mobile Accessories Vending Machine
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Bruegger's Bagels
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Burgh Sportz Bar
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
CNN Newsstand
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Burgh Sportz Bar
OPEN NOW
| Closes at 6:00 PM
Post-Security Terminal / Concourse
Pet Relief Area
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Family Restroom
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Water Refill Station
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Johnston & Murphy
OPEN NOW
| Closes at 5:00 PM
Post-Security Terminal / Concourse
Sunglass Hut
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Lids
OPEN NOW
| Closes at 7:30 PM
Post-Security Terminal / Concourse
Water Refill Station
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Starbucks
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Beercode
OPEN NOW
| Closes at 9:00 PM
Post-Security Terminal / Concourse
Hudson
OPEN NOW
| Closes at 9:30 PM
Post-Security Terminal / Concourse
Water Refill Station
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
InMotion Entertainment
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
ATM - PNC Bank
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Auntie Anne's
OPEN NOW
| Closes at 10:00 PM
Post-Security Terminal / Concourse
ATM - PNC Bank
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Chick-fil-A
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Hudson Booksellers
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Martini
OPEN NOW
| Closes at 7:30 PM
Post-Security Terminal / Concourse
Water Refill Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Water Refill Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
SmarteCartes
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
SmarteCartes
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
SmarteCartes
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
ATM - PNC Bank
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
ATM - PNC Bank
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
ShopAll  TravelWell Vending Machine
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
Security Checkpoint
OPEN NOW
| Closes at 10:30 PM
Pre-Security Terminal / Transit
Water Refill Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
SmarteCartes
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
USPS Mailbox
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
ATM - PNC Bank
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Airport Ambassador Desk
OPEN NOW
| Closes at 7:00 PM
Pre-Security Terminal / Baggage Claim
Visit Pittsburgh
OPEN NOW
| Closes at 9:00 PM
Pre-Security Terminal / Baggage Claim
Water Refill Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
SmarteCartes
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Pet Relief Area
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Pet Relief Area
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Extended Parking Shuttle Stop
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Hotel Courtesy Shuttles
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
The Strip Market
OPEN NOW
| Closes at 12:00 PM
Post-Security Terminal / Concourse
Water Refill Station
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
The Club Lounge
OPEN NOW
| Closes at 7:30 PM
Post-Security Terminal / Concourse
Marathon Diner Temporarily closed for renovation
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Dunkin' Donuts
OPEN NOW
| Closes at 6:00 PM
Pre-Security Terminal / Transit
Penn Brewery
OPEN NOW
| Closes at 7:30 PM
Post-Security Terminal / Concourse
Water Refill Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Bicycle Assembly Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Charging Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Charging Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Self Service Check-In Kiosk
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
7 Eleven
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
SmarteCartes
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
SmarteCartes
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
River Market by Hudson
OPEN NOW
| Closes at 11:00 PM
Pre-Security Terminal / Transit
Charging Station
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
ATM - PNC Bank
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Joe & The Juice
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Hudson
OPEN NOW
| Closes at 10:00 PM
Post-Security Terminal / Concourse
Vino Volo
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Dunkin' Donuts
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Gaby et Jules
OPEN NOW
| Closes at 6:00 PM
Post-Security Terminal / Concourse
Local Craft Kitchen & Brewery
OPEN NOW
| Closes at 7:30 PM
Post-Security Terminal / Concourse
Water Refill Station
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Wigle Whiskey
OPEN NOW
| Closes at 9:00 PM
Post-Security Terminal / Concourse
Sarris Candies
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Primanti Bros.
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
FuelRod
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Kidsport Play Area
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
FuelRod
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
TGI Friday's Pub
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
ATM - PNC Bank
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Kylie Cosmetics Vending Machine
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Sound & Mobile Accessories Vending Machine
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Vendmobility Mobile Accessories Vending Machine
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
SmarteCartes
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
FuelRod
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
FuelRod
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Vendmobility Mobile Accessories Vending Machine
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
USPS Mailbox
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
ShopAll  TravelWell Vending Machine
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
PIT Information Desk/Lost and Found
OPEN NOW
| Closes at 7:00 PM
Pre-Security Terminal / Transit
USPS Mailbox
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Jabbrrbox
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
LEGO Vending Machine
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Hyatt Regency
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
PIT Information Desk
OPEN NOW
| Closes at 7:00 PM
Post-Security Terminal / Concourse
Heinz History Center Statues
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
Meadowcroft Rock Shelter and Historic Village Display
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Miss Pittsburgh
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
T-Rex Cast
OPEN NOW | Open 24hrs
Post-Security Terminal / Trains
Prosegur wheelchair services
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Bellfarm Kitchen | Bar
OPEN NOW
| Closes at 11:45 PM
Pre-Security Terminal / Ticketing
ACTS Airport Security
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
SmarteCartes
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
7 Eleven with Sunoco Gas Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Farmer's Fridge
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Farmer's Fridge
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Farmer's Fridge
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Farmer's Fridge
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
EV Auto Charging Stations
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Bike Rack
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Montour Trail Airport Connector
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
FuelRod
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
EV Auto Charging Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
EV Auto Charging Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Presley's Place Sensory Sensitivities Room
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Accessible Parking (Short Term Garage)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Short Term Garage)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Short Term Garage)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Short Term Garage)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Extended Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Extended Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Extended Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Extended Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Extended Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Economy Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Long Term Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Long Term Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Long Term Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Long Term Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Long Term Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Long Term Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Accessible Parking (Long Term Lot)
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Nursing Room
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Accessible Restroom with Universal Changing Table
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
All Gender Restroom
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Family Restroom
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
InMotion
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Family Restroom
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C29
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C31
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C28
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C26
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C27
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
TDD Device for the Deaf
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C23
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C33
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C36
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
TDD Device for the Deaf
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C40
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C41
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Water Refill Station
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C39
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
TDD Device for the Deaf
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C38
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C30
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C35
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Water Refill Station
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Nursing Room
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Accessible restroom with universal changing table
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Sneak Peek of new terminal
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Water Refill Station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Convert cash to a prepaid card
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Convert cash to a prepaid card
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Historical Airport Presentation
OPEN NOW | Open 24hrs
Post-Security Terminal / Trains
Airport Courtesy Phone C10
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Self Service Check-In Kiosk
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
Airport Courtesy Phone C18
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Airport Courtesy Phone C17
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Airport Courtesy Phone C15
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Airport Courtesy Phone C13
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Airport Courtesy Phone C12
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
All Gender Restroom
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport courtesy phone C25
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Airport Courtesy Phone C32
OPEN NOW | Open 24hrs
Post-Security Terminal / Trains
Self Service Check-In Kiosk
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Self Service Check-In Kiosk
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Airport Courtesy Phone C8
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Public Phone
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Public Phone
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Accessible Restroom with Universal Changing Table
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Champion City
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Duquesne Supply Co.
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Hudson
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
FuelRod
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Water Refill Station
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
All Gender Restroom
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Family Restroom
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
MAC Cosmetics
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse
Accessible Restroom with Universal Changing Table
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Nursing Room
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
TDD Device for the Deaf
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Off Site Parking Shuttles
OPEN NOW | Open 24hrs
Pre-Security Terminal / Baggage Claim
Nursing Room
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Accessible Restroom with Universal Changing Table
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Family Restroom
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Prospect wheelchair service
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
All Gender Restroom
OPEN NOW | Open 24hrs
Post-Security Terminal / Concourse
Public Phone
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
Parking pay station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
Parking pay station
OPEN NOW | Open 24hrs
Pre-Security Terminal / Transit
Accessibility Lane
OPEN NOW
| Closes at 10:30 PM
Pre-Security Terminal / Transit
TDD Device for the Deaf
OPEN NOW | Open 24hrs
Pre-Security Terminal / Ticketing
Tumi
OPEN NOW
| Closes at 8:00 PM
Post-Security Terminal / Concourse 
```


### Analysis
Between the two, the first contains much more extraneous and unhelpful content, which could muddle the vectorizing process for the LLM. Comparatively, the second one, which may contain some unnecessary phrases like "loading...", still is a cleaner and more precise interpretation of the webpage. The script used is quite elementary and could be improved upon to improve the sophistication of formatting and output format.
