"""
Building on your solutions from the previous exercises, write a function 
`local_greet` that takes a locale as input, and returns a greeting. The locale 
lets us greet people from different countries appropriately, even when they 
share a common language, for example:

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

Distinguish greetings for English speaking countries like the US, UK, Canada, 
or Australia in your implementation, and feel free to fall back on the language
-specific greetings in all other cases, for example:

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

When implementing `local_greet`, make sure you re-use your `extract_language`, 
`extract_region`, and `greet` functions from the previous exercises.
"""
"""
I: a string (locale)
O: a string (greeting based on language & locale)

✱ QUESTIONS ✱
- 

✱ RULES ✱
- if the language is english, distinguish greeting from other english speaking
  countries like US, UK, AU, and canada.
- for all other languages, just return a greeting in that language, no need to
  distinguish between regions.

✱ EXAMPLES / TEST CASES ✱
- 'en_US.UTF-8' -> Hey!
- 'en_GB.UTF-8' -> Hello!
- 'en_AU.UTF-8' -> Howdy!
- 'fr_FR.UTF-8' -> Salut!
- 'fr_CA.UTF-8' -> Salut!

✱ DS ✱
- 

✱ ALGORITHM ✱
I: `locale`
[x] extract the language code by calling `extract_language()` function - assign 
   to `language`
[x] if language is english:
    [] extract the region by calling `extract_region()` function - assign to
       `region`
        [] if the region is the US:
          return 'Hey!'
        [] if the region is the UK:
            return 'Hello!'
        [] if the region is Australia:
            return 'Howdy!'
[x] else:
    [x] call the `greet()` function with `language` as the argument

"""
def greet(lang_code):
    match lang_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale[0:2]

def extract_region(locale):
    return locale[3:5]

def local_greet(locale):
    language = extract_language(locale)

    if language == 'en':
        region = extract_region(locale)
        match region:
            case 'US':
                return 'Hey!'
            case 'GB':
                return 'Hello!'
            case 'AU':
                return 'Howdy!'
    else:
        return greet(language)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!


# LS Solution
def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)
