##########################
######## Ping Pong! ######
##########################

# A game of table tennis almost always sounds like Ping! followed by Pong!
# You know that Player 2 won if you hear Pong! as the last sound (since Player 1 didn't return the ball back).
# Given an array of Ping!, create a function that inserts Pong! in betwen each element. Also:

# - If win euqals true, end the list with Pong!
# - If win equals false, end the list with Ping!

##Example 1
#pingPong(["Ping!"], True)
#output = ["Ping!", "Pong!"]
#
##Example 2
#pingPong(["Ping!", "Ping!"], False)
#output = ["Ping!", "Pong!", "Ping!"]
#
##Example 3
#pingPong(["Ping!", "Ping!", "Ping!"], True)
#output = ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"]

def pingPong(ping_pong_list, win):
    complete_ping_pong_list = []
    for i in range(len(ping_pong_list)):
        if i == len(ping_pong_list) - 1 and not win:
            complete_ping_pong_list.append(ping_pong_list[i])
        else:
            complete_ping_pong_list.append(ping_pong_list[i])
            complete_ping_pong_list.append("Pong!")
    return complete_ping_pong_list


print(pingPong(["Ping!", "Ping!", "Ping!"], True))