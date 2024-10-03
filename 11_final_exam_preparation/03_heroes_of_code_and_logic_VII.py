number_of_heroes = int(input())
heroes = {}
maximum_hp = 100
maximum_mp = 200

for _ in range(number_of_heroes):
    name, hp, mp = input().split()
    heroes[name] = [int(hp), int(mp)]


def cast_spell(hero, mana_cost, spell):
    if heroes[hero][1] >= mana_cost:
        heroes[hero][1] -= mana_cost
        print(f"{hero} has successfully cast {spell} and now has {heroes[hero][1]} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell}!")


def take_damage(hero, damage, attacker):
    if damage < heroes[hero][0]:
        heroes[hero][0] -= damage
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!")
    else:
        del heroes[hero]
        print(f"{hero} has been killed by {attacker}!")


def recharge(hero, amount):
    if heroes[hero][1] + amount >= maximum_mp:
        amount_recovered = maximum_mp - heroes[hero][1]
        heroes[hero][1] = maximum_mp
        print(f"{hero} recharged for {amount_recovered} MP!")
    else:
        heroes[hero][1] += amount
        print(f"{hero} recharged for {amount} MP!")


def heal(hero, amount):
    if heroes[hero][0] + amount >= maximum_hp:
        amount_recovered = maximum_hp - heroes[hero][0]
        heroes[hero][0] = maximum_hp
        print(f"{hero} healed for {amount_recovered} HP!")
    else:
        heroes[hero][0] += amount
        print(f"{hero} healed for {amount} HP!")


def print_function():
    for hero, values in heroes.items():
        print(f"{hero}\n\tHP: {values[0]}\n\tMP: {values[1]}")


def heroes_of_code_and_logic_main():
    while True:
        command = input()
        if command == "End":
            break

        command_split = command.split(" - ")
        action, hero = command_split[0], command_split[1]

        if action == "CastSpell":
            mana_needed, spell = int(command_split[2]), command_split[3]
            cast_spell(hero, mana_needed, spell)

        elif action == "TakeDamage":
            damage, attacker = int(command_split[2]), command_split[3]
            take_damage(hero, damage, attacker)

        elif action == "Recharge":
            amount = int(command_split[2])
            recharge(hero, amount)

        elif action == "Heal":
            amount = int(command_split[2])
            heal(hero, amount)

    print_function()


heroes_of_code_and_logic_main()
