#!/usr/bin/env python3

from sys import stdout


def main_loop():
    tpb = TenPinBowling()
    while True:
        player_name = input("Enter the name of a player or DONE to finish: ")
        if player_name == 'DONE':
            break
        tpb.add_player(player_name)
    tpb.play()


class Player(object):
    def __init__(self, name):
        self._name = name
        self.scorecard = [None] * 10

    @property
    def name(self):
        return self._name

    def set_frame_score(self,frame,score):
        self.scorecard[frame] = score

    def get_frame_scores(self):
        cumulative_scores = [''] * 10
        add_back = [0] * 10
        for i in range(len(self.scorecard)):
            if not self.scorecard[i]:
                break
            
            if i == 0:
                cumulative_scores[i] = 0
            else:
                cumulative_scores[i] = cumulative_scores[i-1]

            frame_score = 0
            for j in range(len(self.scorecard[i])):
                pins = self.scorecard[i][j]
                if pins < 0:
                    break
                frame_score += pins

                # Add this score to the previous strike or spare score.
                add_back_total = 0
                for x in range(i):
                    if add_back[x] > 0:
                        add_back[x] -= 1
                        cumulative_scores[x] += pins + add_back_total
                        cumulative_scores[i] += pins
                        add_back_total += pins

                # Add current frame score to the current total
                cumulative_scores[i] += pins

                # If we have a strike or spare, register for add_back
                if pins == 10:
                    add_back[i] = 2
                    if i < 9:
                        break
                elif frame_score == 10:
                    add_back[i] = 1
            
        return cumulative_scores

    def print_scorecard(self):
        print('\n +' + '-' * (len(self.name)+2) + '+')
        print('/  {}  \\'.format(self.name))
        print('+' + '-----+' * 10)
        stdout.write('|')
        f=0
        for frame in self.scorecard:
            if not frame:
                stdout.write(" | | |")
                continue
            a = b = c = ' '

            # Use 'X' to indicate a strike
            if frame[0] == 10:
                a = 'X'
                b = '-'
            # Use '/' to indicate a spare
            elif sum(frame[:2]) == 10:
                a = frame[0]
                b = '/'
            # Use 0-9 for every other score
            else:
                a = frame[0]
                b = frame[1]

            # If third value isn't -1, we're in the last frame
            # Players take up to two extra shots. Strike = 2, Spare = 1 (as normal)
            if frame[2] != -1:
                b = frame[1]
                if b == 10:
                    b = 'X'
                elif sum(frame[:2]) == 10:
                    b = '/'
                c = frame[2]
                if c == 10:
                    c = 'X'
            stdout.write("{}|{}|{}|".format(a,b,c))
            f+=1
        print()
        stdout.write('|')
        for score in self.get_frame_scores():
            stdout.write('{:^5}|'.format(score))
        print('\n+' + '-----+' * 10)
        print('\n')


class TenPinBowling(object):
    def __init__(self):
        self.players = []

    def add_player(self, player_name):
        self.players.append( Player(player_name) )

    def _get_pins_score(self,player,frame,current_score):
        prompt = "Pins bowled by {} (frame {}): ".format(player.name,frame+1)
        score = -1
        while score < 0:
            try:
                score = int(input(prompt))

                if score < 0:
                    raise ValueError()
                
                if frame < 9 and (score > 10 or current_score + score > 10):
                    raise ValueError()
                
                if frame == 9:
                    if score > 10 or current_score + score > 30:
                        raise ValueError()
                    if current_score < 10 and score + current_score > 10:
                        raise ValueError()

            except ValueError as e:
                print("Invalid Score entered! - try again...")
                score = -1
        return score

    def play(self):
        # GAME...
        for frame in range(10):
            for player in self.players:
                frame_score = 0
                a,b,c = (0,-1,-1)
                score = self._get_pins_score(player,frame,frame_score)
                frame_score += score
                a = score

                if score < 10 or (frame == 9 and frame_score == 10):
                    score = self._get_pins_score(player,frame,frame_score)
                    frame_score += score
                    b = score

                if frame == 9 and frame_score >= 10:
                    score = self._get_pins_score(player,frame,frame_score)
                    frame_score += score
                    c = score

                player.set_frame_score(frame, (a,b,c))
                player.print_scorecard()

        # Show scorecards for every player
        print('\n>>> FINAL SCORES <<<')
        for player in self.players:
            player.print_scorecard()


if __name__ == '__main__':
    main_loop()
