print("Welcome To The Ramayana Mad Libs Game!")

king_of_ayodhya = input("Enter the name of Ayodhya's King: ").lower()

if king_of_ayodhya == "dasharatha":
    eldest_son = input("Enter the name of "+ king_of_ayodhya.capitalize() + "'s Eldest son: " ).lower()

    if eldest_son == "rama":
        wife_of_ram = input("Enter the name of "+ eldest_son.capitalize() + "'s Wife: ").lower()

        if wife_of_ram == "sita":
            son_of_kaikeyi = input("Enter the name of Kaikeyi's Son: ").lower()

            if son_of_kaikeyi == "bharata":
                years_of_excile = str(input("Enter the number of years of "+eldest_son.capitalize()+"'s excile: "))

                if years_of_excile == "14":
                    print(king_of_ayodhya.capitalize()+" is the King of Ayodhya and has three wives and four sons, "+eldest_son.capitalize()+", Lakshmana, "+son_of_kaikeyi.capitalize()+", Shatrughana. "
                        +eldest_son.capitalize()+" is the ideal and perfect son, and grows up with his brothers. "
                        "When he comes of age, he marries "+wife_of_ram.capitalize()+", the princess of Janaka. " 
                        "However, "+son_of_kaikeyi.capitalize()+"'s mother is Kaikeyi, who resents "+eldest_son.capitalize()+" being the crown prince. "
                        "She calls up a debt that "+king_of_ayodhya.capitalize()+" owes her and asks for "+eldest_son.capitalize()+" to be exiled for "+years_of_excile+" years and her son "+son_of_kaikeyi.capitalize()+" be made crown prince instead.")
                else:
                    print("You're Wrong! You lost the Game.")
            else:
                print("You're Wrong! You lost the Game.")
        else:
            print("You're Wrong! You lost the Game.")

    else:
        print("You're Wrong! You lost the Game.")

else:
    print("You're Wrong! You lost the Game. Do you want to try again ? ")

print("Hope to see you play again. Bye...")
