import random

# Simulated NILM disaggregation model
def disaggregate_power(total_watts):

    devices = {
        "Air Conditioner": 0,
        "Fridge": 0,
        "TV": 0,
        "Fan": 0,
        "Unknown Load": 0
    }

    remaining = total_watts

    devices["Air Conditioner"] = min(1200, int(remaining * 0.6))
    remaining -= devices["Air Conditioner"]

    devices["Fridge"] = min(200, int(remaining * 0.4))
    remaining -= devices["Fridge"]

    devices["TV"] = random.randint(50, 120)
    devices["Fan"] = random.randint(30, 80)

    devices["Unknown Load"] = max(0, remaining)

    return devices


def detect_anomaly(device_power):
    if device_power["Air Conditioner"] > 1000 and device_power["Fan"] > 0:
        return "⚠️ High AC usage detected"
    if device_power["Fridge"] > 250:
        return "⚠️ Fridge abnormal consumption"
    return "✅ System normal"
