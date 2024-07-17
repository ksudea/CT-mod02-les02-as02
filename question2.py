# Task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2
audio_system = "large double speakers" if attendees >= 150 else "regular speakers"
projector = "triple screen projector" if attendees >= 50 else "room projector"
print(audio_system)
print(projector)

# Task 3 

preference = input("Do you want vegetarian food? (yes/no) ")
caterer = "Veggie Delight Caterers" if preference == "yes" else "Gourmet Meals Caterers"
print(caterer)

