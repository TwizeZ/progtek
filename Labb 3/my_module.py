from text_encryption_function import encrypt    # Importerar funktionen encrypt från text_encryption_function.py
import json                                     # Importerar modulen json

# Uppgift 1

def copy_text_file(in_file, out_file):
    with open(in_file, 'r') as f1:          # Öppnar filen som ska kopieras
        with open(out_file, 'w') as f2:     # Öppnar filen som ska skrivas till
            for line in f1:                 # Loopar igenom varje rad i filen som ska kopieras
                f2.write(line)              # Skriver varje rad från första filen till den nya filen

# Uppgift 2

def encrypt_file(in_file, out_file):
    with open(in_file, 'r') as f1:          # Öppnar filen som ska krypteras
        with open(out_file, 'w') as f2:     # Öppnar filen som ska skrivas till
            for line in f1:                 # Loopar igenom varje rad i filen som ska krypteras
                f2.write(encrypt(line))     # Krypterar varje rad från första filen och skriver den till den nya filen

# Uppgift 3

def user_dialogue():
    status = True                                                               # Variabel som håller koll på om användaren har skrivit in ett korrekt filnamn
    while status:                                                               # Loopar så länge användaren inte har skrivit in ett korrekt filnamn
        in_file = input("Enter the name of the file you want to encrypt: ")     # Frågar efter filnamnet på filen som ska krypteras
        out_file = input("Enter the name of the new encrypted file: ")          # Frågar efter filnamnet på den nya krypterade filen
        
        try:
            encrypt_file(in_file, out_file)                                     # "Testar" att kryptera filen
            status = False                                                      # Om krypteringen lyckas så sätts status till False och loopen avslutas
        except FileNotFoundError:                                               # Om filen inte hittas i "encrypt_file" så fångas felet och användaren får försöka igen
            print("File not found. Please try again.")
    
    print("File encrypted successfully.")                                       # Om krypteringen lyckas så skrivs detta ut utanför loopen

# Uppgift 4
    
def get_int_input(prompt_string):
    status = True                                   # Variabel som håller koll på om användaren har skrivit in ett giltigt heltal
    while status:                                   # Loopar så länge användaren inte har skrivit in ett giltigt heltal
        try:
            input_num = int(input(prompt_string))   # Tar en input och försöker konvertera den till ett heltal
            status = False                          # Om det går så sätts status till False och loopen avslutas
        except ValueError:                          # Om konverteringen misslyckas (dvs. om input inte är ett heltal) så fångas felet och användaren får försöka igen
            print("Please enter a NUMBER!! >:(")
    return input_num                                # Om funktionen lyckas returneras det giltiga heltalet utanför loopen

# Uppgift 5

short_quiz_list_of_lists = [['Vad heter Norges huvudstad?', 'Oslo', 'Bergen', 'Köpenhamn'],
                            ['Vad står ABBA för?', 'Agneta Björn Benny Annefrid', 'Kalle och Lisa', 'Smarrig Sill']
                            ]

def run_quiz(quiz_list_of_lists):
    print("\n----------------------------------------\nHello and welcome, eller hejsan hopsan!\n----------------------------------------\n")
    
    correct_answers = 0                                             # Variabel som håller koll på antalet rätta svar
    for item in quiz_list_of_lists:                                 # Loopar igenom varje lista (fråga och svarsalternativ) i quiz_list_of_lists
        i = 1                                                       # Variabel som används för att skriva ut svarsalternativen
        print(item[0])                                              # Skriver ut frågan (första elementet i varje lista)
        for q_or_a in item[1:]:                                     # Loopar igenom varje svarsalternativ (de andra elementen i varje lista)
            print({i}, q_or_a)                                      # Skriver ut svarsalternativen
            i += 1
        
        status = True                                               # Variabel som håller koll på om användaren har svarat på frågan
        while status:                                               # Loopar så länge användaren inte har anget ett korrekt svar på frågan
            answer = get_int_input("Ange ditt svar (1, 2, 3): ")    # Anropar funktionen get_int_input och sparar användarens svar i variabeln answer
            if answer == 1:                                         # Om answer = 1 så skrivs "Rätt svar!" ut och correct_answers ökar med 1
                print("Rätt svar!")
                correct_answers += 1
                status = False                                      # Status sätts till False och loopen avslutas
            elif answer == 2 or answer == 3:                        # Om answer = 2 eller 3 så skrivs "Fel svar :(" ut och rätt svar skrivs ut
                print("Fel svar :(\nRätt svar är", item[1])
                status = False                                      # Status sätts till False och loopen avslutas
            else:
                print("Du måste ange 1, 2 eller 3.")                # Om användaren inte angett 1, 2 eller 3 så skrivs detta ut och loopen fortsätter tills ett korrekt svar angets
        print()
    print(f"Tack för ditt deltagande! Du fick {correct_answers} poäng av {len(quiz_list_of_lists)} möjliga.") # Skriver ut antalet rätta svar och antalet frågor i quizen

# Uppgift 6
    
def get_list_handle_exceptions():
    status = True                                                   # Variabel som håller koll på om användaren har skrivit in ett korrekt filnamn
    while status:                                                   # Loopar så länge användaren inte har skrivit in ett korrekt filnamn
        filename = input("Name of quiz-file: ")                     # Input för att ange quiz-filens namn
        try:
            short_quiz_list_of_lists = []                           # Skapar en tom lista som ska fyllas med frågor och svarsalternativ
            with open(filename, "r", encoding="utf8") as f:         # Öppnar filen som angivits
                for item in f:                                      # Loopar igenom varje rad i filen
                    question_list = item.strip().split(";")         # Delar upp varje rad i en lista med 4 parametrar (fråga och tre svarsalternativ)
                    if len(question_list) != 4:                     # Om en rad inte innehåller 4 parametrar så fångas felet och användaren får försöka igen
                        raise ValueError("Invalid file format. Make sure each line contains a question and three answer options separated by semicolons.")
                    short_quiz_list_of_lists.append(question_list)  # Om raden innehåller 4 parametrar så läggs den till i listan short_quiz_list_of_lists
            status = False                                          
        except FileNotFoundError:                                   # Om filen inte hittas så fångas felet och användaren får försöka igen
            print("File not found. Please try again.")
        except ValueError as err:                                   # Om en rad inte innehåller 4 parametrar så fångas felet här och användaren får försöka igen
            print(err)
    return short_quiz_list_of_lists                                 # Returnerar listan short_quiz_list_of_lists

# ----------------------------------------------------------

if __name__ == "__main__":
    # copy_text_file('namn.csv', 'my_copy.csv')
    # encrypt_file('namn.csv', 'secret_names.csv')
    # user_dialogue()
    # get_int_input("Enter a number: ")

    # run_quiz(short_quiz_list_of_lists)
    # print(get_list_handle_exceptions())

    # run_quiz(get_list_handle_exceptions())
    
    # NOTE Uppgift 8:
    ql = get_list_handle_exceptions()
    json_string = json.dumps(ql, indent=2)
    with open("quiz.json", "w", encoding="utf8") as fo:
        fo.write(json_string)