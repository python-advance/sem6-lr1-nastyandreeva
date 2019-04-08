import pandas as pd
import numpy as np
import re
data = pd.read_csv('titanic.csv', index_col='PassengerId')
data['Pclass'] = data['Pclass'].astype(object)

# 1. Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.

# Реализация без функции:
sex_counts = data['Sex'].value_counts()
print("Ответ№1:" , '{} {}'.format(sex_counts['male'], sex_counts['female']))

# Реализация с функцией:
sex_counts = data['Sex'].value_counts()

def sex_count(sex, data = None):
    setsex = data.value_counts()
    if sex == 'male':
        return setsex['male']
    else:
        return setsex['female']
    
male_numb = sex_count('male', data['Sex'] )
female_numb = sex_count('female', data['Sex'])
print("Ответ№1:" , male_numb, female_numb)


# 2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
embarked_counts = data['Embarked'].value_counts()
print("Ответ№2:" , '{} {} {}'.format(embarked_counts['C'], embarked_counts['S'],embarked_counts['Q']))

# 3. Посчитайте долю погибших на параходе (число и процент)?

# Реализация без функции:
surv_counts = data['Survived'].value_counts()
surv_percent = 100.0 * surv_counts[0] / surv_counts.sum()
print("Ответ№3:", "{:0.2f}".format(surv_percent), surv_counts[0])

# Реализация с функцией:
surv_counts = data['Survived'].value_counts()

def surv_count(survived, data = None):
    setsurv = data.value_counts()
    if survived == 0:
        return setsurv[0]
    else:
        return setsurv[1]
    
not_surv_numb = surv_count(0, data['Survived'])
surv_percent = 100.0 * not_surv_numb / surv_counts.sum()
print("Ответ№3:" ,not_surv_numb,"{:0.2f}".format(surv_percent))

# 4. Какие доли составляли пассажиры первого, второго, третьего класса?

# Реализация без функции:
pclass_counts = data['Pclass'].value_counts()
pclass_percent1 = 100.0 * pclass_counts[1] / pclass_counts.sum()
pclass_percent2 = 100.0 * pclass_counts[2] / pclass_counts.sum()
pclass_percent3 = 100.0 * pclass_counts[3] / pclass_counts.sum()
print("Ответ№4:", "{:0.2f}".format(pclass_percent1), "{:0.2f}".format(pclass_percent2), "{:0.2f}".format(pclass_percent3))

# Реализация с функцией:
def get_number_of_class(rec):
    
  data = pd.read_csv(rec)
  pclass_percent1 = 100.0 * pclass_counts[1] / pclass_counts.sum()
  pclass_percent2 = 100.0 * pclass_counts[2] / pclass_counts.sum()
  pclass_percent3 = 100.0 * pclass_counts[3] / pclass_counts.sum()
  return pclass_percent1,pclass_percent2,pclass_percent3

get_number_of_class('titanic.csv')

# 5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
def corr_Pirson(x, y):
    
    data = pd.read_csv('titanic.csv')
    res = data[x].corr(data[y])
    return res

answer = corr_Pirson('SibSp','Parch' )
print("Ответ№5:", "{:0.2f}".format(answer))

# 6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
# возрастом и параметром survival;
# полом человека и параметром survival;
# классом, в котором пассажир ехал, и параметром survival.

def corr_Pirson(x, y):
    
    data = pd.read_csv('titanic.csv')
    res = data[x].corr(data[y])
    return res

answer = corr_Pirson('Age','Survived' )
print("Ответ№6:", "{:0.2f}".format(answer))

#answer = corr_Pirson('Sex','Survived' )
#print("Ответ№6:", "{:0.2f}".format(answer))

answer1 = corr_Pirson('Pclass','Survived' )
print("Ответ№6:", "{:0.2f}".format(answer1))

# 7. Посчитайте средний возраст пассажиров и медиану.
def age(data = None):
    age_lst = data.value_counts().index.tolist()
    return np.average(age_lst)
age_int = price(data['Age'])
print("Ответ№7:","{:0.2f}".format(age_int))

# 8. Посчитайте среднюю цену за билет и медиану

def price(data = None):
    price_lst = data.value_counts().index.tolist()
    return np.average(price_lst)
price_int = price(data['Fare'])
print("Ответ№8:","{:0.2f}".format(price_int))
    
# 9. Какое самое популярное мужское имя на корабле?
def clean_name(name):
    # Первое слово до запятой - фамилия
    s = re.search('^[^,]+, (.*)', name)
    if s:
        name = s.group(1)

    # Если есть скобки - то имя пассажира в них
    s = re.search('\(([^)]+)\)', name)
    if s:
        name = s.group(1)

    # Удаляем обращения
    name = re.sub('(Master\. |Mr\. |Mrs\. )', '', name)

    # Берем первое оставшееся слово и удаляем кавычки
    name = name.split(' ')[0].replace('"', '')

    return name
names = data[data['Sex'] == 'male']['Name'].map(clean_name)
name_counts = names.value_counts()
print("Ответ№9:",name_counts.head(1).index.values[0])
# 10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
