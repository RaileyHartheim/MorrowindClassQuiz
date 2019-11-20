print("Hello there! You have come to the right place if you don't know what class to choose. You will be asked ten multiple-choice questions, and we try to suggest the class that best fits your answers. So you need to choose an appropriate answer and just type 1, 2 or 3. \n")

combat = 0
magic = 0
stealth = 0

first_answer = input("Question 1: On a clear day you chance upon a strange animal, its leg trapped in a hunter's clawsnare. Judging from the bleeding it will not survive long. \n 1. Draw your dagger, mercifully ending its life with a single thrust. \n 2. Use herbs from your pack to put it to sleep. \n 3. Do not interfere in the natural evolution of events, but rather take the opportunity to learn more about a strange animal you have never seen before. \n Please, type your answer:  ")
if first_answer == "1":
    combat += 1
elif first_answer == "2":
    magic += 1
elif first_answer == "3":
    stealth += 1

second_answer = input("Question 2: One Summer afternoon your father gives you a choice of chores. \n 1. Work in the forge with him casting iron for a new plow. \n 2. Gather herbs for your mother who is preparing dinner. \n 3. Go catch fish at the stream using a net and line. \n Please, type your answer:  ")
if second_answer == "1":
    combat += 1
elif second_answer == "2":
    magic += 1
elif second_answer == "3":
    stealth += 1

third_answer = input("Question 3: Your cousin has given you a very embarrassing nickname and, even worse, likes to call you it in front of your friends. You asked him to stop, but he finds it very amusing to watch you blush. \n 1. Beat up your cousin, then tell him that if he ever calls you that nickname again, you will bloody him worse than this time. \n 2. Make up a story that makes your nickname a badge of honor instead of something humiliating. \n 3. Make up an even more embarrassing nickname for him and use it constantly until he learns his lesson. \n Please, type your answer:  ")
if third_answer == "1":
    combat += 1
elif third_answer == "2":
    magic += 1
elif third_answer == "3":
    stealth += 1

fourth_answer = input("Question 4: There is a lot of heated discussion at the local tavern over a grouped of people called 'Telepaths'. They have been hired by certain City-State kings. Rumor has it these Telepaths read a person's mind and tell their lord whether a follower is telling the truth or not. \n 1. This is a terrible practice. A person's thoughts are his own and no one, not even a king, has the right to make such an invasion into another human's mind. \n 2. Loyal followers to the king have nothing to fear from a Telepath. It is important to have a method of finding assassins and spies before it is too late. \n 3. In these times, it is a necessary evil. Although you do not necessarily like the idea, a Telepath could have certain advantages during a time of war or in finding someone innocent of a crime. \n Please, type your answer:  ")
if fourth_answer == "1":
    combat += 1
elif fourth_answer == "2":
    magic += 1
elif fourth_answer == "3":
    stealth += 1

fifth_answer = input("Question 5: Your mother sends you to the market with a list of goods to buy. After you finish you find that by mistake a shopkeeper has given you too much money back in exchange for one of the items. \n 1. Return to the store and give the shopkeeper his hard-earned money, explaining to him the mistake. \n 2. Decide to put the extra money to good use and purchase items that would help your family. \n 3. Pocket the extra money, knowing that shopkeepers in general tend to overcharge customers anyway. \n Please, type your answer:  ")
if fifth_answer == "1":
    combat += 1
elif fifth_answer == "2":
    magic += 1
elif fifth_answer == "3":
    stealth += 1

sixth_answer = input("Question 6: While in the market place you witness a thief cut a purse from a noble. Even as he does so, the noble notices and calls for the city guards. In his haste to get away, the thief drops the purse near you. Surprisingly no one seems to notice the bag of coins at your feet. \n 1. Pick up the bag and signal to the guard, knowing that the only honorable thing to do is return the money to its rightful owner. \n 2. Leave the bag there, knowing that it is better not to get involved. \n 3. Pick up the bag and pocket it, knowing that the extra windfall will help your family in times of trouble. \n Please, type your answer:  ")
if sixth_answer == "1":
    combat += 1
elif sixth_answer == "2":
    magic += 1
elif sixth_answer == "3":
    stealth += 1

seventh_answer = input("Question 7: Your father sends you on a task which you loathe, cleaning the stables. On the way there, pitchfork in hand, you run into your friend from the homestead near your own. He offers to do it for you, in return for a future favor of his choosing. \n 1. Decline his offer, knowing that your father expects you to do the work, and it is better not to be in debt. \n 2. Ask him to help you, knowing that two people can do the job faster than one, and agree to help him with one task of his choosing in the future. \n 3. Accept his offer, reasoning that as long as the stables are cleaned, it matters not who does the cleaning. \n Please, type your answer:  ")
if seventh_answer == "1":
    combat += 1
elif seventh_answer == "2":
    magic += 1
elif seventh_answer == "3":
    stealth += 1

eigth_answer = input("Question 8: Your mother asks you to help fix the stove. While you are working, a very hot pipe slips its mooring and falls towards her. \n 1. Position yourself between the pipe and your mother. \n 2. Grab the hot pipe and try to push it away. \n 3. Push your mother out of the way. \n Please, type your answer:  ")
if eigth_answer == "1":
    combat += 1
elif eigth_answer == "2":
    magic += 1
elif eigth_answer == "3":
    stealth += 1

ninth_answer = input("Question 9: While in town the baker gives you a sweetroll. Delighted, you take it into an alley to enjoy only to be intercepted by a gang of three other kids your age. The leader demands the sweetroll, or else he and his friends will beat you and take it. \n 1. Drop the sweetroll and step on it, then get ready for the fight. \n 2. Give him the sweetroll now without argument, knowing that later this afternoon you will have all your friends with you and can come and take whatever he owes you. \n 3. Act like you're going to give him the sweetroll, but at the last minute throw it in the air, hoping that they'll pay attention to it long enough for you to get a shot in on the leader. \n Please, type your answer:  ")
if ninth_answer == "1":
    combat += 1
elif ninth_answer == "2":
    magic += 1
elif ninth_answer == "3":
    stealth += 1

tenth_answer = input("Question 10: Entering town you find that you are witness to a very well-dressed man running from a crowd. He screams to you for help. The crowd behind him seem very angry. \n 1. Rush to the town's aid immediately, despite your lack of knowledge of the circumstances. \n 2. Stand aside and allow the man and the mob to pass, realizing it is probably best not to get involved. \n 3. Rush to the man's aid immediately, despite your lack of knowledge of the circumstances. \n Please, type your answer:  ")
if tenth_answer == "1":
    combat += 1
elif tenth_answer == "2":
    magic += 1
elif tenth_answer == "3":
    stealth += 1

def chosen_class(combat, magic, stealth):
    if combat >= 7:
        return "Congratulations, warrior class suits you best!"
    elif magic >= 7:
        return "Congratulations, mage class suits you best!"
    elif stealth >= 7:
        return "Congratulations, thief class suits you best!"
    elif combat == 6 and magic == 4 or combat == 6 and magic == 2 and stealth == 2 or combat == 6 and stealth == 4:
        return "Congratulations, knight class suits you best!"
    elif combat == 6 and magic == 3 and stealth == 1:
        return "Congratulations, barbarian class suits you best!"
    elif combat == 6 and magic == 1 and stealth == 3:
        return "Congratulations, crusader class suits you best!"
    elif combat == 5 and magic == 5 or combat == 5 and magic == 4 and stealth == 1 or combat == 5 and magic == 1 and stealth == 4:
        return "Congratulations, archer class suits you best!"
    elif combat == 5 and magic == 2 and stealth == 3 or combat == 5 and magic == 3 and stealth == 2:
        return "Congratulations, scout class suits you best!"
    elif combat == 4 and magic == 1 and stealth == 5 or combat == 4 and stealth == 6 or combat == 5 and stealth == 5:
        return "Congratulations, rogue class suits you best!"
    elif combat == 3 and magic == 6 and stealth == 1 or combat == 4 and magic == 6:
        return "Congratulations, healer class suits you best!"
    elif combat == 3 and magic == 5 and stealth == 2 or combat == 2 and magic == 5 and stealth == 3:
        return "Congratulations, witchhunter class suits you best!"
    elif combat == 3 and magic == 4 and stealth == 3 or combat == 1 and magic == 4 and stealth == 5 or magic == 4 and stealth == 6:
        return "Congratulations, spellsword class suits you best!"
    elif combat == 3 and magic == 2 and stealth == 5:
        return "Congratulations, pilgrim class suits you best!"
    elif combat == 4 and magic == 3 and stealth == 3 or combat == 4 and magic == 4 and stealth == 2:
        return "Congratulations, bard class suits you best!"
    elif combat == 2 and magic == 4 and stealth == 4:
        return "Congratulations, nightblade class suits you best!"
    elif combat == 2 and magic == 3 and stealth == 5 or combat == 3 and magic == 3 and stealth == 4:
        return "Congratulations, monk class suits you best!"
    elif combat == 2 and magic == 2 and stealth == 6:
        return "Congratulations, acrobat class suits you best!"
    elif combat == 1 and magic == 3 and stealth == 6 or magic == 5 and stealth == 5:
        return "Congratulations, assassin class suits you best!"
    elif combat == 3 and magic == 1 and stealth == 6 or combat == 4 and magic == 2 and stealth == 4:
        return "Congratulations, agent class suits you best!"
    elif combat == 2 and magic == 6 and stealth == 2 or combat == 4 and magic == 5 and stealth == 1:
        return "Congratulations, sorcerer class suits you best!"
    elif combat == 1 and magic == 6 and stealth == 3 or magic == 6 and stealth == 4 or combat == 1 and magic == 5 and stealth == 4:
        return "Congratulations, battlemage class suits you best!"
    else:
        return "Something gone wrong."

result = str(chosen_class(combat, magic, stealth))
print(result)