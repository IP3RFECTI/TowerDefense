import csv
import pygame


class Leaderboard():

    """statistics"""
    def __init__(self, screen):
        """stat init"""
        self.path = 'assets/leaderboard/leaderboard.csv'
        self.file_data = []
        self.titles = ["Name", "Score"]
        self.check_file()
        self.ARIAL_50 = pygame.font.SysFont('arial', 50)
        self.screen = screen
        self.clicked = True

    def write_new_record(self, new_record):
        """writes record"""
        new_data = []
        for values in range(1, len(self.file_data)):
            current_name = self.file_data[values][0]
            if "Player" == current_name and self.new_score_is_more(new_record):
                new_data.append(["Player", int(new_record)])
            else:
                new_data.append([self.file_data[values][0], int(self.file_data[values][1])])
        new_data.sort(key=lambda x: x[1], reverse=True)
        new_data2 = new_data
        new_data = [self.titles]
        for val in new_data2:
            new_data.append(val)
        with open(self.path, mode="w", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
            for i in new_data:
                file_writer.writerow([i[0], str(i[1])])


    def check_file(self):
        try:
            with open("assets/leaderboard/leaderboard.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file)
                for val in file_reader:
                    self.file_data.append(val)
        except FileNotFoundError:
            with open(self.path, mode="w", encoding='utf-8') as w_file:
                file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=self.titles)
                file_writer.writeheader()
                file_writer.writerow({self.titles[0]: "Alex", self.titles[1]: str(1000)})
                file_writer.writerow({self.titles[0]: "Player", self.titles[1]: str(0)})

    def new_score_is_more(self, new_record):
        for val in self.file_data:
            if val[0] == "Player" and int(val[1]) < new_record:
                return True
        return False

    def draw_leaderboards(self):
        counter = 0
        for name, val in self.file_data:
            if counter == 0:
                draw = self.ARIAL_50.render(name + "                  " +
                                            val, True, (255, 255, 255))
                self.screen.blit(draw, (200, 400 + (counter*50)))
            else:
                draw = self.ARIAL_50.render(name + ": ", True, (255, 255, 255))
                self.screen.blit(draw, (200, 400 + (counter*50)))
                draw = self.ARIAL_50.render(val, True, (255, 255, 255))
                self.screen.blit(draw, (510, 400 + (counter*50)))
            counter += 1


    def leaderboard_clicked(self):
        """start click check"""
        if self.clicked:
            self.clicked = False
        else:
            self.clicked = True