import tkinter as tk
from tkinter import ttk

version = 1


class Main:
    dict_phases = {'dzien': 'Dzienny', 'tydzien': 'Tygodniowy', 'dwatygodnie': 'dwu tygodniowy',
                   'trzytygodnie': 'trzy tygodniowy', 'miesiac': 'Miesieczny',
                   'trzymiesiace': 'trzy miesieczny', 'polroku': 'pol roczny', 'rok': 'Roczny',
                   'dwalata': 'dwuletni', 'pieclat': 'piecioletni'}

    savings_phases = {'dzien': 'Dziennie', 'tydzien': 'Tygodniowo', 'dwatygodnie': 'dwu tygodniowo',
                      'trzytygodnie': 'trzy tygodniowo', 'miesiac': 'Miesiecznie',
                      'trzymiesiace': 'trzy miesiecznie', 'polroku': 'pol rocznie', 'rok': 'Rocznie',
                      'dwalata': 'dwuletnie', 'pieclat': 'piecioletnie'}

    recurring_phases = {'dzien': 'Dzienne', 'tydzien': 'Tygodniowe', 'dwatygodnie': 'dwu tygodniowe',
                        'trzytygodnie': 'trzy tygodniowe', 'miesiac': 'Miesieczne',
                        'trzymiesiace': 'trzy miesieczne', 'polroku': 'pol roczne', 'rok': 'Roczne',
                        'dwalata': 'dwuletnie', 'pieclat': 'piecioletnie'}

    visible_phases = ['Dzien', 'Tydzien', 'dwa tygodnie', 'trzy tygodnie', 'Miesiac', 'trzy miesiace', 'pol roku',
                      'Rok', 'dwa lata', 'piec lat']

    day_phases = {'dzien': 1, 'tydzien': 7, 'dwatygodnie': 14, 'trzytygodnie': 21, 'miesiac': 30,
                  'trzymiesiace': 91, 'polroku': 182, 'rok': 365, 'dwalata': 730, 'pieclat': 1825}

    week_phases = {'dzien': 7, 'tydzien': 1, 'dwatygodnie': 2, 'trzytygodnie': 3, 'miesiac': 4,
                   'trzymiesiace': 12, 'polroku': 24, 'rok': 48, 'dwalata': 96, 'pieclat': 240}

    two_weeks_phases = {'dzien': 14, 'tydzien': 2, 'dwatygodnie': 1, 'trzytygodnie': 1.5, 'miesiac': 2,
                        'trzymiesiace': 6, 'polroku': 12, 'rok': 24, 'dwalata': 48, 'pieclat': 120}

    three_weeks_phases = {'dzien': 21, 'tydzien': 3, 'dwatygodnie': 1.5, 'trzytygodnie': 1, 'miesiac': 1.4,
                          'trzymiesiace': 4.2, 'polroku': 8.4, 'rok': 16.8, 'dwalata': 33.6, 'pieclat': 84}

    month_phases = {'dzien': 30, 'tydzien': 4, 'dwatygodnie': 2, 'trzytygodnie': 1.4, 'miesiac': 1,
                    'trzymiesiace': 3, 'polroku': 6, 'rok': 12, 'dwalata': 24, 'pieclat': 60}

    three_months_phases = {'dzien': 90, 'tydzien': 12, 'dwatygodnie': 6, 'trzytygodnie': 4, 'miesiac': 3,
                           'trzymiesiace': 1, 'polroku': 2, 'rok': 4, 'dwalata': 8, 'pieclat': 20}

    half_year_phases = {'dzien': 180, 'tydzien': 25, 'dwatygodnie': 12, 'trzytygodnie': 8, 'miesiac': 6,
                        'trzymiesiace': 2, 'polroku': 1, 'rok': 2, 'dwalata': 4, 'pieclat': 10}

    year_phases = {'dzien': 365, 'tydzien': 52, 'dwatygodnie': 26, 'trzytygodnie': 17, 'miesiac': 12,
                   'trzymiesiace': 4, 'polroku': 2, 'rok': 1, 'dwalata': 2, 'pieclat': 5}

    two_years_phases = {'dzien': 730, 'tydzien': 104, 'dwatygodnie': 52, 'trzytygodnie': 34, 'miesiac': 24,
                        'trzymiesiace': 8, 'polroku': 4, 'rok': 2, 'dwalata': 1, 'pieclat': 2.5}

    five_years_phases = {'dzien': 1825, 'tydzien': 260, 'dwatygodnie': 130, 'trzytygodnie': 85, 'miesiac': 60,
                         'trzymiesiace': 20, 'polroku': 10, 'rok': 5, 'dwalata': 2.5, 'pieclat': 1}

    more_or_end = ['Wiecej', 'Zakoncz']

    def __init__(self):
        self.income = 0
        self.recurring = 0
        self.expenses = 0
        self.income_phase = ''
        self.recurring_phase = ''
        self.expenses_phase = ''
        self.more_income_value = ''
        self.more_recurring_value = ''
        self.more_expenses_value = ''
        self.combobox_value_phase_income = ''
        self.combobox_value_phase_recurring = ''
        self.combobox_value_phase_expenses = ''
        self.combobox_value_savings = ''
        self.savings = 0
        self.changing_income = 0
        self.changing_recurring = 0
        self.changing_expenses = 0
        self.savings_phase = ''
        self.savings_phase_recurring = ''
        self.you_earn = ''
        self.recurring_costs = ''
        self.seem = ''
        self.saves = ''
        self.saving_data = None

    def first_greeting(self):
        window = tk.Tk()
        window.minsize(800, 800)
        width_value = window.winfo_screenwidth()
        height_value = window.winfo_screenheight()
        window.maxsize(width_value, height_value)
        window.title("ALOS BudgetTracker")
        window.wm_iconbitmap('ikona.ico')

        label = ttk.Label(window, text='Witaj w aplikacji Sledzenie budzetu! \nDziekuje ze wybrales moja aplikacje!')
        label.grid(column=0, row=0)
        label.config(font=("Courier", 20))

        def if_clicked():
            self.combobox_value_phase_income = ''
            self.combobox_value_phase_recurring = ''
            self.combobox_value_phase_expenses = ''
            self.combobox_value_savings = ''
            window.destroy()
            self.income_phase_ask()

        button = ttk.Button(text="ZACZYNAJMY", command=if_clicked, width=50)
        button.grid(column=0, row=1)

        window.mainloop()

    def combo_box(self, label_top_text, combo_values, method_name):
        window = tk.Tk()
        window.minsize(800, 800)
        width_value = window.winfo_screenwidth()
        height_value = window.winfo_screenheight()
        window.maxsize(width_value, height_value)
        window.title("ALOS BudgetTracker")
        window.wm_iconbitmap('ikona.ico')

        label = ttk.Label(window, text=label_top_text)
        label.grid(column=0, row=0)

        def getting_combobox_value():
            if label_top_text == 'Co ile dostajesz pieniadze Netto?':
                self.combobox_value_phase_income = combobox.get()
                for key, value in self.dict_phases.items():
                    if key == self.combobox_value_phase_income.replace(" ", "").lower():
                        self.income_phase = value
            elif label_top_text == 'Jesli masz wiecej niz jeden dochod wybierz "Wiecej" jesli nie wybierz "Zakoncz"':
                combobox_value_more_income = combobox.get()
                self.more_income_value = combobox_value_more_income.lower()
            elif label_top_text == 'Co ile masz powtarzajace sie koszty?':
                self.combobox_value_phase_recurring = combobox.get()
                for key, value in self.recurring_phases.items():
                    if key == self.combobox_value_phase_recurring.replace(" ", "").lower():
                        self.recurring_phase = value
            elif label_top_text == 'Jesli masz wiecej niz jeden powtarzajacy sie koszt wybierz "Wiecej" jesli nie ' \
                                   'wybierz "Zakoncz"':
                combobox_value_more_recurring = combobox.get()
                self.more_recurring_value = combobox_value_more_recurring.lower()
            elif label_top_text == 'Co ile masz swoje wydatki?':
                self.combobox_value_phase_expenses = combobox.get()
                for key, value in self.dict_phases.items():
                    if key == self.combobox_value_phase_expenses.replace(" ", "").lower():
                        self.expenses_phase = value
            elif label_top_text == 'Jesli masz wiecej niz jeden wydatek wybierz "Wiecej" jesli nie wybierz "Zakoncz"':
                combobox_value_more_expenses = combobox.get()
                self.more_expenses_value = combobox_value_more_expenses.lower()

        combobox = ttk.Combobox(window, width=15, state="readonly")
        combobox.bind("<<ComboboxSelected>>", lambda _: getting_combobox_value())
        combobox['values'] = combo_values
        combobox.grid(column=1, row=0)
        combobox.current(0)

        def if_clicked():
            window.destroy()
            if method_name == 'income_ask':
                self.income_ask()
            elif method_name == 'more_income_ask':
                if self.more_income_value == 'wiecej':
                    self.income_ask()
                elif self.more_income_value == 'zakoncz':
                    self.recurring_phase_ask()
                else:
                    self.Error_box(method_error='more_income_ask', label_top_text='Blad! Wybierz "Wiecej" lub '
                                                                                  '"Zakoncz"! Sprobuj Ponownie!')
            elif method_name == 'recurring_ask':
                self.recurring_ask()
            elif method_name == 'more_recurring_ask':
                if self.more_recurring_value == 'wiecej':
                    self.recurring_ask()
                elif self.more_recurring_value == 'zakoncz':
                    self.expenses_phase_ask()
                else:
                    self.Error_box(method_error='more_recurring_ask', label_top_text='Blad! Wybierz "Wiecej" lub '
                                                                                     '"Zakoncz"! Sprobuj Ponownie!')
            elif method_name == 'expenses_ask':
                self.expenses_ask()
            elif method_name == 'more_expenses_ask':
                if self.more_expenses_value == 'wiecej':
                    self.expenses_ask()
                elif self.more_expenses_value == 'zakoncz':
                    self.window_with_everything()
                else:
                    self.Error_box(method_error='more_expenses_ask', label_top_text='Blad! Wybierz "Wiecej" lub '
                                                                                    '"Zakoncz"! Sprobuj Ponownie!')

        def if_back():
            window.destroy()
            if method_name == 'income_ask':
                self.income_phase = ''
                self.combobox_value_phase_income = ''
                self.first_greeting()
            elif method_name == 'more_income_ask':
                self.income = 0
                self.more_income_value = ''
                self.income_ask()
            elif method_name == 'recurring_ask':
                self.recurring_phase = ''
                self.more_income_value = ''
                self.combobox_value_phase_recurring = ''
                self.more_income_ask()
            elif method_name == 'more_recurring_ask':
                self.recurring = 0
                self.more_recurring_value = ''
                self.recurring_ask()
            elif method_name == 'expenses_ask':
                self.expenses_phase = ''
                self.more_recurring_value = ''
                self.combobox_value_phase_expenses = ''
                self.more_recurring_ask()
            elif method_name == 'more_expenses_ask':
                self.expenses = 0
                self.more_expenses_value = ''
                self.expenses_ask()

        button = ttk.Button(text="DALEJ", command=if_clicked, width=50)
        button.grid(column=0, row=1)
        button = ttk.Button(text="COFNIJ", command=if_back, width=50)
        button.grid(column=0, row=3)

        window.mainloop()

    def Error_box(self, method_error, label_top_text):
        window = tk.Tk()
        window.minsize(800, 800)
        width_value = window.winfo_screenwidth()
        height_value = window.winfo_screenheight()
        window.maxsize(width_value, height_value)
        window.title("ALOS BudgetTracker")
        window.wm_iconbitmap('ikona.ico')

        label = ttk.Label(window, text=label_top_text)
        label.grid(column=0, row=0)

        def if_clicked():
            if method_error == 'income_ask':
                window.destroy()
                self.income_ask()
            elif method_error == 'income_phase_ask':
                window.destroy()
                self.income_phase_ask()
            elif method_error == 'more_income_ask':
                window.destroy()
                self.more_income_ask()
            elif method_error == 'recurring_phase_ask':
                window.destroy()
                self.recurring_phase_ask()
            elif method_error == 'recurring_ask':
                window.destroy()
                self.recurring_ask()
            elif method_error == 'more_recurring_ask':
                window.destroy()
                self.more_recurring_ask()
            elif method_error == 'expenses_phase_ask':
                window.destroy()
                self.expenses_phase_ask()
            elif method_error == 'expenses_ask':
                window.destroy()
                self.expenses_ask()
            elif method_error == 'more_expenses_ask':
                window.destroy()
                self.more_expenses_ask()

        button = ttk.Button(text="SPROBUJ  PONOWNIE!", command=if_clicked, width=50)
        button.grid(column=0, row=1)

        window.mainloop()

    def input_box(self, label_top_text, method_name):
        window = tk.Tk()
        window.minsize(800, 800)
        width_value = window.winfo_screenwidth()
        height_value = window.winfo_screenheight()
        window.maxsize(width_value, height_value)
        window.title("ALOS BudgetTracker")
        window.wm_iconbitmap('ikona.ico')

        label = ttk.Label(window, text=label_top_text)
        label.grid(column=0, row=0)

        inputbox = tk.Entry(window, bd=5, width=50)
        inputbox.grid(column=0, row=1)

        def if_clicked():
            if method_name == 'income_ask':
                income_value = inputbox.get()
                try:
                    int_value = int(income_value)
                    self.income += int_value
                except ValueError:
                    window.destroy()
                    self.Error_box(method_error='income_ask', label_top_text='Blad! To nie jest Pelna liczba! '
                                                                             'Sprobuj Ponownie!')
                else:
                    window.destroy()
                    self.more_income_ask()
            elif method_name == 'recurring_ask':
                recurring_value = inputbox.get()
                try:
                    int_value = int(recurring_value)
                    self.recurring += int_value
                except ValueError:
                    window.destroy()
                    self.Error_box(method_error='recurring_ask', label_top_text='Blad! To nie jest Pelna liczba! '
                                                                                'Sprobuj Ponownie!')
                else:
                    window.destroy()
                    self.more_recurring_ask()
            elif method_name == 'expenses_ask':
                expenses_value = inputbox.get()
                try:
                    int_value = int(expenses_value)
                    self.expenses += int_value
                except ValueError:
                    window.destroy()
                    self.Error_box(method_error='expenses_ask', label_top_text='Blad! To nie jest Pelna liczba! '
                                                                               'Sprobuj Ponownie!')
                else:
                    window.destroy()
                    self.more_expenses_ask()

        def if_back():
            window.destroy()
            if method_name == 'income_ask':
                self.income_phase = ''
                self.income = 0
                self.combobox_value_phase_income = ''
                self.income_phase_ask()
            elif method_name == 'recurring_ask':
                self.recurring = 0
                self.recurring_phase = ''
                self.combobox_value_phase_recurring = ''
                self.recurring_phase_ask()
            elif method_name == 'expenses_ask':
                self.expenses = 0
                self.expenses_phase = ''
                self.combobox_value_phase_expenses = ''
                self.expenses_phase_ask()

        button = ttk.Button(text="DALEJ", command=if_clicked, width=50)
        button.grid(column=0, row=2)
        button = ttk.Button(text="COFNIJ", command=if_back, width=50)
        button.grid(column=0, row=3)

        window.mainloop()

    def income_phase_ask(self):
        self.combo_box(label_top_text='Co ile dostajesz pieniadze Netto?', combo_values=self.visible_phases,
                       method_name='income_ask')

    def income_ask(self):
        if self.combobox_value_phase_income in self.visible_phases:
            self.input_box(label_top_text=f'Wprowadz {self.income_phase} dochod Netto (pelna liczbe!)',
                           method_name='income_ask')
        else:
            self.Error_box(method_error='income_phase_ask', label_top_text='Blad! Wybierz Co ile dostajesz pieniadze '
                                                                           'Netto! Sprobuj Ponownie!')

    def more_income_ask(self):
        self.combo_box(label_top_text='Jesli masz wiecej niz jeden dochod wybierz "Wiecej" jesli nie wybierz "Zakoncz"',
                       combo_values=self.more_or_end, method_name='more_income_ask')

    def recurring_phase_ask(self):
        self.combo_box(label_top_text='Co ile masz powtarzajace sie koszty?', combo_values=self.visible_phases,
                       method_name='recurring_ask')

    def recurring_ask(self):
        if self.combobox_value_phase_recurring in self.visible_phases:
            self.input_box(label_top_text=f'Wprowadz {self.recurring_phase} powtarzajace sie koszty (pelna liczbe!)',
                           method_name='recurring_ask')
        else:
            self.Error_box(method_error='recurring_phase_ask', label_top_text='Blad! Wybierz Co ile masz powtarzajace '
                                                                              'sie koszty! Sprobuj Ponownie!')

    def more_recurring_ask(self):
        self.combo_box(label_top_text='Jesli masz wiecej niz jeden powtarzajacy sie koszt wybierz "Wiecej" jesli nie '
                                      'wybierz "Zakoncz"',
                       combo_values=self.more_or_end, method_name='more_recurring_ask')

    def expenses_phase_ask(self):
        self.combo_box(label_top_text='Co ile masz swoje wydatki?', combo_values=self.visible_phases,
                       method_name='expenses_ask')

    def expenses_ask(self):
        if self.combobox_value_phase_expenses in self.visible_phases:
            self.input_box(label_top_text=f'Wprowadz {self.expenses_phase} wydatek (pelna liczbe!)',
                           method_name='expenses_ask')
        else:
            self.Error_box(method_error='expenses_phase_ask', label_top_text='Blad! Wybierz Co ile masz wydatki! '
                                                                             'Sprobuj Ponownie!')

    def more_expenses_ask(self):
        self.combo_box(label_top_text='Jesli masz wiecej niz jeden wydatek wybierz "Wiecej" jesli nie wybierz '
                                      '"Zakoncz"', combo_values=self.more_or_end, method_name='more_expenses_ask')

    def window_with_everything(self):
        window = tk.Tk()
        window.minsize(800, 800)
        width_value = window.winfo_screenwidth()
        height_value = window.winfo_screenheight()
        window.maxsize(width_value, height_value)
        window.title("ALOS BudgetTracker")
        window.wm_iconbitmap('ikona.ico')

        label = ttk.Label(window, text='Wybierz z jakiego okresu czasu chcesz zobacycz ile oszczedzasz.Jesli chcesz '
                                       'zobaczyc drugi raz kliknij w przycisk jeszcze raz')
        label.grid(column=5, row=0)

        def on_choice():
            def if_clicked():
                window.destroy()
                self.window_with_everything()

            button = ttk.Button(text="JESZCZE RAZ", command=if_clicked, width=20)
            button.grid(column=5, row=7)

            self.combobox_value_savings = combobox.get()
            self.calculations()
            self.savings = self.changing_income - self.changing_recurring - self.changing_expenses
            combobox.destroy()
            for key, value in self.savings_phases.items():
                if key == self.combobox_value_savings.replace(" ", "").lower():
                    self.savings_phase = value

            for key, value in self.recurring_phases.items():
                if key == self.combobox_value_savings.replace(" ", "").lower():
                    self.savings_phase_recurring = value

            label2 = ttk.Label(window, text=f'{self.you_earn} {self.savings_phase}: {self.changing_income}')
            label2.grid(column=5, row=3)
            label3 = ttk.Label(window, text=f'{self.savings_phase_recurring} {self.recurring_costs} '
                                            f'{self.changing_recurring}')
            label3.grid(column=5, row=4)
            label4 = ttk.Label(window, text=f'{self.seem} {self.savings_phase}: {self.changing_expenses}')
            label4.grid(column=5, row=5)
            label5 = ttk.Label(window, text=f'{self.saves} {self.savings_phase}: {self.savings}')
            label5.grid(column=5, row=6)

        combobox = ttk.Combobox(window, width=15, state="readonly")
        combobox.bind("<<ComboboxSelected>>", lambda _: on_choice())
        combobox['values'] = self.visible_phases
        combobox.grid(column=5, row=1)
        combobox.current(0)

        def if_restart():
            window.destroy()
            self.first_greeting()

        button_restart = ttk.Button(text="OD POCZATKU", command=if_restart, width=20)
        button_restart.grid(column=5, row=9)

        window.mainloop()

    def calculations(self):
        self.changing_income = self.income
        self.changing_recurring = self.recurring
        self.changing_expenses = self.expenses
        self.you_earn = 'Zarabiasz'
        self.recurring_costs = 'powtarzajace sie koszty:'
        self.seem = 'Wydajesz'
        self.saves = 'Oszczedzasz'
        if self.combobox_value_savings == 'Dzien':
            for key, value in self.day_phases.items():
                if key == self.combobox_value_phase_income.replace(" ", "").lower():
                    self.changing_income //= value
                if key == self.combobox_value_phase_recurring.replace(" ", "").lower():
                    self.changing_recurring //= value
                if key == self.combobox_value_phase_expenses.replace(" ", "").lower():
                    self.changing_expenses //= value
        elif self.combobox_value_savings == 'Tydzien':
            for key, value in self.week_phases.items():
                if key == self.combobox_value_phase_income.replace(" ", "").lower():
                    if self.combobox_value_phase_income == 'Dzien':
                        self.changing_income *= value
                    else:
                        self.changing_income //= value
                if key == self.combobox_value_phase_recurring.replace(" ", "").lower():
                    if self.combobox_value_phase_recurring == 'Dzien':
                        self.changing_recurring *= value
                    else:
                        self.changing_recurring //= value
                if key == self.combobox_value_phase_expenses.replace(" ", "").lower():
                    if self.combobox_value_phase_expenses == 'Dzien':
                        self.changing_expenses *= value
                    else:
                        self.changing_expenses //= value
        elif self.combobox_value_savings == 'dwa tygodnie':
            for key, value in self.two_weeks_phases.items():
                if key == self.combobox_value_phase_income.replace(" ", "").lower():
                    if self.combobox_value_phase_income == 'Dzien' or self.combobox_value_phase_income == 'Tydzien':
                        self.changing_income *= value
                    else:
                        self.changing_income //= value
                if key == self.combobox_value_phase_recurring.replace(" ", "").lower():
                    if self.combobox_value_phase_recurring == 'Dzien' or self.combobox_value_phase_recurring == \
                            'Tydzien':
                        self.changing_recurring *= value
                    else:
                        self.changing_recurring //= value
                if key == self.combobox_value_phase_expenses.replace(" ", "").lower():
                    if self.combobox_value_phase_expenses == 'Dzien' or self.combobox_value_phase_expenses == \
                            'Tydzien':
                        self.changing_expenses *= value
                    else:
                        self.changing_expenses //= value
        elif self.combobox_value_savings == 'trzy tygodnie':
            for key, value in self.three_weeks_phases.items():
                if key == self.combobox_value_phase_income.replace(" ", "").lower():
                    if self.combobox_value_phase_income == 'Dzien' or self.combobox_value_phase_income == 'Tydzien' or \
                            self.combobox_value_phase_income == 'dwa tygodnie':
                        self.changing_income *= value
                    else:
                        self.changing_income //= value
                if key == self.combobox_value_phase_recurring.replace(" ", "").lower():
                    if self.combobox_value_phase_recurring == 'Dzien' or self.combobox_value_phase_recurring == \
                            'Tydzien' or self.combobox_value_phase_recurring == 'dwa tygodnie':
                        self.changing_recurring *= value
                    else:
                        self.changing_recurring //= value
                if key == self.combobox_value_phase_expenses.replace(" ", "").lower():
                    if self.combobox_value_phase_expenses == 'Dzien' or self.combobox_value_phase_expenses == \
                            'Tydzien' or self.combobox_value_phase_expenses == 'dwa tygodnie':
                        self.changing_expenses *= value
                    else:
                        self.changing_expenses //= value
        elif self.combobox_value_savings == 'Miesiac':
            for key, value in self.month_phases.items():
                if key == self.combobox_value_phase_income.replace(" ", "").lower():
                    if self.combobox_value_phase_income == 'Dzien' or self.combobox_value_phase_income == 'Tydzien' or \
                            self.combobox_value_phase_income == 'dwa tygodnie' or self.combobox_value_phase_income == \
                            'trzy tygodnie':
                        self.changing_income *= value
                    else:
                        self.changing_income //= value
                if key == self.combobox_value_phase_recurring.replace(" ", "").lower():
                    if self.combobox_value_phase_recurring == 'Dzien' or self.combobox_value_phase_recurring == \
                            'Tydzien' or self.combobox_value_phase_recurring == 'dwa tygodnie' or \
                            self.combobox_value_phase_recurring == 'trzy tygodnie':
                        self.changing_recurring *= value
                    else:
                        self.changing_recurring //= value
                if key == self.combobox_value_phase_expenses.replace(" ", "").lower():
                    if self.combobox_value_phase_expenses == 'Dzien' or self.combobox_value_phase_expenses == \
                            'Tydzien' or self.combobox_value_phase_expenses == 'dwa tygodnie' or \
                            self.combobox_value_phase_expenses == 'trzy tygodnie':
                        self.changing_expenses *= value
                    else:
                        self.changing_expenses //= value
        elif self.combobox_value_savings == 'trzy miesiace':
            for key, value in self.three_months_phases.items():
                if key == self.combobox_value_phase_income.replace(" ", "").lower():
                    if self.combobox_value_phase_income == 'Dzien' or self.combobox_value_phase_income == 'Tydzien' or \
                            self.combobox_value_phase_income == 'dwa tygodnie' or self.combobox_value_phase_income == \
                            'trzy tygodnie' or self.combobox_value_phase_income == 'Miesiac':
                        self.changing_income *= value
                    else:
                        self.changing_income //= value
                if key == self.combobox_value_phase_recurring.replace(" ", "").lower():
                    if self.combobox_value_phase_recurring == 'Dzien' or self.combobox_value_phase_recurring == \
                            'Tydzien' or self.combobox_value_phase_recurring == 'dwa tygodnie' or \
                            self.combobox_value_phase_recurring == 'trzy tygodnie' or \
                            self.combobox_value_phase_recurring == 'Miesiac':
                        self.changing_recurring *= value
                    else:
                        self.changing_recurring //= value
                if key == self.combobox_value_phase_expenses.replace(" ", "").lower():
                    if self.combobox_value_phase_expenses == 'Dzien' or self.combobox_value_phase_expenses == \
                            'Tydzien' or self.combobox_value_phase_expenses == 'dwa tygodnie' or \
                            self.combobox_value_phase_expenses == 'trzy tygodnie' or \
                            self.combobox_value_phase_expenses == 'Miesiac':
                        self.changing_expenses *= value
                    else:
                        self.changing_expenses //= value
        elif self.combobox_value_savings == 'pol roku':
            for key, value in self.half_year_phases.items():
                if key == self.combobox_value_phase_income.replace(" ", "").lower():
                    if self.combobox_value_phase_income == 'Dzien' or self.combobox_value_phase_income == 'Tydzien' or \
                            self.combobox_value_phase_income == 'dwa tygodnie' or self.combobox_value_phase_income == \
                            'trzy tygodnie' or self.combobox_value_phase_income == 'Miesiac' or \
                            self.combobox_value_phase_income == 'trzy miesiace':
                        self.changing_income *= value
                    else:
                        self.changing_income //= value
                if key == self.combobox_value_phase_recurring.replace(" ", "").lower():
                    if self.combobox_value_phase_recurring == 'Dzien' or self.combobox_value_phase_recurring == \
                            'Tydzien' or self.combobox_value_phase_recurring == 'dwa tygodnie' or \
                            self.combobox_value_phase_recurring == 'trzy tygodnie' or \
                            self.combobox_value_phase_recurring == 'Miesiac' or self.combobox_value_phase_income == \
                            'trzy miesiace':
                        self.changing_recurring *= value
                    else:
                        self.changing_recurring //= value
                if key == self.combobox_value_phase_expenses.replace(" ", "").lower():
                    if self.combobox_value_phase_expenses == 'Dzien' or self.combobox_value_phase_expenses == \
                            'Tydzien' or self.combobox_value_phase_expenses == 'dwa tygodnie' or \
                            self.combobox_value_phase_expenses == 'trzy tygodnie' or \
                            self.combobox_value_phase_expenses == 'Miesiac' or self.combobox_value_phase_expenses == \
                            'trzy miesiace':
                        self.changing_expenses *= value
                    else:
                        self.changing_expenses //= value
        elif self.combobox_value_savings == 'Rok':
            for key, value in self.year_phases.items():
                if key == self.combobox_value_phase_income.replace(" ", "").lower():
                    if self.combobox_value_phase_income == 'Dzien' or self.combobox_value_phase_income == 'Tydzien' or \
                            self.combobox_value_phase_income == 'dwa tygodnie' or self.combobox_value_phase_income == \
                            'trzy tygodnie' or self.combobox_value_phase_income == 'Miesiac' or \
                            self.combobox_value_phase_income == 'trzy miesiace' or self.combobox_value_phase_income == \
                            'pol roku':
                        self.changing_income *= value
                    else:
                        self.changing_income //= value
                if key == self.combobox_value_phase_recurring.replace(" ", "").lower():
                    if self.combobox_value_phase_recurring == 'Dzien' or self.combobox_value_phase_recurring == \
                            'Tydzien' or self.combobox_value_phase_recurring == 'dwa tygodnie' or \
                            self.combobox_value_phase_recurring == 'trzy tygodnie' or \
                            self.combobox_value_phase_recurring == 'Miesiac' or self.combobox_value_phase_income == \
                            'trzy miesiace' or self.combobox_value_phase_recurring == 'pol roku':
                        self.changing_recurring *= value
                    else:
                        self.changing_recurring //= value
                if key == self.combobox_value_phase_expenses.replace(" ", "").lower():
                    if self.combobox_value_phase_expenses == 'Dzien' or self.combobox_value_phase_expenses == \
                            'Tydzien' or self.combobox_value_phase_expenses == 'dwa tygodnie' or \
                            self.combobox_value_phase_expenses == 'trzy tygodnie' or \
                            self.combobox_value_phase_expenses == 'Miesiac' or self.combobox_value_phase_expenses == \
                            'trzy miesiace' or self.combobox_value_phase_expenses == 'pol roku':
                        self.changing_expenses *= value
                    else:
                        self.changing_expenses //= value
        elif self.combobox_value_savings == 'dwa lata':
            for key, value in self.two_years_phases.items():
                if key == self.combobox_value_phase_income.replace(" ", "").lower():
                    if self.combobox_value_phase_income == 'Dzien' or self.combobox_value_phase_income == 'Tydzien' or \
                            self.combobox_value_phase_income == 'dwa tygodnie' or self.combobox_value_phase_income == \
                            'trzy tygodnie' or self.combobox_value_phase_income == 'Miesiac' or \
                            self.combobox_value_phase_income == 'trzy miesiace' or self.combobox_value_phase_income == \
                            'pol roku' or self.combobox_value_phase_income == 'Rok':
                        self.changing_income *= value
                    else:
                        self.changing_income //= value
                if key == self.combobox_value_phase_recurring.replace(" ", "").lower():
                    if self.combobox_value_phase_recurring == 'Dzien' or self.combobox_value_phase_recurring == \
                            'Tydzien' or self.combobox_value_phase_recurring == 'dwa tygodnie' or \
                            self.combobox_value_phase_recurring == 'trzy tygodnie' or \
                            self.combobox_value_phase_recurring == 'Miesiac' or self.combobox_value_phase_income == \
                            'trzy miesiace' or self.combobox_value_phase_recurring == 'pol roku' or \
                            self.combobox_value_phase_recurring == 'Rok':
                        self.changing_recurring *= value
                    else:
                        self.changing_recurring //= value
                if key == self.combobox_value_phase_expenses.replace(" ", "").lower():
                    if self.combobox_value_phase_expenses == 'Dzien' or self.combobox_value_phase_expenses == \
                            'Tydzien' or self.combobox_value_phase_expenses == 'dwa tygodnie' or \
                            self.combobox_value_phase_expenses == 'trzy tygodnie' or \
                            self.combobox_value_phase_expenses == 'Miesiac' or self.combobox_value_phase_expenses == \
                            'trzy miesiace' or self.combobox_value_phase_expenses == 'pol roku' or \
                            self.combobox_value_phase_expenses == 'Rok':
                        self.changing_expenses *= value
                    else:
                        self.changing_expenses //= value
        elif self.combobox_value_savings == 'piec lat':
            for key, value in self.five_years_phases.items():
                if key == self.combobox_value_phase_income.replace(" ", "").lower():
                    if self.combobox_value_phase_income == 'Dzien' or self.combobox_value_phase_income == 'Tydzien' or \
                            self.combobox_value_phase_income == 'dwa tygodnie' or self.combobox_value_phase_income == \
                            'trzy tygodnie' or self.combobox_value_phase_income == 'Miesiac' or \
                            self.combobox_value_phase_income == 'trzy miesiace' or self.combobox_value_phase_income == \
                            'pol roku' or self.combobox_value_phase_income == 'Rok' or \
                            self.combobox_value_phase_income == 'dwa lata':
                        self.changing_income *= value
                    else:
                        self.changing_income //= value
                if key == self.combobox_value_phase_recurring.replace(" ", "").lower():
                    if self.combobox_value_phase_recurring == 'Dzien' or self.combobox_value_phase_recurring == \
                            'Tydzien' or self.combobox_value_phase_recurring == 'dwa tygodnie' or \
                            self.combobox_value_phase_recurring == 'trzy tygodnie' or \
                            self.combobox_value_phase_recurring == 'Miesiac' or self.combobox_value_phase_income == \
                            'trzy miesiace' or self.combobox_value_phase_recurring == 'pol roku' or \
                            self.combobox_value_phase_recurring == 'Rok' or self.combobox_value_phase_recurring == \
                            'dwa lata':
                        self.changing_recurring *= value
                    else:
                        self.changing_recurring //= value
                if key == self.combobox_value_phase_expenses.replace(" ", "").lower():
                    if self.combobox_value_phase_expenses == 'Dzien' or self.combobox_value_phase_expenses == \
                            'Tydzien' or self.combobox_value_phase_expenses == 'dwa tygodnie' or \
                            self.combobox_value_phase_expenses == 'trzy tygodnie' or \
                            self.combobox_value_phase_expenses == 'Miesiac' or self.combobox_value_phase_expenses == \
                            'trzy miesiace' or self.combobox_value_phase_expenses == 'pol roku' or \
                            self.combobox_value_phase_expenses == 'Rok' or self.combobox_value_phase_expenses == \
                            'dwa lata':
                        self.changing_expenses *= value
                    else:
                        self.changing_expenses //= value


if __name__ == '__main__':
    m = Main
    m.first_greeting(Main())
