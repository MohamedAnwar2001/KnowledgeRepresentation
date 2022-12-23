from logic import *
# question 1
# 1
# in English : Carrot's color is orange
carrots = Symbol(" carrots ")
orange = Symbol(" orange ")
knowledge_q1 = And(
    Implication(carrots, orange)
)
print(knowledge_q1.formula())  # print the output formula of knowledge base
#---------------------------------------------------
#***************************************************
#---------------------------------------------------


# question 1
# 2
# in English : " person likes carrots if person is vegetarian. "
person = Symbol("person")
vegetarian = Symbol("vegetarian(x)")
like = Symbol("like")
person_like_carrots = Symbol("like(x, carrots)")
knowledge_q2 = And(Implication(vegetarian, person_like_carrots))
print(knowledge_q2.formula())
#---------------------------------------------------
#***************************************************
#---------------------------------------------------

# question 1
#3
# in English : " Student pass if student study hard "
pass_test= Symbol("pass(x)")
study_hard = Symbol("study_hard(x)")
knowledge_q3 = Implication(study_hard,pass_test)
print(knowledge_q3.formula())
#---------------------------------------------------
#***************************************************
#---------------------------------------------------
# question 1
#4
# answer in English : " who will pass? "
Pass = Symbol("? pass(who)")
knowledge_q4 = And(Pass)
print(knowledge_q4.formula())
#---------------------------------------------------
#***************************************************
#---------------------------------------------------
# question 1
#5
#  Answer in English : " Which course professor teaches? "
teaches = Symbol("? teaches(course, which)")
knowledge_q5 = And(teaches)
print(knowledge_q5.formula())
#---------------------------------------------------
#***************************************************
#---------------------------------------------------
# question 1.6
# answer in English : " If X & Y are enemies then X hates Y and X fights Y. "
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates = Symbol(f"hates({x}, {y})")
fight = Symbol(f"fight({x}, {y})")
knowledge_q6 = And(Implication(enemies, And(hates, fight)))
print(knowledge_q6.formula())
