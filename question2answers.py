from logic import *
# question 2
#1
# answer : ( read (maria, logic programming book)) => (by (peter lucas))
maria = Symbol("maria")
peter_lucas = Symbol("peter lucas")
read = Symbol(f" read ({maria}, logic programming book)")
by = Symbol(f"by ({peter_lucas})")
knowledge_q1 = And(Implication(read, by))
print(knowledge_q1.formula())
#---------------------------------------------------
#***************************************************
#---------------------------------------------------

# question 2
#2
# (is_girl(x)) => (like(x, shopping ))
is_girl = Symbol("is_girl(x)")
shopping = Symbol("shopping")
like = Symbol(f"like(x, {shopping} )")
knowledge_q2 = And(Implication(is_girl, like))
print(knowledge_q2.formula())

#---------------------------------------------------
#***************************************************
#---------------------------------------------------
# question 2
#3
# (?) ∧ (like(x, shopping ))
who = Symbol("?")
knowledge_q3  = And(who ,like)
print(knowledge_q3.formula())
#---------------------------------------------------
#***************************************************
#---------------------------------------------------
# question 2.4
# (city(x, big, crowdy)) => (kirke, x)
city = Symbol("city(x, big, crowdy)")
hates = Symbol("kirke, x")
knowledge_q4 = And(Implication(city, hates))
print(knowledge_q4.formula())