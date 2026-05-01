def calculate_score(total_kwh):

    score = 100 - (total_kwh * 10)

    if score < 0:
        score = 0

    return round(score, 2)


def score_label(score):

    if score > 80:
        return "Excellent ⚡"
    elif score > 60:
        return "Good 👍"
    elif score > 40:
        return "Average ⚠️"
    else:
        return "Poor ❌"
