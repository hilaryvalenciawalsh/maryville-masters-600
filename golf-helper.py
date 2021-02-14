def golf():
    print('Welcome to the Golf Club Helper!')
    print('Tell me your situation, and I will recommend a club\n')

    green = input('Did you hit on the green (y/n)?: ').lower()
    farAway = int(input('How far is the ball from the hole (in yards)?: '))

    if green == 'y':
        print('I recommend using your Putter!')
    else:
        if farAway >= 200:
            print('I recommend using your Driver!')
        elif farAway >= 140:
            print('I recommend using your 5-Iron!')
        elif farAway >= 100:
            print('I recommend using your 9-Iron!')
        else:
            print('I recommend using your Pitching Wedge!')


golf()
