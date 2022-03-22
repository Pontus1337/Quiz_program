from random import choice, shuffle


class Question:
    def __init__(self,question,truanswer,alternatives:list):
        self.question=question
        self.truanswer=truanswer
        self.alternatives=alternatives
        
    def control_answer(self,answer):
        if answer == self.truanswer :
            return 1
        else:
            print(f"Wrong answer, the right answer was {self.truanswer}")

    def write_alternatives(self):
        print(f"1 out of these answer are correct {self.alternatives}")

        
class Quiz:
    def __init__(self,name,questions:list,score:int) :
        self.name=name
        self.questions=questions
        self.score=0

    def askquestions(self):
        for y in self.questions:
            print(y.question)
            n=0
            for x in y.alternatives:
                n+=1
                print(f"{n}: {x}")
            answer=input("Write your answer :")
            if y.control_answer(answer)==1:
                self.score+=1
                print(f"This is ur current score {self.score}")
            else:
                self.score-=1
                print(f"You answered wrong :( , ur current score is  {self.score}")
            print()



    def get_score(self):
        return self.score
    
    def get_name(self):
        return self.name

    def quiz_start(self):
        print(f"This is the best quiz ever and is called {self.name}.\n")
        input("Press enter to start\n")
        
def load_questions():
    loaded=[]
    with open("questions.txt","r", encoding="utf8") as f:
        for line in f.readlines():
            quest=line.split("/")
            l=Question(quest[0],str(quest[1]),quest[2].split(","))
            loaded.append(l)
    return loaded

# In the text file "questions.txt" you need to write "Question"/"which place the right answer is for example 3"/ answer 1, answer2 2, answer 3,
# Divide each question with a diffrent line

        
def main():
    quiz=Quiz("Quiz",[] ,0)
    quiz.questions.extend(load_questions())
    shuffle(quiz.questions)
    quiz.quiz_start()
    quiz.askquestions()
    print(f"This is your end score: {quiz.get_score()}")




main()


