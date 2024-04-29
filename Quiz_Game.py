print('Welcome to my small quiz game!')
ans = input('Are you ready?: ')
score = 0
total_questions = 3

if ans.lower() == 'yes':
    ans = input('Who plays Tony Stark in Marvel Cinematic Universe? ')
    if ans == 'Robert Downey Jr':
        print('Good job!')
    else:
        print('Wrong, try again')

    ans = input('Q2=Who is the lead singer of Coldplay? ')
    if ans == 'Chris Martin':
        score += 1
        print('Well done!')
    else:
      print('Wrong, try again')

    ans = input('Q3=What is the capital of Spain? ')
    if ans == 'Madrid':
        score += 1
        print('Nice!')
    else:
        print('Wrong, try again')

marks = float((score/total_questions)*100)
print('Marks:', marks)
print('Thank you for participating in this small quiz!')
