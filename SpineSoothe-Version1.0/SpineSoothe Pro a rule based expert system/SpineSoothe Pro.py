class BackPainExpertSystem:
    def __init__(self):
        self.exercise_rules = [
            {"location": "upper", "exercise": "Upper Back Stretch", "description": "follow this link :https://www.youtube.com/watch?v=IOukY_GzDFc&ab_channel=JeffreyPengMD"},
            {"location": "middle", "exercise": "Cat-Cow Stretch", "description": "follow this link :https://www.youtube.com/watch?v=GonNUMJOFlk&ab_channel=SpineCareDecompressionandChiropracticCenter"},
            {"location": "lower", "exercise": "Pelvic Tilt", "description": "follow this link :https://www.spine-health.com/video/4-easy-stretches-lower-back-pain-video"},
            {"location": "full", "exercise": "Child's Pose", "description": "follow this link :https://www.youtube.com/watch?v=BlLsuINN_oM"},
        ]

    def get_user_input(self):

        location = input("Where is the pain located? (upper/middle/lower/full): ").lower()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        return location

    def suggest_exercise(self, location):
        for rule in self.exercise_rules:
            if location == rule["location"]:
                return rule["exercise"], rule["description"]
        return "No specific exercise recommendation found."

    def run(self):
        print("|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |")
        print("|                      ->=== Welcome to SPINE_SOOTH_PRO ===<-                    |")
        print("|        Discover Personalized Back Pain Relief and Stress Release Exercises     |")
        print("|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |")
        location = self.get_user_input()
        exercise, description = self.suggest_exercise(location)

        print("\nRecommended Exercise:", exercise)
        print("Description:", description)


if __name__ == "__main__":
    back_pain_expert = BackPainExpertSystem()
    back_pain_expert.run()