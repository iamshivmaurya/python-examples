import json
import random

# File where flashcards will be saved
FLASHCARDS_FILE = 'flashcards.json'

class FlashcardApp:
    def __init__(self):
        self.flashcards = []
        self.load_flashcards()

    def add_flashcard(self, question, answer):
        flashcard = {"question": question, "answer": answer}
        self.flashcards.append(flashcard)
        print("Flashcard added!")

    def quiz(self):
        if not self.flashcards:
            print("No flashcards available. Please add some first.")
            return
        
        correct_answers = 0
        random.shuffle(self.flashcards)  # Shuffle flashcards for random quiz order
        for card in self.flashcards:
            user_answer = input(f"Q: {card['question']} > ")
            if user_answer.lower() == card['answer'].lower():
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Incorrect. The answer is: {card['answer']}")
        
        print(f"\nQuiz finished! You got {correct_answers} out of {len(self.flashcards)} correct.")

    def save_flashcards(self):
        with open(FLASHCARDS_FILE, 'w') as file:
            json.dump(self.flashcards, file)
        print("Flashcards saved successfully!")

    def load_flashcards(self):
        try:
            with open(FLASHCARDS_FILE, 'r') as file:
                self.flashcards = json.load(file)
            print("Flashcards loaded successfully!")
        except FileNotFoundError:
            print("No flashcards file found. Starting fresh!")

def main():
    app = FlashcardApp()
    print("\n--- Flashcard App ---")
    while True:
        print("\nOptions:\n1. Add Flashcard\n2. Quiz\n3. Save Flashcards\n4. Load Flashcards\n5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            app.add_flashcard(question, answer)
        elif choice == "2":
            app.quiz()
        elif choice == "3":
            app.save_flashcards()
        elif choice == "4":
            app.load_flashcards()
        elif choice == "5":
            print("Exiting Flashcard App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

