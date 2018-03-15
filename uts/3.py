score = int(raw_input('Enter the Score : '))
score = float(score)

if score >= 91:
    grade = 'A'
elif score >= 81:
    grade = 'B'
elif score >=71:
    grade = 'C'
elif score >=61:
    grade = 'D'
elif score >=51:
    grade = 'E'
else:
    grade = 'F'
print 'Your Grade : ' + grade 
