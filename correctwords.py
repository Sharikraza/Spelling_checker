from spellchecker import SpellChecker

# Step 1: Class banate hain
class SpellCheckerApp:
    def __init__(self):  # Correct initialization method
        self.spell = SpellChecker()

    # Step 2: Text correct karne ka method
    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')
            corrected_words.append(corrected_word)

        return ' '.join(corrected_words)

    # Step 3: App run karne ka method
    def run(self):
        print("\n--- Spell Checker App ---")

        while True:
            print("")
            text = input('Enter text (or type "exit" to quit): ')
            if text.lower() == 'exit':
                print("Exiting the program...")
                break

            corrected_text = self.correct_text(text)
            print(f'Corrected Text: {corrected_text}')

# Step 4: Program ko run karne wala block
if __name__ == "__main__":  # Correct line for entry point
    SpellCheckerApp().run()
