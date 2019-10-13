class LetterGrade:

    letter_to_points_mapper = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "F": 0.0
    }

    def __init__(self, letter):
        self.letter = letter
    
    def to_points(self):
        return self.letter_to_points_mapper.get(self.letter, "ERROR: Invalid letter")