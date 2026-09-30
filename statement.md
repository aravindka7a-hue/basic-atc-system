# Basic ATC System: Project Statement

## 1. Problem Statement

Air traffic control decides whether an aircraft can safely land or take off, based on conditions such as fuel, weather and airport capacity. Learners and beginners rarely get a simple, hands-on way to see how these decisions are made, and real ATC systems are too complex to study or experiment with.

This project provides a small, easy-to-understand Python program that simulates basic ATC clearance decisions. A pilot enters a request (land or take off), selects an airport, and provides fuel range and wind speed. The system replies with a clear clearance message.

## 2. Scope of Project

**In scope**

- A command-line program that handles two request types: landing and takeoff
- Eight Indian airports: Chennai, Hyderabad, Delhi, Bengaluru, Mumbai, Kochi, Kolkata and Ahmedabad
- One module per airport, each with its own `landing()` and `takeoff()` decision functions
- Clearance decisions based on three inputs: fuel range (km), wind speed (knots), and a per-airport capacity counter
- Text-based clearance messages (safe to land or take off, or try elsewhere or later)

**Out of scope (in the current version)**

- Real-time flight, radar or weather data
- Multiple aircraft handled at the same time
- Runway scheduling, taxiing, gate management or air-to-air separation
- A graphical interface or network access
- Use in real aviation operations. This is an educational simulation only

## 3. Target Users

- **Students and beginners** learning Python (functions, modules, conditionals, user input) through a real-world example
- **Educators** who need a simple demonstration project for programming classes
- **Aviation enthusiasts** who want to explore how basic clearance rules work
- **Developers** who want a starting point to extend into a larger simulation

## 4. High-Level Features

- **Interactive menu:** choose between landing and takeoff, then pick an airport from a numbered list
- **Multi-airport support:** eight airports, each in its own module so rules can be changed independently
- **Rule-based clearance:** decisions use fuel range, wind speed and airport capacity
- **Clear responses:** plain-language messages such as "you can land safely" or "sorry try anywhere else"
- **Modular design:** adding a new airport means adding one module with the same two functions
- **No dependencies:** runs on any machine with Python 3 and only the standard library
