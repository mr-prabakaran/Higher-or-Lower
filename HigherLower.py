import random

about = [
    "LeBron James - An American basketball player known for his incredible skills and multiple NBA championships.",
    "Beyoncé - A globally acclaimed singer and performer from the USA, famous for her powerful voice and dynamic stage presence.",
    "Taylor Swift - An American singer-songwriter celebrated for her hit albums and storytelling through music.",
    "Cristiano Ronaldo - A Portuguese football star renowned for his goal-scoring prowess and numerous awards.",
    "Kim Kardashian - An American media personality and businesswoman known for her reality TV presence and fashion ventures.",
    "Dwayne Johnson - An American actor and former wrestler known for his charisma and roles in blockbuster films.",
    "Oprah Winfrey - An American talk show host and philanthropist recognized for her influential career and media empire.",
    "Leonardo DiCaprio - An American actor acclaimed for his performances in award-winning films and environmental activism.",
    "Rihanna - A Barbadian singer and entrepreneur celebrated for her music career and fashion line.",
    "Shakira - A Colombian singer and dancer known for her hit songs and vibrant performances.",
    "Angelina Jolie - An American actress and humanitarian recognized for her roles in films and international advocacy work.",
    "Justin Bieber - A Canadian pop singer famous for his youthful voice and chart-topping hits.",
    "Eminem - An American rapper and songwriter known for his influential lyrics and impactful music.",
    "Ariana Grande - An American singer and actress celebrated for her powerful vocals and chart-topping songs.",
    "Kylie Jenner - An American businesswoman and media personality known for her beauty brand and social media presence.",
    "Denzel Washington - An American actor and director known for his powerful performances and acclaimed films.",
    "Zendaya - An American actress and singer recognized for her roles in film and TV and her impact on pop culture.",
    "Tom Brady - An American football quarterback celebrated for his multiple Super Bowl victories and NFL records.",
    "Gigi Hadid - An American model known for her work in fashion and high-profile runway shows.",
    "David Beckham - An English football legend known for his exceptional skills and global impact on the sport.",
]

data = []

def generate_followers():
    return random.randint(1, 200)

for _ in range(100):
    followers = generate_followers()
    data.append({
        "about":random.choice(about),
        "followers": followers
    })

score = 0

highScore = 0

def compareFollowers(d1,d2):
    return "higher" if d1["followers"] < d2["followers"] else "lower" 
     
def HigherLower():
    global score,highScore
    while True:
        d1 = random.choice(data)
        d2 = random.choice(data)
        while d1 == d2:
            d2 = random.choice(data)

        print(f"""
"{d1["about"]}" has "{d1["followers"]} M"
-----------------------------------               vs               ----------------------------------------           
"{d2["about"]}" has?
(higher/lower)
""")    
        userInput = input().strip().lower()

        if userInput in ['higher','up','h', 'true', 't', '1']:
            userGuess = "higher"
        elif userInput in ['lower','down', 'l', 'false', 'f', '0']:
            userGuess = "lower"
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
            continue

        if userGuess == compareFollowers(d1,d2):
            score += 1
            if score > highScore:
                highScore = score
            print(f'Correct! {d2["followers"]} M followers.')
            print(f"""
High Score: {highScore}                                                     Score: {score}
""")
        else:
            print(f'Incorrect. {d2["followers"]} M followers.')
            print(f"You Scored: {score}")
            break

HigherLower()