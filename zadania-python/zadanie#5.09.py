vowels = "aeiuo"
def only_vowels(data) :
        lenght = len(str(data))
        for i in range(lenght):
            if data[i] in vowels:
                    yield data[i]
            elif data[i] not in vowels:
                    yield ""

for char in only_vowels("aagbeeupixieololul"):
            print(char, end="")

