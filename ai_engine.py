def detect_waste(device, watts, hours, motion):
    if device == "Air Conditioner" and not motion and hours > 2:
        return "⚠️ Waste detected: AC running in empty room"
    if watts > 1000 and hours > 4:
        return "⚠️ High energy usage detected"
    return "✅ Normal usage"


def estimate_cost(watts, hours):
    return round((watts * hours * 0.001) * 0.6, 2)


def estimate_co2(kwh):
    return round(kwh * 0.5, 2)
