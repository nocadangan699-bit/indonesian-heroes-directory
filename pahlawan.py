"""
Indonesia National Heroes Directory
A simple Python command-line application that displays a comprehensive list 
of Indonesian national heroes and provides detailed information upon selection.
"""

# Database of Indonesian heroes using a nested dictionary
indonesian_heroes = {
    "Ir. Soekarno": {
        "Origin": "Surabaya, East Java",
        "Role": "Proclamator and the first President of the Republic of Indonesia.",
        "Legacy": "Led the independence movement, formulated Pancasila (the state philosophy), and read the Proclamation of Independence on August 17, 1945."
    },
    "Drs. Mohammad Hatta": {
        "Origin": "Bukittinggi, West Sumatra",
        "Role": "Proclamator and the first Vice President of the Republic of Indonesia.",
        "Legacy": "Accompanied Soekarno during the Proclamation, fought for international recognition of RI's sovereignty, and is known as the Father of Indonesian Cooperatives."
    },
    "Jenderal Sudirman": {
        "Origin": "Purbalingga, Central Java",
        "Role": "The first Commander-in-Chief of the Indonesian National Armed Forces.",
        "Legacy": "Led the legendary guerrilla warfare to defend Indonesia's independence against Dutch Military Aggressions despite being severely ill."
    },
    "R.A. Kartini": {
        "Origin": "Jepara, Central Java",
        "Role": "Pioneer of women's emancipation and rights in Indonesia.",
        "Legacy": "Advocated for women's education and rights. Her published letters, 'Out of Darkness into Light', inspired the modern Indonesian women's movement."
    },
    "Pangeran Diponegoro": {
        "Origin": "Yogyakarta",
        "Role": "Leader of the Java War (1825–1830).",
        "Legacy": "Led a massive resistance against the Dutch East Indies colonial rule in Java, severely draining the colonial treasury."
    },
    "Cut Nyak Dhien": {
        "Origin": "Aceh",
        "Role": "Female guerrilla leader in the Aceh War.",
        "Legacy": "Continued the fierce resistance against Dutch forces after her husband (Teuku Umar) passed away, leading troops in the Aceh jungles."
    },
    "Ki Hajar Dewantara": {
        "Origin": "Yogyakarta",
        "Role": "Father of National Education and founder of Taman Siswa.",
        "Legacy": "Opposed discriminatory colonial education policies and coined the famous educational maxim: 'Ing Ngarsa Sung Tuladha, Ing Madya Mangun Karsa, Tut Wuri Handayani'."
    },
    "Bung Tomo (Sutomo)": {
        "Origin": "Surabaya, East Java",
        "Role": "Revolutionary leader during the Battle of Surabaya (November 10).",
        "Legacy": "Ignited the fighting spirit of Surabaya's youth via emotional radio broadcasts to fight back against Allied and NICA forces."
    },
    "Pattimura (Thomas Matulessy)": {
        "Origin": "Saparua, Maluku",
        "Role": "Leader of the Maluku rebellion against colonial rule.",
        "Legacy": "Led the people of Maluku in a major revolt against the Dutch VOC and successfully captured Fort Duurstede in 1817."
    },
    "I Gusti Ngurah Rai": {
        "Origin": "Badung, Bali",
        "Role": "Military commander of the Indonesian forces in Lesser Sunda.",
        "Legacy": "Led the famous 'Puputan Margarana' (a fight to the death) against the Dutch military forces in Bali."
    }
}

def display_menu():
    """Displays the interactive menu on the console."""
    print("\n=============================================")
    print("      INDONESIAN NATIONAL HEROES DIRECTORY     ")
    print("=============================================")
    # Automatically generate numbers for the list
    for index, name in enumerate(indonesian_heroes.keys(), 1):
        print(f"{index}. {name}")
    print("0. Exit Application")
    print("=============================================")

def main():
    """Main program execution loop."""
    hero_names = list(indonesian_heroes.keys())
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter a hero's number to view details (or 0 to exit): "))
            
            if choice == 0:
                print("\nThank you for using the app. Never forget history!")
                break
            elif 1 <= choice <= len(hero_names):
                selected_hero = hero_names[choice - 1]
                info = indonesian_heroes[selected_hero]
                
                # Display the structured hero profile
                print(f"\n>>> HERO PROFILE: {selected_hero.upper()} <<<")
                print(f"Place of Origin : {info['Origin']}")
                print(f"Historical Role : {info['Role']}")
                print(f"Major Legacy    : {info['Legacy']}")
                
                input("\nPress ENTER to return to the main menu...")
            else:
                print("\n[Error] Invalid number. Please select a number from the list.")
        except ValueError:
            print("\n[Error] Please enter a valid integer numeric value.")

if __name__ == "__main__":
    main()

