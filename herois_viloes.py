import random

super_heroes = ["Spider-Man","Iron Man","Captain America","Thor","Hulk","Black Panther","Doctor","Strange","Vision"]
super_villians = ["Magneto","Doctor Doom","Thanos","Loki","Galactus","Kingpin","Green Goblin","Venon"]

while len(super_villians) > 0:  
    heroi = random.choice(super_heroes)
    vilao = random.choice(super_villians)
    print(f"Combate de {heroi} contra {vilao}")

    super_heroes.remove(heroi)
    super_villians.remove(vilao)

    combate = [heroi,vilao]
    vencedor = random.choice(combate)
    print(f"Vencedor foi {vencedor}")
    

