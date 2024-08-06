class Question:
    all = []
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        Question.all.append((self.prompt,self.answer))
    def __repr__(self):
        print(f'{self.prompt}','self.answer')

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def take_quiz(self):
        for question in self.questions:
            user_answer = input(question[0])
            if user_answer.lower() == question[1].lower():
                self.score += 1

    def show_results(self):
        print(f"\nYou got {self.score}/{len(self.questions)} correct.")

    def review_answers(self):
        print("\nReview your answers:")
        for question in self.questions:
            print(f"Question: {question[0].strip()} - Answer: {question[1]}")

# Example questions
question_prompts = [
    "What is the capital of France?\n(a) Berlin\n(b) Madrid\n(c) Paris\n(d) Lisbon\n\n",
    "What is 5 + 7?\n(a) 10\n(b) 11\n(c) 12\n(d) 13\n\n",
    "Which planet is known as the Red Planet?\n(a) Earth\n(b) Mars\n(c) Jupiter\n(d) Venus\n\n"
]

question1 = Question(question_prompts[0], "c")
question2 = Question(question_prompts[1], "c")
question3 = Question(question_prompts[2], "b")


# Create a quiz instance
quiz = Quiz()

# # # Add questions to the quiz
for question in Question.all:
    quiz.add_question(question)

# Take the quiz
quiz.take_quiz()

# Show results
quiz.show_results()

# Review answers
quiz.review_answers()