Typing Speed Test (Python)
A simple and interactive Typing Speed Test application built in Python.
This program measures Words Per Minute (WPM), accuracy and generates a final score.
It also stores user performance, allows score comparison and visualizes results using bar charts.

#How It Works
The user types a given paragraph. The program calculates:
WPM = (words typed / time taken) × 60
Accuracy = % of correctly typed words
Score = WPM × (accuracy / 100)
Results are saved for future comparison and analysis.

#Features
Typing speed test with live WPM & accuracy calculation
User score saving (stored in typing_scores.csv)
Compare scores between two selected users
Score visualization using matplotlib
Automatic data loading & saving via pandas