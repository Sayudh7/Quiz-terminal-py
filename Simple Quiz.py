questions=["How many elements are in periodic table?",
          "which animal lay the largest egg?",
          "what is most abundant gas in Earth's atmosphere?",
          "How many bones are there in human body?",
          "Which planet is hottest planet?"]

option=[["a.116","b.117","c.118","d.119"],
        ["a.whale","b.crocodile","c.elephant","d.ostrich"],
        ["a.nitrogen","b.oxygen","c.carbon dioxide","d.hydrogen"],
        ["a.206","b.207","c.208","d.209"],
        ["a.mercury","b.venus","c.earth","d.mars"]]

answer=["c","d","a","a","b"]

guesses=[]
score=0
no=0
for question in questions:
    print(question)
    for i in option[no]:
        print(i)
    o=input("enter the option for this question: ")
    guesses.append(o)
    if o==answer[no]:
        print("correct")
        score=score+1
    else:
        print("wrong")
    no=no+1
print(f"your score is {score}")
print("your answer is ")
for i in guesses:
    print(i,end=" ")
print("\ncorrect answer")
for i in answer:
    print(i,end=" ")
score=(score/len(option)*100)
print()
print(f"the score is {score}%")