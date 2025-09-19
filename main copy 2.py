# working with strings and numbers in PyScript
from pyscript import display, document

def gettingstrings(e):
    num1 = float(document.getElementById('name').value)
    num2 = float(document.getElementById('Age').value)
    num3 = float(document.getElementById('School').value)
    prod = num1 * num2 * num3

    display(f'The Computation of {num1} and {num2} is {prod:.2f}')



sample_multilinestrings = ''' 
👤Name: Zipporah Alvarado Ala
✅Age: 15
School 🏫: OB Montessori Center Greenhills
'''

print(sample_multilinestrings)
display(sample_multilinestrings)

sample_string = 'Zipporah Alvarado Ala\s Info'
sample_string2 = '15'
sample_string3 = 'OB Montessori Center Greenhills'
display(sample_string2)
display(sample_string3 * 5)