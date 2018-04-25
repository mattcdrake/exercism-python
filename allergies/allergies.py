class Allergies(object):
    def __init__(self, score):
        self.allergies = []
        if score >= 256:
            highest_power = 8

            while score > (2 ** (highest_power + 1)):
                highest_power += 1

            score -= (2 ** highest_power)
        
        if score >= 128:
            self.allergies.append("cats")
            score -= 128
        if score >= 64:
            self.allergies.append("pollen")
            score -= 64
        if score >= 32:
            self.allergies.append("chocolate")
            score -= 32
        if score >= 16:
            self.allergies.append("tomatoes")
            score -= 16
        if score >= 8:
            self.allergies.append("strawberries")
            score -= 8
        if score >= 4:
            self.allergies.append("shellfish")
            score -= 4
        if score >= 2:
            self.allergies.append("peanuts")
            score -= 2
        if score == 1:
            self.allergies.append("eggs")

    def is_allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        return self.allergies
