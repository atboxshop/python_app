student = ('Sue',[89, 94, 85])
name, grades = student

print(f'{name}: {grades}')

print("Grade 1:", grades.__getitem__(0), "for Math")
print("Grade 2:", grades.__getitem__(1), "for Scienece")
print("Grade 3:", grades.__getitem__(2), "for Physic")

# if else statement inside a print function
print('A' if grades.__getitem__(0) == 89 and grades.__getitem__(1) == 95 else 'B')
