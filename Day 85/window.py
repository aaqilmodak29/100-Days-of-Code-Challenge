from tkinter import *
from sentences import SENTENCES
import random
import time

FONT = ('Arial', 15)
TIME_IN_MS = 60000


class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title('Typing Speed Test')
        self.window.minsize(width=500, height=400)
        self.window.config(padx=50, pady=50)

        self.start = time.time()
        self.total_words = 0
        self.wpm = 0
        self.timer = 60
        self.errors = 0
        self.elapsed_time = 0
        self.wrong_inputs = []
        self.wrong_inputs_time = []

        self.label_1 = Label(text='Start Typing...', font=FONT)
        self.label_1.grid(column=0, row=1)

        self.label_2 = Label(text=random.choice(SENTENCES), font=FONT)
        self.label_2.grid(column=1, row=2)

        self.label_3 = Label(text='', font=FONT)
        self.label_3.grid(column=2, row=4)
        try:
            with open('HighScores.txt', mode='r') as file:
                score = file.read()
                self.label_4 = Label(text='Current High Score: {}'.format(score), font=FONT)
                self.label_4.grid(column=1, row=0)

        except FileNotFoundError:
            with open('HighScores.txt', mode='w') as file:
                file.write('0')
            with open('HighScores.txt', mode='r') as read_file:
                score = read_file.read()
                self.label_4 = Label(text='Current High Score: {}'.format(score), font=FONT)
                self.label_4.grid(column=1, row=0)

        self.receive_input = Entry(width=50)
        self.receive_input.focus()
        self.receive_input.grid(column=2, row=2)
        self.receive_input.size()

        # self.button_1 = Button(self.window, text='Check Speed', command=self.read_input)
        # self.button_1.grid(column=2, row=3)

        self.window.bind('<Return>', self.read_input)
        self.window.after(TIME_IN_MS, self.window.destroy)

        self.window.mainloop()

        print('Total Time Elapsed Since Last Entry: {} seconds,\n'
              'Words Per Minute: {},\n'
              'Number of Errors: {}.'.format(self.elapsed_time, self.wpm, self.errors))
        print('\n')

        with open('HighScores.txt', mode='r') as file:
            score = file.read()
            if self.wpm > float(score):
                with open('HighScores.txt', mode='w') as write_to_file:
                    write_to_file.write(str(self.wpm))

        for i in range(len(self.wrong_inputs)):
            print('Wrong input "{}" at {} seconds'.format(self.wrong_inputs[i], self.wrong_inputs_time[i]))

    def read_input(self, event):
        end = time.time()
        self.elapsed_time = round(end - self.start, 2)
        elapsed_time_in_minutes = self.elapsed_time / 60

        response = self.receive_input.get()
        self.receive_input.delete(0, END)
        if response == self.label_2['text']:
            words = response.split()
            for word in words:
                # characters per minute as given online as to how to calculate wpm
                self.total_words += len(list(word))

                # # calculation of literal words per minute
                # self.total_words += len(list(word))

            self.wpm = round((self.total_words / 5) / elapsed_time_in_minutes, 1)
            try:
                num = random.randint(0, len(SENTENCES) - 1)
                self.label_2['text'] = SENTENCES[num]
                self.label_3['text'] = 'Keep it Up!'
            except ValueError:
                self.label_3['text'] = '0 sentences Left! Total Time Elapsed: {}! WPM: {}!'.format(self.elapsed_time,
                                                                                                   self.wpm)

            self.label_3['text'] = 'Total Time Elapsed: {}!'.format(self.elapsed_time)
        else:
            self.label_3['text'] = '{} is wrong! Try again! Total Time Elapsed: {}!'.format(response, self.elapsed_time)
            self.errors += 1
            self.wrong_inputs.append(response)
            self.wrong_inputs_time.append(self.elapsed_time)

