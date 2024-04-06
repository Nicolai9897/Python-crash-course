
# 8-1 Messages
def display_message():
    """Displays a basic funtction message"""
    print("dette kapittelet handler om funksjoner")


display_message()

print("\n")


# 8-2 Favourite Book
def fav_book(book):
    """A basic deff function that also take an argument"""
    print(f"{book}, er en av mine favoritt bøker")


fav_book("Project hail mary")

print("\n")


# 8-3 T-shirt
def make_tshirt(size, text):
    """A function used to show how to use both keyword arguments,
    and positional argument in a funciton"""
    print(f"You have selected a {size} T-shirt with the text "
          f"\"{text}\" on the front")


make_tshirt("Large", "Hey moma!")
make_tshirt(text='Hey dadyo', size='Meium')

print("\n")


# 8-4 Large shirts
def make_tshirt(size='Large', text='I love python'):
    """A function used to show how to use both keyword arguments,
    and positional argument in a funciton"""
    print(f"You have selected a {size} T-shirt with the text "
          f"\"{text}\" on the front")


make_tshirt()
make_tshirt(size='medium')
make_tshirt('Small', "screw Java")

print("\n")


# 8-5 Cities
def describe_city(city, country='Norway'):
    """prints a short message about a country and its city"""
    print(f"{city.title()} is a city in {country.title()}")


describe_city('Trondheim')
describe_city('New York', 'USA')
describe_city(country='england', city='London')

print("\n")


# 8-6 City names
def city_country(city, country):
    """makes a list of citys and their countrys"""
    ccformat = f'"{city}, {country}"'
    return ccformat.title()


print(city_country('Oslo', 'Norway'))
print(city_country(country='sweden', city='stOckhOLm'))
print(city_country('kopenhagen', 'denmark'))

print("\n")


# 8-7 Album
def make_album(artist, album_name, songs=None):
    """function to create a discography,
    with the ability to show how many songs are in an album"""
    album = {'artist': artist, 'album': album_name}
    if songs:
        album['songs'] = songs
    return album


album = make_album('Eminem', 'Recovery', 22)
print(album)

album = make_album('Taylor swift', '1989')
print(album)

album = make_album('Kaptein Sabeltan', 'Grusomme gabriels skatt', 16)
print(album)

print("\n")
print("\n")


# 8-8 User Album
def make_album(artist, album_name, songs=None):
    """function to create a discography,
    with the ability to show how many songs are in an album"""
    album = {'artist': artist, 'album': album_name}
    if songs:
        album['songs'] = songs
    return album

print("\n")
print("\n")



#while True:
#    print("when you want to exit the application, press q")
#    artist = input('Enter the artists name: ')
#    if artist == 'q':
#        break
#
#    album = input("Enter the album name: ")
#    if album == "q":
#        break
#
#   print(make_album(artist, album))


#8-9 Messages
print("\n")
print("\n")

messages = ['Hey babe', 'how you doing', 'wanna fuck?', 'I\'m ready']

def show_messages():
    """Function to print each string in a list"""

    for message in messages:
        print(message)

show_messages()

print("\n")
print("\n")


# 8-9 sending Messages
messages = ['Hey babe', 'how you doing', 'wanna fuck?', 'I\'m ready']
sent_messages = []


def show_messages():
    """Function to print each string in a list"""

    while messages:
        msg = messages.pop()
        print(msg)
        sent_messages.append(msg)


def show_sent_messagea():
    """function to show string that have been sent"""

    for message in sent_messages:
        print(message)

show_messages()
show_sent_messagea()
print("\n")
print("\n")


# 8-10 archived Messages

messages = ['Hey babe', 'how you doing', 'wanna fuck?', 'I\'m ready']
sent_messages = []





def send_messages():
    """Function to print each string in a list"""

    while messages[:]:
        msg = messages.pop()
        print(msg)
        sent_messages.append(msg)


def show_original_messages():
    """function to show string that have been sent"""

    for message in messages:
        print(message)

send_messages()
print("original messages")
show_sent_messagea()
print("\n")
print("\n")


#8-12 Sandwiches
"""function to print list of items the customers want on a sandwich"""

def sandwiches(*items):
    print("The sandwich will contain:")
    for item in items:
        print(f" -{item}")
    print("\n")

sandwiches('tomatoe',' cheese', 'lettuce')
sandwiches('bacon', 'lettuce', 'tomatoe')
sandwiches('beef', ' bacon', ' cheese', ' bbq sauce', ' lettuce')
print("\n")
print("\n")


#8-13 user profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('nicolai', 'olsen',
                             location='gjøvik',
                             age='25',
                             study='computer engineer')
print(user_profile)
print("\n")
print("\n")


#8-14 cars
def build_car(manufacturer, model, **kwargs):
    """function for building a dictionary with car information"""
    kwargs['manufacturer'] = manufacturer
    kwargs['car model'] = model
    return kwargs

first_car = build_car('toyota', 'prius',
                      color='gray',
                      gear='automatic',
                      electric=False)

print(first_car)
print("\n")
print("\n")


#8-15/16 printing models
#import printing_functions as pf
#from printing_functions import print_models
#from printing_functions import show_completed_models as scm
from printing_functions import*

unprinted_list =['telefon', 'bokstøtte', 'figur']
completed_models= []

#pf.print_models(unprinted_list, completed_models)
#pf.show_completed_models(completed_models)
#print_models(unprinted_list, completed_models)
#scm(completed_models)
print_models(unprinted_list, completed_models)
show_completed_models(completed_models)


