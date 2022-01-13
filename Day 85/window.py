from tkinter import *
from sentences import SENTENCES
import random
import time

FONT = ('Arial', 15)
TIME_IN_MS = 60000

# COMPLETE_SENTENCE = []


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
        self.wrong_inputs = []
        self.wrong_inputs_time = []

        self.label_1 = Label(text='Start Typing...', font=FONT)
        self.label_1.grid(column=0, row=0)

        self.label_2 = Label(text=random.choice(SENTENCES), font=FONT)
        self.label_2.grid(column=1, row=1)

        self.label_3 = Label(text='', font=FONT)
        self.label_3.grid(column=2, row=3)

        self.receive_input = Entry(width=50)
        self.receive_input.focus()
        self.receive_input.grid(column=2, row=2)
        self.receive_input.size()

        # self.button_1 = Button(self.window, text='Check Speed', command=self.read_input)
        # self.button_1.grid(column=2, row=3)

        self.window.bind('<Return>', self.read_input)
        self.window.after(TIME_IN_MS, self.window.destroy)

        self.window.mainloop()

        print('Total Time Elapsed: {} seconds,\n'
              'Words Per Minute: {},\n'
              'Number of Errors: {}.'.format(TIME_IN_MS/1000, self.wpm, self.errors))
        print('\n')
        for i in range(len(self.wrong_inputs)):
            print('Wrong input "{}" at {} seconds'.format(self.wrong_inputs[i], self.wrong_inputs_time[i]))

    def read_input(self, event):
        end = time.time()
        elapsed_time = round(end - self.start, 2)
        elapsed_time_in_minutes = elapsed_time / 60

        response = self.receive_input.get()
        self.receive_input.delete(0, END)
        if response in SENTENCES:
            words = response.split()
            for word in words:
                self.total_words += len(word)
            self.wpm = round((self.total_words / 5) / elapsed_time_in_minutes, 1)
            try:
                num = random.randint(0, len(SENTENCES) - 1)
                self.label_2['text'] = SENTENCES[num]
                self.label_3['text'] = 'Keep it Up!'
            except ValueError:
                self.label_3['text'] = '0 sentences Left! Total Time Elapsed: {}! WPM: {}!'.format(elapsed_time,
                                                                                                   self.wpm)

            self.label_3['text'] = 'Total Time Elapsed: {}!'.format(elapsed_time)
        else:
            self.label_3['text'] = '{} not in List! Total Time Elapsed: {}!'.format(response, elapsed_time)
            self.errors += 1
            self.wrong_inputs.append(response)
            self.wrong_inputs_time.append(elapsed_time)
