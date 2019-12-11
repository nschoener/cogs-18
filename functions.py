month = input('\nWhat is your month of birth? e.g. November\n\n').lower()
day = int(input('\nWhat is your date of birth? e.g. 14\n\n'))
    
def determine_zodiac(month, day):
    
    if month == 'december':
        sign = 'sagittarius' if (day < 23) else 'capricorn'
    elif month == 'january':
        sign = 'capricorn' if (day < 21) else 'aquarius'
    elif month == 'february':
        sign = 'aquarius' if (day < 20) else 'pisces'
    elif month == 'march':
        sign = 'pisces' if (day < 21) else 'aries'
    elif month == 'april':
        sign = 'aries' if (day < 21) else 'taurus'
    elif month == 'may':
        sign = 'taurus' if (day < 22) else 'gemini'
    elif month == 'june':
        sign = 'gemini' if (day < 22) else 'cancer'
    elif month == 'july':
        sign = 'cancer' if (day < 23) else 'leo'
    elif month == 'august':
        sign = 'leo' if (day < 22) else 'virgo'
    elif month == 'september':
        sign = 'virgo' if (day < 24) else 'libra'
    elif month == 'october':
        sign = 'libra' if (day < 24) else 'scorpio'
    elif month == 'november':
        sign = 'scorpio' if (day < 23) else 'sagittarius'
    else:
        print('Invalid date. Please try again.')
    return sign

sign = determine_zodiac(month, day)
print( '\nYour zodiac sign is ' + sign + '.')


def horoscope_traits(sign = 'default'):
    if sign == 'aries':
        traits = ' eager and competitive'
    elif sign == 'taurus':
        traits = ' strong and dependable'
    elif sign == 'gemini':
        traits = ' versatile and expressive'
    elif sign == 'cancer':
        traits = ' intuitive and sentimental'
    elif sign == 'leo':
        traits = ' self-assured and outgoing'
    elif sign == 'virgo':
        traits = ' practical and loyal'
    elif sign == 'libra':
        traits = ' social and diplomatic'
    elif sign == 'scorpio':
        traits = ' resourceful and brave'
    elif sign == 'sagittarius':
        traits = ' optimistic and generous'
    elif sign == 'capricorn':
        traits = ' indepndent and disciplined'
    elif sign == 'aquarius':
        traits = ' imaginative and uncompromising'
    elif sign == 'pisces':
        traits = ' affectionate and artistic'
    else: 
        print('Please determine sign first.')
    return traits
print( '\n You are' + horoscope_traits(sign) + '.')



#horoscope data for this function is taken from http://horoscope-api.herokuapp.com/horoscope/today/
def daily_horoscope(sign = 'default'):
    import requests
    base_url = 'http://horoscope-api.herokuapp.com/horoscope/today/'
    fetch_url = base_url + sign[0].upper() + sign[1:]
    horoscope = requests.get(fetch_url)
    result = horoscope.json()
    return result['horoscope']
print(daily_horoscope(sign))



potential_match = input('\nWhom would you like to check your compatibility with? e.g. Jessica\n\n')
potential_match_sign = input('\nWhat is their sign? e.g. Sagittarius\n\n').lower()
my_score = random.randrange(0, 100, 1)
def compatibility(sign, potential_match, potential_match_sign, my_score):
    
    dict_of_signs = {'aries': 58, 'aquarius': 11, 'cancer': 8, 'capricorn': 10, 'gemini': 82, 'leo': 99, 'libra': 79, 'pisces': 57 , 'sagittarius': 38, 'scorpio': 34, 'taurus': 8, 'virgo': 37}
    if (my_score - 20) < dict_of_signs[potential_match_sign] < (my_score + 20):
        conclusion = '\n\nYou and ' + potential_match + ' are a match!'
    else: 
        conclusion = '\n\nYou and ' + potential_match + ' are not a match :('
    return conclusion
                             
conclusion = compatibility(sign, potential_match, potential_match_sign, my_score)
print(conclusion)
                         
    
    
