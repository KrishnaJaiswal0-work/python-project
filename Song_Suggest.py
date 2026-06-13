while True:
    User_input = input("Enter Your Mood :").upper()
    mood = {
        "AGGRESSION" : ("Seedhe Maut ", "Sidhu Moose wala", "Divine", "Kr$na"),
        "PARTY" : ("Honey Singh", "Bohemia", "Gippy Grewal", "Dox"),
        "SAD" : ("Arijit Singh", "A.R.Rahman", "Nusrat Fateh Ali Khan", "Atif Aslam"),
        "OLD" : ("Kishore Kumar", "Lata Mangeshkar", "Mohammed Rafi", "Asha Bhosle"),
        }

    import random as rd

    artist = rd.choice(mood[User_input])
    print(f"Here's the artist :{artist}")

    song = {
        "Seedhe Maut" : ("Hola Amigo", "Khatta Flow"),
        "Sidhu Moose wala" : ("295", "So High"),
        "Divine" : ("Mirchi", "Baazigar"),
        "Kr$na" : ("I Guess", "Joota Japani"),
        "Honey Singh" : ("One Bottle Down", "Dope Shope"),
        "Bohemia" : ("Kali Denali", "Mi Amor"),
        "Gippy Grewal" : ("Car Nachdi", "Shoe"),
        "Dox" : ("Superstar", "Kadipatti"),
        "Arijit Singh" : ("Apna Bana Le", "Agar Tum Saath Ho"),
        "A.R.Rahman" : ("Nee Singam Dhan", "Kun Faya Kun"),
        "Nusrat Fateh Ali Khan" : ("Sochta Hoon", "Sanson Ki Mala"),
        "Atif Aslam" : ("Tera Hone Laga Hoon", "Tera Bin"),
        "Kishore Kumar" : ("O Mere Dil Ke Chayan", "Pal Pal Dil Ke Paas"),
        "Lata Mangeshkar" : ("Koi Ladki Hai", "Aankhein Khuli"),
        "Mohammed Rafi" : ("Baharon Phool Barsao", "Likhe Jo Khat Tujhe"),
        "Asha Bhosle" : ("Radha Kaise Na Jale", "Sharara"),
        }
    
    print(f"Here's the song of {artist} according to {User_input} : {rd.choice(song[artist])}")



# while True:
#     User_input = input("Enter Your Mood :").upper()
#     mood = {
#         "AGGRESSION" : ("Seedhe Maut ", "Sidhu Moose wala", "Divine", "Kr$na"),
#         "PARTY" : ("Honey Singh", "Bohemia", "Gippy Grewal", "Dox"),
#         "SAD" : ("Arijit Singh", "A.R.Rahman", "Nusrat Fateh Ali Khan", "Atif Aslam"),
#         "OLD" : ("Kishore Kumar", "Lata Mangeshkar", "Mohammed Rafi", "Asha Bhosle"),
#         }

#     import random as rd

#     choice =  rd.choice(mood[User_input])
#     print(f"Here's the artist : {choice}")
#     song = {
#         "Seedhe Maut" : ("Hola Amigo", "Khatta Flow"),
#         "Sidhu Moose wala" : ("295", "So High"),
#         "Divine" : ("Mirchi", "Baazigar"),
#         "Kr$na" : ("I Guess", "Joota Japani"),
#         "Honey Singh" : ("One Bottle Down", "Dope Shope"),
#         "Bohemia" : ("Kali Denali", "Mi Amor"),
#         "Gippy Grewal" : ("Car Nachdi", "Shoe"),
#         "Dox" : ("Superstar", "Kadipatti"),
#         "Arijit Singh" : ("Apna Bana Le", "Agar Tum Saath Ho"),
#         "A.R.Rahman" : ("Nee Singam Dhan", "Kun Faya Kun"),
#         "Nusrat Fateh Ali Khan" : ("Sochta Hoon", "Sanson Ki Mala"),
#         "Atif Aslam" : ("Tera Hone Laga Hoon", "Tera Bin"),
#         "Kishore Kumar" : ("O Mere Dil Ke Chayan", "Pal Pal Dil Ke Paas"),
#         "Lata Mangeshkar" : ("Koi Ladki Hai", "Aankhein Khuli"),
#         "Mohammed Rafi" : ("Baharon Phool Barsao", "Likhe Jo Khat Tujhe"),
#         "Asha Bhosle" : ("Radha Kaise Na Jale", "Sharara"),
#         }
    
#     print(f"Here's the song of {choice} accordiing to {User_input} : {rd.choice(song[choice])}")
    