# 6-4 Glossary 2

learning_glossary = {
    'list': 'a array / collection of any type of items or objects',
    'loops': 'iterations in code for any particular statement or set of statements',
    'variable': 'a value that can store a value / number / string etc',
    'if else': 'conditional filtering in code - if this then this, else this'
}

for topic, detail in learning_glossary.items():
    print(f"{topic} : {detail}")



# 6-5 Rivers

rivers = {
    'Chenab': 'Pakistan',
    'Ganga': 'India',
    'Amazon': 'United States',
    'Nile': 'Egypt',
}

print("\n")

for river, country in rivers.items():
    print(f"The {river} runs through {country}")

print("\n")

for river in rivers.keys():
    print(river)

print("\n")

for country in rivers.values():
    print(country)

print("\n")

# 6-6 Polling

favorite_laguages = {
    'zulfiqar': 'C++',
    'umair': 'Java',
    'zahid': 'python',
    'wahab': 'javascript',
    'anjum': 'typescript'
}

people_polled = {
    'zulfiqar': 'yes',
    'umair': 'no',
    'zahid': 'no',
    'wahab': 'yes',
    'anjum': 'yes',
}

for people, isPolled in people_polled.items():
    if isPolled == 'yes':
        print(f"Thanks {people} for polling.")
    elif isPolled == 'no':
        print(f"{people}, please poll!")