from cards import Card, Shoe
from map import *

roundsToSim = 1000000
deckCount = 6




def getVal(card):
    return valueMap[card.getId()]

def playHandScore(playerHand):
    currentScore = 0
    for card in playerHand:
        if (card.getId() != 1):
            currentScore += getVal(card)
        else:
            currentScore += 11
            if (currentScore > 21):
                currentScore -= 10
    return currentScore
    

def shouldPlayerStay(playerHand, dealerUp):
    playerHandVal = 0
    playerAceNum = 0
    for card in playerHand:
        if (card.getId() != 1):
            playerHandVal += getVal(card)
        else:
            playerAceNum += 1
    if (playerHandVal <= 11 and playerAceNum == 0):
        return False
    elif (playerHandVal >= 17 and playerAceNum == 0):
        return True
    elif (playerHandVal >= 8 and playerAceNum == 1):
        return True
    elif (playerHandVal <= 6 and playerAceNum == 1):
        return False
    elif (playerAceNum > 1):
        # EVENTUALLY FIX THIS, PLAYER SHOULD NOT ALWAYS STAY WITH TWO ACES
        # ADD SPLITTING
        # hailey bixley IS COOL :)
        # BUT ALSO HOT :)
        return True
    else:
        #consult map
        try:
            return moveMap[playerHandVal, playerAceNum, dealerUp.getId()]
        except:
            print("Im confused by: " + playerHand + ", " + dealerUp)
            return True
    
def shouldDealerStay(cards):
    currentScore = 0
    for card in cards:
        if (card.getId() != 1):
            currentScore += getVal(card)
        else:
            currentScore += 11
            if (currentScore >= 17 and currentScore <= 21):
                return True
            elif (currentScore >= 21):
                currentScore -= 10
    if currentScore > 17:
        return True
    return False

                



if __name__ == '__main__':

    shoe = Shoe(deckCount)
    shoe.shuffle()
    shoe.draw_1()

    lost = []
    won = []

    for i in range(roundsToSim):
        if len(shoe)<((deckCount*52)/2):
            #reshuffle shoe
            shoe = Shoe(deckCount)
            shoe.shuffle()
            shoe.draw_1()

        # STEP ONE: Setting up hands
        # First dealer card is up card
        playerCards = []
        dealerCards = []
        playerCards.append(shoe.draw_1())
        dealerCards.append(shoe.draw_1())
        playerCards.append(shoe.draw_1())
        dealerCards.append(shoe.draw_1())


        # STEP TWO: Play
        playerScore = playHandScore(playerCards)
        playerStay = shouldPlayerStay(playerCards, dealerCards[0])
        while not playerStay:
            playerCards.append(shoe.draw_1())
            playerStay = shouldPlayerStay(playerCards, dealerCards[0])
            playerScore = playHandScore(playerCards)
            if playerScore > 21:
                break

        if playerScore > 21:
            lost.append(i)
            continue
        
        #STEP THREE: Dealers plays
        while not shouldDealerStay(dealerCards):
            dealerCards.append(shoe.draw_1())
        if playHandScore(dealerCards)>21:
            #Player won
            won.append(i)
            continue

        #STEP FOUR: showdown in town with a gown and a clown
        if playHandScore(dealerCards)>=playHandScore(playerCards):
            lost.append(i)
        else:
            won.append(i)
    print("Player won: " + str(round(len(won)/(len(won)+len(lost)),4)*100) + "%")
        





        



