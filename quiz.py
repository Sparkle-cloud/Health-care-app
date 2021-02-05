
print('RIDDLES')
riddle = {
    '1)Where does today come before yesterday?': ['dictionary'],
    '2)what goes up never come down?': ['age'],
    "3)what has keys but can't open any doors" : ['piano'],
    '4)what can you catch but not throw?': ['cold'],
    '5)the more there is less you see': ['darkness'],
    "6)Give me food and I will live,give me water and I will die" : ['fire'],
    '7)The more you take away,the bigger it gets': ['hole'],
    "8)what has lots of eyes but cant't see": ['potato'],
    }
score = 0
for questions, answers in riddle.items():
    print(questions)
    for i in range(len(answers)-0):
       user_input = input().lower()
    if user_input == answers[0]:
        score = score + 1
        print("Correct! good Job")
    else:
        print("sorry that's incorrect,think harder next time")
        
print("your score is ",score,'/8')
if score == 8:
    print("awesome! you're a genius")
elif score < 5:
    print("Its okay,don't give up!")
