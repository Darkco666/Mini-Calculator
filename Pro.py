# The calculator app with oop and more easy to read readable

# MeCalculator

from tkinter import *


def calculator_conc():  # Calc contenent Function

    # ======Create The App window====== #
    app = Tk()
    app.geometry('400x400')
    app.resizable(False, False)
    app.iconbitmap(
        r'C:\Users\M.N.S\OneDrive\Desktop\M.N.S\P\python\Images\Education__9_.ico')
    app.title('MEcalc')
    app.config(bg='#121212')

    # The Container Entry
    ent1_con = Entry(app, fg='orange', bg='#121212', font=('Helvetica', 23, 'bold'), width=23,
                     border=3, justify='right', relief='flat')

    ent1_con.place(x=1, y=50)

    # ==============================================================================================#

    class ControlConc:  # The class that make the content of the calc

        dote_allow = 'yes'  # To allow to add dote the default is yes
        delet_equal_value = 'no'  # To allow delete the equal value

        def __init__(self, master, value='Nothing') -> None:

            self._master = master
            self._value = value

    # ==============================================================================================#

        def create_b(self, x: int, y: int, w, b, cont: str = 'Button',
                     bgc: str = 'white', fgc: str = 'black', func=None):  # Create buttons func

            btn_num = Button(self._master, bg=bgc, fg=fgc, text=cont, font=('Helvetica', 15, 'bold'),
                             width=w, border=b, command=func, activebackground='gray',
                             activeforeground='white', relief='flat')

            btn_num.place(x=x, y=y)

    # ==============================================================================================#

        def add_numv(self):  # The function to add the numbers from 1 to 9 and 0

            if ent1_con.get() not in ['Error', 'no result']:

                if ControlConc.delet_equal_value != 'yes':

                    value1 = ent1_con.get()

                    if self._value == '0':

                        if len(ent1_con.get()) >= 1:  # check if the content length is able to 0 in it

                            ent1_con.delete(0, END)
                            ent1_con.insert(0, value1 + self._value)
                            FormatConc.format_conc()

                    else:  # We can add any number here
                        ent1_con.delete(0, END)
                        ent1_con.insert(0, value1 + self._value)
                        FormatConc.format_conc()

                else:

                    ent1_con.delete(0, END)
                    ent1_con.insert(0, self._value)
                    ControlConc.delet_equal_value = 'no'  # To stop deleting the value from entry

            # To remove the words that they are in the conc
            else:
                ent1_con.delete(0, END)
                self.add_numv()

    # ==============================================================================================#

        def add_toolv(self):  # The fuction to add the tools [+, -. /, x]

            if ent1_con.get() not in ['Error', 'no result']:

                value2 = ent1_con.get()
                if len(value2) >= 1 and value2[-1].isdigit():

                    if self._value == '.':
                        if ControlConc.dote_allow == 'yes':

                            ent1_con.delete(0, END)
                            ent1_con.insert(0, value2 + self._value)
                            ControlConc.dote_allow = 'no'  # To make the formator turn off
                            # To avoiod adding dote to avoid this 9....
                            FormatConc.allow_format = 'no'

                    else:

                        ent1_con.delete(0, END)
                        ent1_con.insert(0, value2 + self._value)
                        ControlConc.dote_allow = 'yes'  # To make the formator turn on
                        FormatConc.allow_format = 'yes'  # To make the dote be allowed to add to the conc

            ControlConc.delet_equal_value = 'no'  # To stop delet the value from the entry

    # ==============================================================================================#

        # +======Mission functions======+

        @staticmethod
        def equal():  # The equal function

            value4 = ent1_con.get(
            ).replace('*', '**').replace('x', '*').replace(',', '').replace('\xF7', '/')
            ent1_con.delete(0, END)

            if len(value4) >= 1:

                if value4[-1].isdigit():

                    try:
                        ent1_con.insert(0, f'{eval(value4):,d}')

                    except ZeroDivisionError:
                        ent1_con.insert(0, 'Error')

                    except:

                        total = '{:,f}'.format(eval(value4))  # The float natig
                        # The values before the dote(.)
                        cuttotal = total[: total.find('.')]
                        ntotal = ''  # The numbers after the dote(.)

                        # The function that organise the numbers after the . and with .
                        def check_float(item):  # This function is only for the equal func

                            if item == '.':
                                return True  # To add the . in the ntotal

                            else:
                                return int(item)  # To add the numbers

                        # We use the for loop :
                            # check_float to organise the nummbers after .
                            # adding the numbers after the . in the var ntotal
                        for item in filter(check_float, list(total[total.find('.'):])):

                            ntotal += item

                        # To check if there are no numbers only .
                        if ntotal.endswith('.'):

                            ent1_con.insert(
                                0, cuttotal + ntotal.replace('.', ''))

                        # If There are numbers
                        else:
                            ent1_con.insert(0, cuttotal + ntotal)

                # If the user didn't complete the question
                else:
                    ent1_con.insert(0, 'no resutl')

                # To allow deleting the conc when we add a new number
                ControlConc.delet_equal_value = 'yes'

    # ==============================================================================================#

        @staticmethod
        def delete():  # The delete function

            value4 = ent1_con.get()
            nvalue1 = value4[0: len(value4) - 1]

            if len(value4) >= 1:

                ent1_con.delete(0, END)
                ent1_con.insert(0, nvalue1)
                FormatConc.format_conc()

    # ==============================================================================================#

        @staticmethod
        def clear():  # The clear function

            if len(ent1_con.get()) >= 1:

                ent1_con.delete(0, END)
                # Those for return every thing like the first opening
                FormatConc.allow_format = 'yes'  # To make the formator work again
                ControlConc.dote_allow = 'yes'  # To make the dote be allowed to add to the conc

    # ==============================================================================================#

    class FormatConc(ControlConc):  # The class that formated the content of the class

        allow_format = 'yes'  # The default for the application to format the content

        @classmethod
        def format_conc(cls):

            value5 = ent1_con.get().replace(',', '')

            if cls.allow_format == 'yes':

                ent1_con.delete(0, END)

                nums = ''  # The numbers without tools to formated them easily
                nvalue2 = ''  # To formated value

                for item in value5:

                    # To check if the item is a number to add to nums variable
                    if item.isdigit():
                        nums += item

                    elif item == '.':
                        nums += item

                    else:

                        try:
                            nvalue2 += f'{int(nums):,d}' + item
                            nums = ''

                        except ValueError:

                            try:
                                nvalue2 += f'{float(nums):,.{len(nums[nums.find(".") + 1: ])}f}' + item
                                nums = ''

                            except ValueError:
                                pass

                        # To pass any error and because the try want except
                        except:
                            pass

                else:

                    try:

                        nvalue2 += f'{int(nums):,d}'  # To add the end values
                        # To add the new value in the conc after format it
                        ent1_con.insert(0, nvalue2)

                    except ValueError:
                        pass

    # ==============================================================================================#

    def nums_buttons():  # The function that contain the number buttons

        # Number one
        btn1 = ControlConc(app, '1')
        btn1.create_b(10, 140, 7, 2, '1', '#121212', 'orange', btn1.add_numv)

        # Number two
        btn2 = ControlConc(app, '2')
        btn2.create_b(115, 140, 7, 2, '2', '#121212', 'orange', btn2.add_numv)

        # Number three
        btn3 = ControlConc(app, '3')
        btn3.create_b(220, 140, 7, 2, '3', '#121212', 'orange', btn3.add_numv)

        # Number four
        btn4 = ControlConc(app, '4')
        btn4.create_b(10, 195, 7, 2, '4', '#121212', 'orange', btn4.add_numv)

        # Number five
        btn5 = ControlConc(app, '5')
        btn5.create_b(115, 195, 7, 2, '5', '#121212', 'orange', btn5.add_numv)

        # Number six
        btn6 = ControlConc(app, '6')
        btn6.create_b(220, 195, 7, 2, '6', '#121212', 'orange', btn6.add_numv)

        # Number seven
        btn7 = ControlConc(app, '7')
        btn7.create_b(10, 250, 7, 2, '7', '#121212', 'orange', btn7.add_numv)

        # Number eight
        btn8 = ControlConc(app, '8')
        btn8.create_b(115, 250, 7, 2, '8', '#121212', 'orange', btn8.add_numv)

        # Number nine
        btn9 = ControlConc(app, '9')
        btn9.create_b(220, 250, 7, 2, '9', '#121212', 'orange', btn9.add_numv)

        # Number zero
        btn10 = ControlConc(app, '0')
        btn10.create_b(115, 305, 7, 2, '0', '#121212',
                       'orange', btn10.add_numv)

    # ==============================================================================================#

    def tools_buttons():  # The fuctions that contain the tools buttons like +

        # Dote button
        btn1 = ControlConc(app, '.')
        btn1.create_b(10, 305, 7, 2, '.', '#121212', 'orange', btn1.add_toolv)

        # Addition button
        btn2 = ControlConc(app, '+')
        btn2.create_b(325, 140, 5, 2, '+', '#121212', 'orange', btn2.add_toolv)

        # Subtraction button
        btn3 = ControlConc(app, "-")
        btn3.create_b(325, 195, 5, 2, '-', '#121212', 'orange', btn3.add_toolv)

        # Multiplication button
        btn4 = ControlConc(app, 'x')
        btn4.create_b(325, 250, 5, 2, 'x', '#121212', 'orange', btn4.add_toolv)

        # Division button
        btn5 = ControlConc(app, '\xF7')
        btn5.create_b(325, 305, 5, 2, '\xF7', '#121212',
                      'orange', btn5.add_toolv)

        btn6 = ControlConc(app, '*')
        btn6.create_b(220, 305, 7, 2, '*', '#121212', 'orange', btn6.add_toolv)

    # ==============================================================================================#

    def mission_buttons():  # The function that contain the mission buttons like =

        # Equal button
        btn1 = ControlConc(app)
        btn1.create_b(220, 355, 14, 2, '=', '#121212', 'orange', btn1.equal)

        # Delete button
        btn2 = ControlConc(app)
        btn2.create_b(10, 355, 7, 2, 'Delete',
                      '#121212', 'orange', btn2.delete)

        # Clear button
        btn3 = ControlConc(app)
        btn3.create_b(115, 355, 7, 2, 'Clear', '#121212', 'orange', btn3.clear)

    # The nums functions, tools functions , missions functions calling
    nums_buttons()
    tools_buttons()
    mission_buttons()

    app.mainloop()  # To make the application run


if __name__ == '__main__':
    calculator_conc()  # To make the application run
