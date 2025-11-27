import time
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "typing_scores.csv"

class TypingScoreManager:
    def __init__(self, data_file):
        self.data_file= data_file
        self.data =  self.load_typing_score()

    def load_typing_score(self):
        try:
            data = pd.read_csv(self.data_file, index_col=0)
            return data.to_dict(orient='index')
        except FileNotFoundError:
            return {}

    def save_typing_score(self):
        df= pd.DataFrame.from_dict(self.data, orient='index')
        df.to_csv(self.data_file)

    def add_user(self, name):
        if name not in self.data:
            self.data[name] = {"wpm": 0, "accuracy": 0, "score": 0}
            self.save_typing_score()
            print(f"User '{name}' added successfully!")
        else:
            print("User already exists.")

    def select_user(self):
        print("Select a user:")
        for index, user in enumerate(self.data.keys(), 1):
            print(f"{index}. {user}")
        choice = input("Enter the number of the user: ")
        index= int(choice)- 1
        selected_user = list(self.data.keys())[index]
        return selected_user

    def compare_scores(self):
        user1 = self.select_user()
        user2 = self.select_user()
        score1= self.data[user1]["score"]
        score2 = self.data[user2]["score"]
        print(f"\n{user1}'s score: {score1:.2f}")
        print(f"{user2}'s score: {score2:.2f}")
        if score1 >score2:
            print(f"{user1} has a higher score!")
        elif score1 < score2:
            print(f"{user2} has a higher score!")
        else:
            print("Both users have the same score!")

def typing_speed_test(manager, paragraph):
    print("TYPE THE FOLLOWING PARAGRAPH:  ")
    print(paragraph)
    input("PRESS  'ENTER'  WHEN YOU ARE READY TO START TYPING THE PARAGRAPH...")
    start_time=time.time()
    typed_text= input("Type the paragraph here: ")
    end_time = time.time()

    actual_time= end_time - start_time
    words_typed= len(typed_text.split())
    wpm= (words_typed/actual_time)*60
    accuracy= sum(1 for tw, rw in zip(typed_text.split(), paragraph.split()) if tw == rw) / len(paragraph.split()) * 100
    score= wpm*(accuracy/100)

    print("\nCalculating your typing speed and accuracy...")
    time.sleep(2)
    print(f"\nYour typing speed is approximately {wpm:.2f} words per minute.")
    print(f"Your accuracy is {accuracy:.2f}%.")
    print(f"Your score is {score:.2f}.")

    user = input("Enter your name to save your score: ")
    if user:
        manager.add_user(user)
        manager.data[user] ={"wpm": wpm, "accuracy": accuracy, "score": score}
        manager.save_typing_score()

def main():
    paragraph = """
    The quick brown fox jumps over the lazy dog. Jackdaws love my big sphinx of quartz. Vexed nymphs go for quick waltz job.
    """
    manager = TypingScoreManager(DATA_FILE)
    while True:
        print("MENU:\n")
        print("1. Take Typing Speed Test")
        print("2. Compare Scores")
        print("3. Visualize Scores")
        print("4. Exit\n")
        choice = input("Enter your choice: ")
        if choice == '1':
            typing_speed_test(manager, paragraph)
            input("Press Enter to continue...")
        elif choice== '2':
            manager.compare_scores()
            input("Press Enter to continue...")
        elif choice == '3':
            df = pd.DataFrame.from_dict(manager.data, orient='index')
            df.plot(kind='bar', y='score', rot=0, legend=False)
            plt.title('TYPING SCORES')
            plt.xlabel('USERS')
            plt.ylabel('SCORES')
            plt.show()
            input("Press Enter to continue...")
        elif choice == '4':
            print("Thank you for using Typing Speed Test. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()