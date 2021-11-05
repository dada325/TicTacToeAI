def get_percentage(percentage, round_digits=0):
    if round_digits == 0:
        return str(int(round(percentage*100, 0))) + "%"
    return str(round(percentage*100, round_digits)) + "%"

