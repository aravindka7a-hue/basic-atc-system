# Basic ATC System

A simple command-line **Air Traffic Control (ATC)** simulator written in Python. A pilot chooses whether they want to **land** or **take off**, picks one of eight Indian airports, enters their fuel range and the current wind speed, and the program replies with a clearance message.

Each airport has its own module, so the rules and capacity for every airport can be changed independently.

---

## Supported airports

| Menu no. | Airport    | Module file    |
|:--------:|------------|----------------|
| 1        | Chennai    | `chennai.py`   |
| 2        | Hyderabad  | `hyderabad.py` |
| 3        | Delhi      | `delhi.py`     |
| 4        | Bengaluru  | `bengaluru.py` |
| 5        | Mumbai     | `mumbai.py`    |
| 6        | Kochi      | `Kochi.py`     |
| 7        | Kolkata    | `Kolkata.py`   |
| 8        | Ahmedabad  | `Ahmedabad.py` |

## Project structure

```
basic-atc-system/
├── main_code.py     # Entry point: menu, airport selection, calls the airport modules
├── Ahmedabad.py     # landing(f) and takeoff(f) for Ahmedabad
├── bengaluru.py     # ... one module per airport, same two functions
├── chennai.py
├── delhi.py
├── hyderabad.py
├── Kochi.py
├── Kolkata.py
└── mumbai.py
```

Every airport module exposes the same two functions:

- `landing(f)` – decides whether an aircraft can land
- `takeoff(f)` – decides whether an aircraft can take off

where `f` is the distance (in km) the aircraft can cover with its remaining fuel.

## Requirements

- Python 3.x
- No external libraries (only the standard library is used)

## How to run

1. Clone the repository and open the folder:
   ```bash
   git clone https://github.com/aravindka7a-hue/basic-atc-system.git
   cd basic-atc-system
   ```
2. Run the main program:
   ```bash
   python main_code.py
   ```
3. Follow the prompts.

## How it works

1. The program greets you and asks for a choice: **1** for landing or **2** for takeoff.
2. It lists the eight airports. Enter the number of the airport you are near (landing) or at (takeoff).
3. Enter the distance your aircraft can cover with its fuel, in km.
4. The chosen airport module asks for the current **wind speed in knots**.
5. The airport module checks the rules and returns a clearance message.

### Clearance rules

The same rules are used at every airport:

| Request  | Condition to be cleared                                                          | Message if cleared           | Message if not cleared     |
|----------|----------------------------------------------------------------------------------|------------------------------|----------------------------|
| Landing  | fuel range `f` < 250 km, wind speed between 30 and 40 knots (exclusive), and the airport counter `n` > 0 | `you can land safely`        | `sorry try anywhere else`  |
| Takeoff  | fuel range `f` > 500 km and wind speed between 30 and 40 knots (exclusive)       | `you can take off safely`    | `sorry try after sometime` |

Each airport module also has a counter `n` that appears to represent that airport's landing capacity:

| Airport   | Starting `n` |
|-----------|:------------:|
| Ahmedabad | 10 |
| Bengaluru | 40 |
| Chennai   | 12 |
| Delhi     | 78 |
| Hyderabad | 44 |
| Kochi     | 30 |
| Kolkata   | 24 |
| Mumbai    | 96 |

## Example session

```
welcome to ATC how may I help you
1: for landing
2: for takeoff
enter your choice1
are you close to any of these airports
1 : Chennai
2 : Hyderabad
3 : Delhi
4 : Bengaluru
5 : Mumbai
6 : Kochi
7 : Kolkata
8 : Ahmedabad
enter your choice3
enter the distance that can be covered by the fuel in the aircraft in KM200
enter wind speed in knots35
you can land safely
```

## Known issues

These are bugs in the current code that are worth fixing:

- **`chennai.py`** – `takeoff()` is missing the `if` keyword (line reads `f>500 and ws>30 and ws<40:`). This is a `SyntaxError`, so importing Chennai fails.
- **`bengaluru.py`** – in `landing()`, the success branch sets `a` but the function returns `b`, causing an `UnboundLocalError` when landing is allowed.
- **`Kochi.py` and `Kolkata.py`** – in `landing()`, the success branch prints the message and never sets the returned variable `a`, causing an `UnboundLocalError`. Also, `main_code.py` prints the return value, so the message should be returned instead of printed.
- **Landing counter never persists** – `n` is reset every time `landing()` is called, so `n = n - 1` has no lasting effect and capacity is never actually used up. Storing `n` at module level (and using `global n`) would fix this.
- **Wind rule is very narrow** – both landing and takeoff require wind between 30 and 40 knots, so any calm or lighter wind is rejected.
- **No input validation** – non-numeric input crashes the program with a `ValueError`.
- **File names are case-sensitive on Linux/macOS** – `main_code.py` imports `Ahmedabad`, `Kochi` and `Kolkata` with capital letters, so the file names must match exactly.
- The repeated `if/elif` chains in `main_code.py` could be replaced with a dictionary mapping menu numbers to modules.

## Possible improvements

- Fix the bugs listed above
- Track real runway/slot availability across multiple requests in one session
- Loop back to the main menu instead of exiting after one request
- Give each airport different rules (runway length, wind limits) instead of identical ones
- Add unit tests for `landing()` and `takeoff()`
