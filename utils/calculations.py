"""
Utility functions for derived clinical measurements.
"""

def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)


def calculate_pulse_pressure(ap_hi, ap_lo):
    return ap_hi - ap_lo


def calculate_map(ap_hi, ap_lo):
    return ap_lo + (ap_hi - ap_lo) / 3


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


def bp_category(ap_hi, ap_lo):
    if ap_hi < 120 and ap_lo < 80:
        return "Normal"
    elif ap_hi < 130 and ap_lo < 80:
        return "Elevated"
    elif ap_hi < 140 or ap_lo < 90:
        return "Hypertension Stage 1"
    return "Hypertension Stage 2"