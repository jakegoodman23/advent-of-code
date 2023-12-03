def get_score(s):
    roll_list = s.split(" ")

    return int(roll_list[0])

with open("day_2_input.txt", "r") as file:
    correct_game_ids = set()
    bad_game_ids = set()
    for line in file:
        line = line.replace("\n", "")
        game_id = int(line.split()[1].replace(":", ""))
        rolls = line.split(": ")[1]
        rolls = rolls.split("; ")
        for roll in rolls:
            roll = roll.split(", ")
            blue_score = 0
            red_score = 0
            green_score = 0
            for dice in roll:
                if dice.find("blue") != -1:
                    blue_score += get_score(dice)
                if dice.find("red") != -1:
                    red_score += get_score(dice)
                if dice.find("green") != -1:
                    green_score += get_score(dice)
            if red_score <= 12 and green_score <= 13 and blue_score <= 14:
                correct_game_ids.add(game_id)
            else:
                bad_game_ids.add(game_id)
    correct_game_ids -= bad_game_ids
    print(f"Part I Solution: {sum(correct_game_ids)}")

with open("day_2_input.txt", "r") as file:
    total = 0
    for line in file:
        line = line.replace("\n", "")
        game_id = int(line.split()[1].replace(":", ""))
        rolls = line.split(": ")[1]
        rolls = rolls.split("; ")
        blue_score = 0
        red_score = 0
        green_score = 0
        for roll in rolls:
            roll = roll.split(", ")
            for dice in roll:
                if dice.find("blue") != -1:
                    blue_score = max(get_score(dice), blue_score)
                if dice.find("red") != -1:
                    red_score = max(get_score(dice), red_score)
                if dice.find("green") != -1:
                    green_score = max(get_score(dice), green_score)
        total += (blue_score * red_score * green_score)
    print(f"Part II Solution: {total}")            
  