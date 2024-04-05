#განვიხილავთ დავალებას

full_name = "goal orientadze"

vowel_count = 0

for i in range(0,len(full_name)): #aeiou
    char = (full_name[i])
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        vowel_count += 1

print(vowel_count)

#დავალება დავპრინტოთ 0- დან 100 მდე ყველა რიცხვი ამ რიცხვებიდან ყველა 3 ის ჯერადს გვერძე მიეწეროს GOA თუ 5-ის ჯერადია GOA11 თუ 15-ის ჯერადია GOA15