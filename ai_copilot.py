def energy_copilot(query, total_usage):

    if "bill" in query:
        return f"Your estimated bill is RM {round(total_usage * 0.6, 2)}"

    if "save" in query:
        return "Reduce AC usage by 1 hour daily to save ~RM15/month"

    if "waste" in query:
        return "Main waste source is Air Conditioner usage during low occupancy"

    return "I can help you reduce energy cost, detect waste, or predict bills"
