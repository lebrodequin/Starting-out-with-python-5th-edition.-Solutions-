NUM_OF_HOTDOGS_IN_PACK = 10
NUM_OF_BUNS_IN_PACK = 8

num_of_visitors = float(input('input the number of visitors\n'))
num_of_hotdogs_for_a_person = float(input('how many hot dogs would everybody like to have?\n'))
total_num_of_hotdogs = num_of_hotdogs_for_a_person * num_of_visitors

if total_num_of_hotdogs % NUM_OF_HOTDOGS_IN_PACK != 0:
    hotdog_pack = total_num_of_hotdogs // NUM_OF_HOTDOGS_IN_PACK + 1
    hotdog_leftover = hotdog_pack * NUM_OF_HOTDOGS_IN_PACK - total_num_of_hotdogs
    print (f'you need to buy {hotdog_pack:.0f} hot dog packs and {hotdog_leftover:.0f} hot dogs would be leftover')
    
elif total_num_of_hotdogs % NUM_OF_HOTDOGS_IN_PACK == 0:
    hotdog_pack = total_num_of_hotdogs / NUM_OF_HOTDOGS_IN_PACK
    hotdog_leftover = hotdog_pack * NUM_OF_HOTDOGS_IN_PACK - total_num_of_hotdogs
    print (f'you need to buy {hotdog_pack:.0f} hot dog packs and {hotdog_leftover:.0f} hot dogs would be leftover')
    
if total_num_of_hotdogs// NUM_OF_BUNS_IN_PACK != 0:
    bun_pack = total_num_of_hotdogs// NUM_OF_BUNS_IN_PACK + 1
    bun_leftover = bun_pack * NUM_OF_BUNS_IN_PACK - total_num_of_hotdogs
    print (f'you need to buy {bun_pack:.0f} bun packs and {bun_leftover:.0f} buns would be leftover')
    
elif total_num_of_hotdogs// NUM_OF_BUNS_IN_PACK == 0:
    bun_pack = total_num_of_hotdogs/ NUM_OF_BUNS_IN_PACK
    bun_leftover = bun_pack * NUM_OF_BUNS_IN_PACK - total_num_of_hotdogs
    print (f'you need to buy {bun_pack:.0f} bun packs and {bun_leftover:.0f} buns would be leftover')
