# Dice Roll Simulator

# Project Goal
This Python program simulates dice rolls with customizable die sizes and roll counts. It provides detailed statistics, saves roll history to CSV files, and generates visual histograms. The simulator demonstrates core programming concepts including classes, input validation, data persistence, and statistical analysis using Python's standard library with optional visualization.

# Dependencies
- Python 3.6+ (standard libraries only)
- Optional: matplotlib for histograms (`pip install matplotlib`)

# How to Run
1. Save the code as `dice_simulator.py`
2. Run from terminal:
python dice_simulator.py
```

# Sample Session
```
==================================================
             DICE ROLL SIMULATOR             
==================================================

Enter die type (e.g., d4, d6, d20) or number of sides: d20
Number of rolls: 100

========================================
RESULTS (d20):
========================================

Rolls: 5, 20, 13, 7, 18, ..., 2, 19, 1, 15, 8

STATISTICS:
• Minimum: 1
• Maximum: 20
• Average: 10.52
• Most common: 14
• Total rolls: 100

FREQUENCY:
1: 3 rolls (3.0%)
2: 7 rolls (7.0%)
3: 4 rolls (4.0%)
...
20: 6 rolls (6.0%)

Results saved to: d20_rolls_20231025_143022.csv

Matplotlib installed. Generating histogram...

Roll again? (y/n): n

Thanks for rolling! Goodbye!
```

Features
- 🎲 Custom die sizes (d4-d100+)
- 📊 Statistical analysis (min, max, average, mode)
- 📈 Frequency distribution reports
- 💾 Automatic CSV saving with timestamps
- 📉 Optional histogram visualization
- ✅ Comprehensive input validation

File Outputs
- CSV files: `d<size>_rolls_<timestamp>.csv`
- Histograms: `d<size>_histogram.png` (when matplotlib installed)

Implementation Details
- Die class: Encapsulates dice properties and rolling logic
- Input validation: Handles invalid die sizes and roll counts
- Data persistence: Stores results in CSV format
- Statistical analysis: Uses collections.Counter for frequency counting
- Modular design: Separates rolling logic, I/O, and visualization

The program demonstrates professional Python development practices while maintaining simplicity and usability for both casual users and developers.
