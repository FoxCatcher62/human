import file_operations
from faker import Faker
import random


fake = Faker("ru_RU")
first_name = fake.first_name()
last_name = fake.last_name()
job = fake.job()
town = fake.city()

strength = random.randint(3,18)
agility = random.randint(3,18)
endurance = random.randint(3,18)
intelligence = random.randint(3,18)
luck = random.randint(3,18)
skils = ["Стремительный прыжок","Электрический выстрел", "Ледяной удар","Стремительный удар","Кислотный взгляд","Тайный побег","Ледяной выстрел","Огненный заряд"]
ez = random.sample(skils,3)
skill_1 = ez[0]
skill_2 = ez[1]
skill_3 = ez [2]


langueage = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}
langueage.items()


context = {
"first_name": first_name ,
"last_name": last_name,
"job": job,
"town": town,
"strength": strength,
"agility": agility,
"endurance": endurance,
"intelligence": intelligence,
"luck": luck,

"skill_1": skill_1.replace("е","е͠'"),
"skill_2": skill_2.replace("е","е͠'"),
"skill_3": skill_3.replace("е","е͠'")
}
# for lang1,lang2 in langueage.items():
#     print((skill_1, skill_2, skill_3).format(lang1, lang2))


    
file_operations.render_template("E:\\python_project\\5\\charsheet\\charsheet.svg", "E:\\python_project\\5\\cahrsheet_new\\result.svg", context)