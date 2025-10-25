#Return Values Recap

my_name = "bee"
my_age = 12
my_color_eyes = "brown"

# f"{}" #format f포맷팅
print(f" hello i'm {my_name}, i have {my_age} years in the earth, {my_color_eyes} is my eye color")

def make_juice(fruit):
    return f"{fruit} + 🥤"

def add_ice(juice):
    return f"{juice} + 🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+ 🍬"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)