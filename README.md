# BMI Calculator

<div align="center">
<h1 style="color:#00ffff; font-family:monospace;">BMI Calculator</h1>
<p style="font-family:monospace; font-size:16px; color:#9be7ff;">
Calculate your Body Mass Index (BMI) by entering your height, weight, and age 🚀
</p>
</div>

---

## Features

- **BMI Calculation**: Enter your height, weight, and age to calculate BMI  
- **Visual Gauge**: Interactive gauge shows your BMI category  
- **Themes**: Light and Dark options for the interface  
- **Clean Interface** with smooth interactions  

---

## Sample Code

<div style="background:#1e1e2f; padding:15px; border-radius:10px; color:#fff; font-family:monospace; line-height:1.5;">
<pre>
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QColor, QFont

class BMIGauge(QWidget):
    def __init__(self):
        super().__init__()
        self.current_bmi = 10
        self.target_bmi = 10
        self.animation_timer = QTimer()
        self.animation_timer.setInterval(15)
        self.animation_timer.timeout.connect(self.animate)
        self.bmi_min = 10
        self.bmi_max = 40
        self.setMinimumHeight(250)
        self.ranges = [
            (10, 16, QColor(0, 191, 255), "Severe Thinness"),
            (16, 17, QColor(30, 144, 255), "Moderate Thinness"),
            (17, 18.5, QColor(135, 206, 235), "Mild Thinness"),
            (18.5, 25, QColor(0, 255, 127), "Normal"),
            (25, 30, QColor(255, 165, 0), "Overweight"),
            (30, 35, QColor(255, 69, 0), "Obese Class I"),
            (35, 40, QColor(178, 34, 34), "Obese Class II+"),
        ]
</pre>
</div>

<p style="margin-top:10px; color:#333; font-family:monospace;">
Hello, you can calculate your body mass index (BMI) by entering your height, weight, and age.<br>
To use the code, you must be using Python version 3.10.11 because the PyQt5 library is not compatible with newer versions of Python.
</p>

---

## Download File

You can download the `main.py` file directly:

[![Download main.py](https://img.shields.io/badge/Download-main.py-00FFFF?style=for-the-badge&logo=python&logoColor=white)](https://raw.githubusercontent.com/SoBiMoqadam/BMI/main/main.py)

---

## Installation / Setup

Clone this repository and run the script using terminal:

```bash
git clone https://github.com/SoBiMoqadam/BMI.git
cd BMI
python main.py
