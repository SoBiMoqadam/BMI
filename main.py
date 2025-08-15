import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QMessageBox, QComboBox, QCheckBox
)
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
from PyQt5.QtCore import Qt, QPointF, QTimer, QRectF
import math
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
    def setBMI(self, bmi):
        if bmi < self.bmi_min:
            bmi = self.bmi_min
        elif bmi > self.bmi_max:
            bmi = self.bmi_max
        self.target_bmi = bmi
        if not self.animation_timer.isActive():
            self.animation_timer.start()
    def animate(self):
        step = 0.2
        if abs(self.current_bmi - self.target_bmi) < step:
            self.current_bmi = self.target_bmi
            self.animation_timer.stop()
        elif self.current_bmi < self.target_bmi:
            self.current_bmi += step
        else:
            self.current_bmi -= step
        self.update()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        size = min(rect.width(), rect.height())
        margin = 20
        radius = max((size - 2 * margin) / 2, 1)  # حداقل 1
        center = QPointF(float(rect.width()) / 2, float(rect.height()) / 2 + 20)
        start_angle = 135 * 16
        span_angles_total = 270 * 16
        for start_bmi, end_bmi, color, _ in self.ranges:
            start_ratio = (start_bmi - self.bmi_min) / (self.bmi_max - self.bmi_min)
            end_ratio = (end_bmi - self.bmi_min) / (self.bmi_max - self.bmi_min)
            angle_start = start_angle + start_ratio * span_angles_total
            angle_span = (end_ratio - start_ratio) * span_angles_total
            pen = QPen(color, 15, Qt.SolidLine, Qt.FlatCap)
            painter.setPen(pen)
            painter.drawArc(
                QRectF(float(center.x()) - float(radius),
                       float(center.y()) - float(radius),
                       float(radius) * 2,
                       float(radius) * 2),
                int(angle_start),
                int(angle_span)
            )
        ratio = (self.current_bmi - self.bmi_min) / (self.bmi_max - self.bmi_min)
        angle_deg = 135 + 270 * ratio
        angle_rad = math.radians(angle_deg)
        needle_length = radius - 20
        needle_x = center.x() + needle_length * math.cos(angle_rad)
        needle_y = center.y() + needle_length * math.sin(angle_rad)
        pen = QPen(QColor(0, 200, 255), 5)
        painter.setPen(pen)
        painter.drawLine(center, QPointF(needle_x, needle_y))
        painter.setBrush(QColor(0, 200, 255))
        painter.drawEllipse(center, 10, 10)
class BMIApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.resize(450, 600)
        self.setupUI()
    def setupUI(self):
        font_title = QFont("Arial", 24, QFont.Bold)
        font_labels = QFont("Arial", 12)
        font_result = QFont("Arial", 20, QFont.Bold)
        self.title = QLabel("BMI CALCULATOR")
        self.title.setFont(font_title)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: #00ffff; letter-spacing: 3px;")
        self.weight_label = QLabel("Weight (kg):")
        self.weight_label.setFont(font_labels)
        self.weight_label.setStyleSheet("color: #00ffff;")
        self.weight_input = QLineEdit()
        self.weight_input.setFont(QFont("Arial", 18))
        self.weight_input.setStyleSheet(
            "background: transparent; border: 1px solid #00ffff; color: #00ffff; border-radius: 6px; padding: 6px;"
        )
        self.weight_input.setText("70")
        self.height_label = QLabel("Height (cm):")
        self.height_label.setFont(font_labels)
        self.height_label.setStyleSheet("color: #00ffff;")
        self.height_input = QLineEdit()
        self.height_input.setFont(QFont("Arial", 18))
        self.height_input.setStyleSheet(
            "background: transparent; border: 1px solid #00ffff; color: #00ffff; border-radius: 6px; padding: 6px;"
        )
        self.height_input.setText("175")
        self.age_label = QLabel("Age (years):")
        self.age_label.setFont(font_labels)
        self.age_label.setStyleSheet("color: #00ffff;")
        self.age_input = QLineEdit()
        self.age_input.setFont(QFont("Arial", 18))
        self.age_input.setStyleSheet(
            "background: transparent; border: 1px solid #00ffff; color: #00ffff; border-radius: 6px; padding: 6px;"
        )
        self.age_input.setText("30")
        self.gender_label = QLabel("Gender:")
        self.gender_label.setFont(font_labels)
        self.gender_label.setStyleSheet("color: #00ffff;")
        self.gender_combo = QComboBox()
        self.gender_combo.setFont(QFont("Arial", 14))
        self.gender_combo.setStyleSheet(
            "background: transparent; border: 1px solid #00ffff; color: #00ffff; border-radius: 6px; padding: 6px;"
        )
        self.gender_combo.addItems(["Male", "Female"])
        self.calc_button = QPushButton("CALCULATE BMI")
        self.calc_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.calc_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                border: 2px solid #00ffff;
                color: #00ffff;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #00ffff;
                color: #000;
            }
            """
        )
        self.calc_button.clicked.connect(self.calculate_bmi)
        self.bmi_label = QLabel("BMI: --")
        self.bmi_label.setFont(font_result)
        self.bmi_label.setStyleSheet("color: #00ffff;")
        self.category_label = QLabel("")
        self.category_label.setFont(font_result)
        self.category_label.setStyleSheet("color: #00ffff;")
        self.advice_label = QLabel("")
        self.advice_label.setFont(QFont("Arial", 14))
        self.advice_label.setStyleSheet("color: #aaffff;")
        self.advice_label.setWordWrap(True)
        self.ideal_weight_label = QLabel("")
        self.ideal_weight_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.ideal_weight_label.setStyleSheet("color: #00ff99;")
        self.dark_mode_checkbox = QCheckBox("Dark Mode")
        self.dark_mode_checkbox.setStyleSheet("color: #00ffff;")
        self.dark_mode_checkbox.setChecked(True)
        self.dark_mode_checkbox.stateChanged.connect(self.toggle_theme)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title)
        input_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        left_layout.addWidget(self.weight_label)
        left_layout.addWidget(self.weight_input)
        left_layout.addWidget(self.height_label)
        left_layout.addWidget(self.height_input)
        left_layout.addWidget(self.age_label)
        left_layout.addWidget(self.age_input)
        left_layout.addWidget(self.gender_label)
        left_layout.addWidget(self.gender_combo)
        left_layout.addWidget(self.calc_button)
        left_layout.addWidget(self.dark_mode_checkbox)
        right_layout.addStretch()
        input_layout.addLayout(left_layout)
        input_layout.addLayout(right_layout)
        main_layout.addLayout(input_layout)
        self.gauge = BMIGauge()
        main_layout.addWidget(self.gauge)
        main_layout.addWidget(self.bmi_label)
        main_layout.addWidget(self.category_label)
        main_layout.addWidget(self.advice_label)
        main_layout.addWidget(self.ideal_weight_label)
        main_layout.setAlignment(self.category_label, Qt.AlignLeft)
        main_layout.setAlignment(self.bmi_label, Qt.AlignLeft)
        main_layout.setAlignment(self.advice_label, Qt.AlignLeft)
        main_layout.setAlignment(self.ideal_weight_label, Qt.AlignLeft)
        self.setLayout(main_layout)
        self.apply_dark_theme()
    def toggle_theme(self, state):
        if state == Qt.Checked:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()
    def apply_dark_theme(self):
        self.setStyleSheet("background-color: #05051b;")
    def apply_light_theme(self):
        self.setStyleSheet("background-color: #f0f0f0; color: #000;")
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height_cm = float(self.height_input.text())
            age = int(self.age_input.text())
            gender = self.gender_combo.currentText()
            if weight <= 0 or height_cm <= 0 or age <= 0:
                raise ValueError
            height_m = height_cm / 100
            bmi = weight / (height_m ** 2)
            bmi_rounded = round(bmi, 1)
            self.bmi_label.setText(f"BMI: {bmi_rounded}")
            category = ""
            for start_bmi, end_bmi, _, cat in self.gauge.ranges:
                if start_bmi <= bmi < end_bmi:
                    category = cat
                    break
            else:
                if bmi >= self.gauge.bmi_max:
                    category = "Very Obese"
            self.category_label.setText(category)
            advice_dict = {
                "Severe Thinness": "You should consult a healthcare provider to improve your nutrition.",
                "Moderate Thinness": "Consider gaining weight with balanced diet and exercise.",
                "Mild Thinness": "Slightly underweight; monitor your diet and health.",
                "Normal": "Your weight is normal. Keep a healthy lifestyle!",
                "Overweight": "Try to exercise regularly and control your diet.",
                "Obese Class I": "Consider lifestyle changes and consult a professional.",
                "Obese Class II+": "Medical advice is recommended to manage weight.",
                "Very Obese": "Seek medical support for weight management."
            }
            advice = advice_dict.get(category, "")
            if age < 18:
                advice = "BMI interpretation may differ for children and teenagers."
            self.advice_label.setText(advice)
            ideal_weight = 22 * (height_m ** 2)
            self.ideal_weight_label.setText(f"Ideal weight: {ideal_weight:.1f} kg")
            self.gauge.setBMI(bmi_rounded)
        except Exception:
            QMessageBox.warning(
                self,
                "Input error",
                "Please enter valid positive numbers for weight, height, and age."
            )
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMIApp()
    window.show()
    sys.exit(app.exec_())