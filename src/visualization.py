import matplotlib.pyplot as plt

hour_counts = {
    "00": 47862, "01": 38531, "02": 32508, "03": 29995,
    "04": 26756, "05": 27587, "06": 31287, "07": 47386,
    "08": 65443, "09": 78695, "10": 88309, "11": 95342,
    "12": 105143, "13": 104535, "14": 101393, "15": 109465,
    "16": 99527, "17": 80834, "18": 66809, "19": 59315,
    "20": 59944, "21": 57985, "22": 60673, "23": 54570
}

hour_4xx_counts = {
    "00": 368, "01": 332, "02": 618, "03": 364,
    "04": 185, "05": 168, "06": 135, "07": 223,
    "08": 341, "09": 361, "10": 493, "11": 434,
    "12": 651, "13": 616, "14": 525, "15": 553,
    "16": 580, "17": 586, "18": 430, "19": 440,
    "20": 444, "21": 437, "22": 463, "23": 486
}

hours = list(hour_counts.keys())

error_rates = []

for hour in hours:
    rate = (hour_4xx_counts[hour] / hour_counts[hour]) * 100
    error_rates.append(rate)

plt.plot(hours, error_rates, marker="o")

plt.title("4xx Error Rate by Hour")
plt.xlabel("Hour")
plt.ylabel("4xx Error Rate (%)")

plt.tight_layout()
plt.savefig("reports/4xx_error_rate_by_hour.png")
plt.show()