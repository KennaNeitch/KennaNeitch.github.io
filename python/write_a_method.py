def hyperbole():
    print(" all day every day.")

def class_rules(good_practices):
    print("In this class you should " + good_practices, end="", flush=True)
    hyperbole()


good_practices = ["ask questions", "talk to your neighbor", "avoid repetition", "LOVE Tony"]
for practice in good_practices:
    class_rules(practice)
