names = ['Rafal', 'Kaja', 'Monika', 'Filip', 'Przemek']

def pociesz(name):
    return 'Swietnie dzis wygladasz %s!' % (name)


###########################################333333
#tworzenie listy:

#klasycznie
def texts_for_marek(names):
    result = []
    for name in names:
        result.append( pociesz(name) )
    return result

#z list comprehension
def texts_for_marek(names):
    return [pociesz(name) for name in names]

###########################################333333
#tworzenie listy z warunkiem:

#klasycznie
def texts_for_marek(names):
    result = []
    for name in names:
        if name[-1] != 'a':
            result.append( pociesz(name) )
    return result

#z list comprehension
def texts_for_marek(names):
    return [pociesz(name) for name in names if name[-1] != 'a']


###########################################333333
#funkcje

#klasycznie
def key(x):
    return -x

#z lambda
key = lambda x : -x


###########################################333333
#sortowanie
lst = [1,2,3,4]
#key mowi jak sorted ma patrzec na sortowane elementy
print( sorted(lst, key= lambda x : -x) ) # lista malejaca

bmi = lambda wzrost, waga: waga/(wzrost**2)
names = [
    ['Rafal', 1.80, 83],
    ['Przemus', 1.94, 90],
    ['Filip', 1.70, 70],
    ['Marek', 1.50, 100]
]
#sortowanie po BMI
names = sorted(names, key=lambda name : -name[2]/(name[1]**2))
print(names)










