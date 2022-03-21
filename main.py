# ATT FIXA
# FRÅGA 1 LÄGGS IN 2 GÅNGER AV NÅN ALNEDNING

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
            y.write_alternatives()
            answer=input("Write your answer :")
            if y.control_answer(answer)==1:
                self.score+=1
                print(f"This is ur current score {self.score}")
            else:
                self.score-=1
                print(f"You answered wrong :( , ur current score is  {self.score}")

    def get_score(self):
        return self.score
    
    def get_name(self):
        return self.name

    def quiz_start(self): #BEh;ver g;ra klart
        print(f"")
        
        
def main():
        
    question1=Question("How many people live in sweden?","10 million",["10 million","2 million"] )
    question2=Question("How many sides does a cube have?","6",["6","4"])
    quiz=Quiz("Quiz",[] ,0)
    quiz.questions.append(question1)
    quiz.questions.append(question2)
    shuffle(quiz.questions)
    quiz.askquestions()
    print(f"This is your end score: {quiz.get_score()}")




main()


