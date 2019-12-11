def test_determine_zodiac():
    assert determine_zodiac(december, 21) == sagittarius
    assert determine_zodiac(february, 26) == pisces
    assert determine_zodiac(june, 20) == cancer
    assert determine_zodiac(september, 14) == virgo
    
def test_horoscope_traits():
    assert horoscope_traits(gemini) == ' versatile and expressive'
    assert horoscope_traits(libra) == ' social and diplomatic'
    assert horoscope_traits(scorpio) == ' resourceful and brave'
    assert horoscope_traits(leo) == ' self-assured and outgoing'
    
def test_compatibility():
    assert compatibility(gemini, Kat, pisces, 43) == '\n\nYou and Kat are not a match :('
    assert compatibility(libra, Balazs, aries, 41) == '\n\nYou and Balazs are a match!'