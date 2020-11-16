print("б) Програма. Дана послідовність, що містить від 2 до 10 слів, в кожному з яких від 2"
      "до 10 латинських букв; між сусідніми словами - не менше одного пробілу, за останнім"
      " словом - крапка.\nВивести на екран всі слова, відмінні від останнього слова,"
      "попередньо залишивши в слові тільки перші входження кожної літери.")

words = (input().lower()).split()
# words = ["Вова", "Кака", "Саса", "Воваffffffffffffff."]

print(f"Ваша строка котру ви ввели {words}")
t = -1;
while t >= -len(words):
    if len(words[t]) >= 2 and len(words[t]) <= 10:
        if (words[t].isalpha()):
            end = words[-t]
            break
        else:
            end = words[-1][0:-1]
            break
    t -= 1

words.pop(-t)
words.append(end)
result = []

if (len(words) >= 2 and len(words) <= 10):

    for word in words:
        if len(word) >= 2 and len(word) <= 10:
            newWord = []
            liters = word.lower()
            liters = list(liters)
            for i in liters:
                if i not in newWord:
                    newWord.append(i)
                    newWord__str = "".join(newWord)
            if (word != end):
                result.append(newWord__str)

resultEnd = []
endList = list(end)
for i in endList:
    i = i.lower()
    if i not in resultEnd:
        resultEnd.append(i)
        resultEnd__str = "".join(resultEnd)
result.append(resultEnd__str)

print(f"Результат : {result}")
