# create a multiple choice question and options

questions = ('What is the capital of India?',
             'Who is known as the “Father of the Nation” in India?',
             'Which is the longest river in India?',
             'How many states are there in India(as of now)?',
             'Which Inidan state is known as "Land of Five Rivers" ?',
             'Who was the first Prime Minister of India?',
             "Which is the National Animal of India?",
             'Which is the highest Mountain peak in India?',
             
             'Which Inidan city is known as "Silicon Valley of India"?'
             )
options = (('A. Mumbai','B. West Bengal','C. New Delhi','D. Bangalore'),
           ('A. Jawaharlal Nehru','B. Mahatma Gandhi','C. Subhas Chandra Bose','D. Bhagat Singh'),
           ('A. Yamuna','B. Ganga','C. Brahmaputra','D. Godavari'),
           ('A. 25','B. 26','C. 28','D. 30'),
           ('A. Harayana','B. Punjab','C. Utter Pradesh','D. Rajasthan'),
           ('A. Jawaharlal Nehru','B. Mahatma Gandhi','C. Subhas Chandra Bose','D. Bhagat Singh'),
           ('A. Lion','B. Elephant','C. Tiger','D. Leopard'),
          ('A. Mount Everest','B. Kanchenjunga','C. Nanda Devi','D. K2'),
          ('A. Pune','B. Bengaluru','C. Hyderabad','D. Chennai'),
           )
answers = ('C','B','B','C','B','A','C','B','B')
question_no=0
guesses=[]
score=0
for question in questions:
  print('------------------------------------------')
  print(f'{question_no+1}. {question}')
  print('------------------------------------------')
  for option in options[question_no]:
    print(option)
  guess = input('Select one option (A,B,C,D): ').upper()
  guesses.append(guess)
  if guess ==answers[question_no]:
    score+=1
    print('Correct!!')
  else:
    score -=0.3
    print('InCorrect!')
    print('Correct Answer is:'+answers[question_no])
  question_no+=1

print('Your Score is: '+str(score))

