class AdaptabilityAssessment:
    def __init__(self):
        self.questions = {
            "Seasonal or climatic changes": [
                "No difficulty is faced, no health problem arises, can cope up changes easily",
                "Some uneasiness is there sometimes but it goes off at its own and no treatment is required",
                "Health problems like allergies are always there and require treatment"
            ],
            "Habitat change": [
                "No difficulty is faced, no health problem arises, can cope up changes easily",
                "Some uneasiness is there sometimes but it goes off at its own and no treatment is required",
                "Health problems like allergies are always there and require treatment"
            ],
            "Dietary changes": [
                "No problem arises if a new food item is eaten or on changes in dietary pattern",
                "Sometimes discomfort is there but require no treatment",
                "Changes in dietary pattern or intake of new or particular food item leads to allergy or discomfort in body, needs treatment"
            ],
            "Intake of ghrita": [
                "In every meal",
                "Sometimes, off and on",
                "Very less / Never"
            ],
            "Intake of oil": [
                "In every meal, food processing is done by cooking in oil",
                "Sometimes food is processed in oil and sometimes not",
                "Very less or No use of oil"
            ],
            "Intake of milk": [
                "Regular consumption of milk(around 500ml per day)",
                "Often takes milk (around 250ml per day)",
                "Very less intake or no intake of milk"
            ],
            "Intake of meat soups": [
                "Regular intake of meat soups.(almost daily)",
                "Moderate intake (3 to 4 times per week)",
                "Very less or no intake.(once weekly)"
            ],
            "Intake of 6 rasa": [
                "Intake of madhur, amla, lavana, katu, tikta, kshaya rasa food regularly",
                "Intake of any 3 to 5 rasa",
                "Intake of only one rasa, inadaptability to other 5 rasa"
            ],
        }
        self.scores = {
            "No difficulty is faced, no health problem arises, can cope up changes easily": 2,
            "Some uneasiness is there sometimes but it goes off at its own and no treatment is required": 1,
            "Health problems like allergies are always there and require treatment": 0,
            "No problem arises if a new food item is eaten or on changes in dietary pattern": 2,
            "Sometimes discomfort is there but require no treatment": 1,
            "Changes in dietary pattern or intake of new or particular food item leads to allergy or discomfort in body, needs treatment": 0,
            "In every meal": 2,
            "Sometimes, off and on": 1,
            "Very less / Never": 0,
            "In every meal, food processing is done by cooking in oil": 2,
            "Sometimes food is processed in oil and sometimes not": 1,
            "Very less or No use of oil": 0,
            "Regular consumption of milk(around 500ml per day)": 2,
            "Often takes milk (around 250ml per day)": 1,
            "Very less intake or no intake of milk": 0,
            "Regular intake of meat soups.(almost daily)": 2,
            "Moderate intake (3 to 4 times per week)": 1,
            "Very less or no intake.(once weekly)": 0,
            "Intake of madhur, amla, lavana, katu, tikta, kshaya rasa food regularly": 2,
            "Intake of any 3 to 5 rasa": 1,
            "Intake of only one rasa, inadaptability to other 5 rasa": 0,
        }

    def get_score(self, answer):
        return self.scores[answer]

    def adaptability_category(self, score):
        if 12 <= score <= 16:
            category = "Pravara Satmaya /High adaptability"
            treatment = "• All types of medicines can be given keeping into consideration the condition/disease."
        elif 6 <= score <= 11:
            category = "Madhyama Satmaya /Medium adaptability"
            treatment = "• Selection of type of medicine should be done as per satmya.\n" \
                        "• Some kind of rasayana medicines should be given along with normal required treatment as per condition/disease."
        elif 0 <= score <= 5:
            category = "Avara Satmaya /Low adaptability"
            treatment = "• Selection of type of medicine should be done as per satmya.\n" \
                        "• Rasayana medicines must be given along with normal required treatment as per condition/disease.\n" \
                        "• Some diet recommendations must be there regarding intake of advantageous food items (which are not in habit) following padanshika krama."
        else:
            category = "Score out of range"
            treatment = "Cannot determine treatment indication."

        return category, treatment

    def assessment(self):
        total_score = 0
        for question, options in self.questions.items():
            print(f"\n{question}:")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            answer = int(input("Please choose your option (enter the corresponding number): "))
            total_score += self.get_score(options[answer - 1])

        category, treatment = self.adaptability_category(total_score)
        print(f"\nYour score is: {total_score}")
        print(f"Your adaptability category is: {category}")
        print("Indication of line of treatment as per satmya:\n" + treatment)


# Running the assessment
assessment_tool = AdaptabilityAssessment()
assessment_tool.assessment()
