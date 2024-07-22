import random

# Define the quiz data
questions = [
    {"question": "What is the capital of France?", "choices": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": "C"},
    {"question": "Which planet is known as the Red Planet?", "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"], "answer": "B"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "choices": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"], "answer": "A"},
    {"question": "What is the smallest prime number?", "choices": ["A. 0", "B. 1", "C. 2", "D. 3"], "answer": "C"},
    {"question": "What is the chemical symbol for water?", "choices": ["A. O2", "B. CO2", "C. H2O", "D. HO"], "answer": "C"},
    {"question": "What is the largest ocean on Earth?", "choices": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"], "answer": "D"},
    {"question": "Who painted the Mona Lisa?", "choices": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"], "answer": "C"},
    {"question": "What is the hardest natural substance on Earth?", "choices": ["A. Gold", "B. Iron", "C. Diamond", "D. Platinum"], "answer": "C"},
    {"question": "What is the capital of Japan?", "choices": ["A. Beijing", "B. Seoul", "C. Tokyo", "D. Shanghai"], "answer": "C"},
    {"question": "Which element has the chemical symbol 'Na'?", "choices": ["A. Sodium", "B. Nitrogen", "C. Neon", "D. Nickel"], "answer": "A"},
    {"question": "What is the largest mammal in the world?", "choices": ["A. African Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"], "answer": "B"},
    {"question": "In which year did the Titanic sink?", "choices": ["A. 1912", "B. 1905", "C. 1920", "D. 1898"], "answer": "A"},
    {"question": "What is the main ingredient in guacamole?", "choices": ["A. Tomato", "B. Avocado", "C. Pepper", "D. Onion"], "answer": "B"},
    {"question": "Which planet is closest to the Sun?", "choices": ["A. Venus", "B. Earth", "C. Mercury", "D. Mars"], "answer": "C"},
    {"question": "Who wrote 'Romeo and Juliet'?", "choices": ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"], "answer": "A"},
    {"question": "What is the capital of Canada?", "choices": ["A. Toronto", "B. Vancouver", "C. Ottawa", "D. Montreal"], "answer": "C"},
    {"question": "What is the longest river in the world?", "choices": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"], "answer": "A"},
    {"question": "Which animal is known as the King of the Jungle?", "choices": ["A. Tiger", "B. Lion", "C. Elephant", "D. Bear"], "answer": "B"},
    {"question": "What gas do plants primarily use for photosynthesis?", "choices": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"], "answer": "C"},
    {"question": "Who is known as the Father of Computers?", "choices": ["A. Alan Turing", "B. Charles Babbage", "C. Ada Lovelace", "D. Bill Gates"], "answer": "B"},
    {"question": "Which country is known as the Land of the Rising Sun?", "choices": ["A. China", "B. Japan", "C. South Korea", "D. Thailand"], "answer": "B"},
    {"question": "What is the capital of Australia?", "choices": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"], "answer": "C"},
    {"question": "What is the chemical symbol for gold?", "choices": ["A. Au", "B. Ag", "C. Fe", "D. Pb"], "answer": "A"},
    {"question": "Who discovered penicillin?", "choices": ["A. Marie Curie", "B. Alexander Fleming", "C. Louis Pasteur", "D. Isaac Newton"], "answer": "B"},
    {"question": "What is the largest planet in our solar system?", "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"], "answer": "C"},
    {"question": "Which continent is the Sahara Desert located on?", "choices": ["A. Africa", "B. Asia", "C. Australia", "D. South America"], "answer": "A"},
    {"question": "What is the currency of the United Kingdom?", "choices": ["A. Dollar", "B. Euro", "C. Pound Sterling", "D. Yen"], "answer": "C"},
    {"question": "Which famous scientist developed the theory of relativity?", "choices": ["A. Albert Einstein", "B. Isaac Newton", "C. Galileo Galilei", "D. Nikola Tesla"], "answer": "A"},
    {"question": "What is the largest organ in the human body?", "choices": ["A. Heart", "B. Liver", "C. Skin", "D. Lungs"], "answer": "C"},
    {"question": "What is the name of the famous clock tower in London?", "choices": ["A. Big Ben", "B. The Shard", "C. Tower Bridge", "D. The Gherkin"], "answer": "A"},
    {"question": "Who was the first person to walk on the moon?", "choices": ["A. Neil Armstrong", "B. Buzz Aldrin", "C. Yuri Gagarin", "D. Michael Collins"], "answer": "A"},
    {"question": "Which Shakespeare play features the characters Oberon and Titania?", "choices": ["A. Hamlet", "B. Macbeth", "C. A Midsummer Night's Dream", "D. Romeo and Juliet"], "answer": "C"},
    {"question": "What is the largest species of shark?", "choices": ["A. Great White Shark", "B. Hammerhead Shark", "C. Whale Shark", "D. Tiger Shark"], "answer": "C"},
    {"question": "Which element is represented by the symbol 'Fe'?", "choices": ["A. Iron", "B. Fluorine", "C. Francium", "D. Phosphorus"], "answer": "A"},
    {"question": "What is the capital of Brazil?", "choices": ["A. São Paulo", "B. Rio de Janeiro", "C. Brasília", "D. Salvador"], "answer": "C"},
    {"question": "Which famous composer wrote 'The Four Seasons'?", "choices": ["A. Ludwig van Beethoven", "B. Johann Sebastian Bach", "C. Antonio Vivaldi", "D. Wolfgang Amadeus Mozart"], "answer": "C"},
    {"question": "What is the name of the process by which plants make their food?", "choices": ["A. Respiration", "B. Photosynthesis", "C. Digestion", "D. Fermentation"], "answer": "B"},
    {"question": "What is the capital of Italy?", "choices": ["A. Rome", "B. Florence", "C. Venice", "D. Milan"], "answer": "A"},
    {"question": "Which country is known as the Land of the Long White Cloud?", "choices": ["A. Australia", "B. New Zealand", "C. Canada", "D. Iceland"], "answer": "B"},
    {"question": "What is the most abundant gas in Earth's atmosphere?", "choices": ["A. Oxygen", "B. Hydrogen", "C. Nitrogen", "D. Carbon Dioxide"], "answer": "C"},
    {"question": "Who is the author of the Harry Potter series?", "choices": ["A. J.K. Rowling", "B. Suzanne Collins", "C. J.R.R. Tolkien", "D. George R.R. Martin"], "answer": "A"},
    {"question": "What is the capital of South Korea?", "choices": ["A. Seoul", "B. Busan", "C. Incheon", "D. Gwangju"], "answer": "A"},
    {"question": "What is the chemical symbol for silver?", "choices": ["A. Au", "B. Ag", "C. Pb", "D. Hg"], "answer": "B"},
    {"question": "Which famous scientist developed the laws of motion?", "choices": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Michael Faraday"], "answer": "A"},
    {"question": "Which country is known as the Emerald Isle?", "choices": ["A. Scotland", "B. Ireland", "C. Wales", "D. New Zealand"], "answer": "B"},
    {"question": "What is the smallest country in the world?", "choices": ["A. Monaco", "B. Vatican City", "C. Luxembourg", "D. San Marino"], "answer": "B"},
    {"question": "What is the hardest natural substance on Earth?", "choices": ["A. Diamond", "B. Gold", "C. Iron", "D. Platinum"], "answer": "A"},
    {"question": "Which planet is known for its rings?", "choices": ["A. Jupiter", "B. Uranus", "C. Neptune", "D. Saturn"], "answer": "D"},
    {"question": "What is the longest river in Africa?", "choices": ["A. Nile", "B. Congo", "C. Zambezi", "D. Niger"], "answer": "A"},
    {"question": "Who was the 16th President of the United States?", "choices": ["A. George Washington", "B. Abraham Lincoln", "C. Thomas Jefferson", "D. Andrew Johnson"], "answer": "B"},
    {"question": "What is the tallest mountain in the world?", "choices": ["A. K2", "B. Kangchenjunga", "C. Mount Everest", "D. Lhotse"], "answer": "C"},
    {"question": "What is the main language spoken in Brazil?", "choices": ["A. Spanish", "B. Portuguese", "C. English", "D. French"], "answer": "B"},
    {"question": "What is the currency of Japan?", "choices": ["A. Yen", "B. Won", "C. Ringgit", "D. Peso"], "answer": "A"},
    {"question": "Which ocean is the largest in terms of surface area?", "choices": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"], "answer": "D"},
    {"question": "What is the chemical symbol for potassium?", "choices": ["A. K", "B. P", "C. Po", "D. Pt"], "answer": "A"},
    {"question": "Who is known as the 'Father of the Nation' in India?", "choices": ["A. Jawaharlal Nehru", "B. Subhash Chandra Bose", "C. Mahatma Gandhi", "D. Bhagat Singh"], "answer": "C"},
    {"question": "What is the largest desert in the world?", "choices": ["A. Sahara", "B. Arabian", "C. Gobi", "D. Kalahari"], "answer": "A"},
    {"question": "Who is the Greek god of the sea?", "choices": ["A. Zeus", "B. Ares", "C. Poseidon", "D. Apollo"], "answer": "C"},
    {"question": "What is the name of the phobia of spiders?", "choices": ["A. Arachnophobia", "B. Claustrophobia", "C. Acrophobia", "D. Agoraphobia"], "answer": "A"},
    {"question": "What is the capital city of Germany?", "choices": ["A. Munich", "B. Frankfurt", "C. Berlin", "D. Hamburg"], "answer": "C"},
    {"question": "Which city is known as the 'City of Angels'?", "choices": ["A. New York", "B. Los Angeles", "C. Paris", "D. London"], "answer": "B"},
    {"question": "What is the primary ingredient in traditional sushi?", "choices": ["A. Chicken", "B. Fish", "C. Beef", "D. Pork"], "answer": "B"},
    {"question": "Who is the main character in the novel '1984'?", "choices": ["A. Winston Smith", "B. Julia", "C. O'Brien", "D. Big Brother"], "answer": "A"},
    {"question": "Which planet is known as the 'Giant Red Spot'?", "choices": ["A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"], "answer": "A"},
    {"question": "What is the capital of Egypt?", "choices": ["A. Cairo", "B. Alexandria", "C. Luxor", "D. Aswan"], "answer": "A"}
]

# Shuffle the questions to ensure random order each time
random.shuffle(questions)

def run_quiz():
    score = 0
    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1}: {question['question']}")
        for choice in question['choices']:
            print(choice)
        
        answer = input("Your answer (A, B, C, or D): ").upper()
        
        if answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The Correct Answer is {question['answer']}.")
    
    print(f"\nYour Final Score is {score} out of {len(questions)}")

def main():
    while True:
        run_quiz()
        retry = input("Do you want to retry the quiz? (yes/no): ").lower()
        if retry != 'yes':
            print("Thank you for playing!")
            break
        else:
            random.shuffle(questions)

if __name__ == "__main__":
    main()
