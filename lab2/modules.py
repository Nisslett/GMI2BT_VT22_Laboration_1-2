from lab2.person import Person
from common import encapsulate, input_int_in_range
from common import input_not_empty

def add_person(person_list):
    person = {}
    for key in Person.keys():
        person[key] = input_not_empty(f"Skriv in {key.title()}: ")
    person_list.append(Person(person))

def search_person_list(personlist: list[Person]):
    keys: list[str] = Person.keys()
    # menu för attribut ,nr1 är alla atributer
    print(encapsulate("Söknings meny"))
    print("Välj den atribut av Personerna du vill söka på.")
    print("1. Alla attribut")
    for i in range(len(keys)):
        print(f"{i+2}. {keys[i]}")
    choice = input_int_in_range(
        "Välj ett av alternativen ovan: ", 1, len(keys)+1)
    if(choice == 1):
        chosen_search_attribute = keys
    else:
        chosen_search_attribute = [keys[choice-2]]
    # type serch term
    search_text: str = input("Skriv in den text du vill söka på: ")
    result_list: list = []
    for person in personlist:
        pers_dict=person.to_dictionary()
        for attribute in chosen_search_attribute:
            #try:
                if pers_dict[attribute].lower().find(search_text.lower()) != -1:
                    result_list.append(person)
                    break
            #except KeyError:
                # Raden nedan användes under utveckling för manuell debugging
                #print(f"key not found {attribute} i {person}")          
    return result_list

#edit
#edit->chose-> search


def choose_person(person_lista:list) -> Person:
    #anropas söknings funktionen/metoden
    result_list = search_person_list(person_lista)
    
    for i in range(len(result_list)):
        print(f"{i+1}. {result_list[i]}")
    print(f"{len(result_list)+1}. Ångra och avsluta funktion")
    choice=input_int_in_range("Välj person:",1,(len(result_list)+1))
    if choice == (len(result_list)+1):
        return None
    else:
        return result_list[choice -1]
    #får tillbaka en lista 
    #om listan är större än 10 kommer man tillbaka till sökfunktionen
    #om under 10 välja vilen du vill radera eller redigera
    #om 1 reda pseronen


def delete_person(person_lista:list):
    print(encapsulate("Radera en person"))
    print(encapsulate("Sök efter den person du vill radera"))
    person:Person = choose_person(person_lista)
    if person==None:
        print("Avbryter")
        return
    while True: 
        choice = input(f"Vill du radera {person}? Y/N").upper()
        if choice == "Y":
            person_lista.remove(person)
            break
        elif choice == "N":
            break
        else:
            print("Felaktig input, välj Y för Ja eller N för nej.")


def edit_person(person_lista:list):
    print(encapsulate("Redigera en person"))
    print(encapsulate("Sök efter den person du vill redigera"))
    #choose_person()
    person:Person=choose_person(person_lista)
    if person==None:
        print("Avbryter")
        return
    keys=Person.keys()
    pdict=person.to_dictionary()
    choice=0
    while True:
        for i in range(len(keys)):
            print(f"{i+1}. {keys[i]} :\"{pdict[keys[i]]}\"")
        print(f"{len(keys)+1}Spara och avsluta")
        print(f"{len(keys)+2}Avsluta utan att spara")
        choice=input_int_in_range("Välj vilken attribut av personen:",1,len(keys)+2)
        if choice>len(keys):
            break
        else:
            #redigera en attribut av personen
            pdict[keys[choice-1]]=input_not_empty(f"Redigera {keys[choice-1]}:\"{pdict[keys[i]]}\":")
    if choice==len(keys)+1:
        #spara person
        index=person_lista.index(person)
        newperson=Person(pdict)
        person_lista[index]=newperson
        print(f"Ersatte\n{person}\nmed\n{newperson}")
    else:
        print("Avslutar och spara INTE dina ändringar!")


def print_list(person_lista:list[Person]):
    keys=Person.keys()
    print(keys[0].ljust(15) + keys[1].ljust(15) + keys[2].ljust(30) + keys[3].ljust(16))
    for person in person_lista:
        print(person.username.ljust(15) + person.firstname.ljust(15) + person.surname.ljust(30) + person.email.ljust(16))
