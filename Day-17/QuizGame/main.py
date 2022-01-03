from question_model import Question
from data import question_data
from random import Random
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:    
    question = Question(q["question"],q["correct_answer"])
    question_bank.append(question)
    
quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_questions():
    quizbrain.next_question()
    
print("You've completed the quiz")
print(f"Your final score was :  {quizbrain.score}/{quizbrain.question_number}")