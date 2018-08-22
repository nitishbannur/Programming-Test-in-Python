from tkinter import *

import tkinter.messagebox
import subprocess


root = Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()

root.geometry("%dx%d+0+0"%(w,h))

# use these variables to record final score and time used
points = 0
time_used = 0  # time used will be stored in seconds

timer = Label(root, font=('arial', 15, 'bold'),bg="#a1dbcd")
totalPoints = Label(root, text="YOUR POINTS SO FAR: "+str(points), font=('arial', 18, 'bold'), justify="center",bg="#a1dbcd")


def game_over():
    root.destroy()
    root2 = Tk()
    score = Label(root2, text='Final score: %d' % points, font=('arial', 14, 'bold'), fg='green')
    score.pack()
    time = Label(root2, text='Time taken: %dmins %dsecs' % (time_used//60, time_used%60), font=('arial', 14, 'bold'))
    time.pack()

    # edit function for saving data


def point():
    global points
    points = points+5
    totalPoints['text'] = "YOUR POINTS SO FAR: "+str(points)


def point_minus():
    global points
    points = points - 1
    totalPoints['text'] = "YOUR POINTS SO FAR: " + str(points)


def countdown(count):
    global time_used
    time_used = 2700 - count
    if count > 0:
        mins = count // 60
        secs = count % 60
        timer['text'] = 'Time left: %dmins %dsecs' % (mins, secs)
        root.after(1000, countdown, count-1)
    else:
        timer['text'] = "Time's over!"
        game_over()


def instructions_page():

    root.title('Instructions')

    # add code to destroy widgets from login page
    user.destroy()
    username.destroy()
    passw.destroy()
    password.destroy()
    JAM.destroy()
    login_button.destroy()

    # add instructions widgets
    #
    #

    def first_problem():
        # add code to destroy widgets from instructions page
        #
        #
        start_button.destroy()

        root.title('First Problem')

        # Permanent labels-------------------
        timer.place(x=850, y=600)
        totalPoints.place(x=800, y=30)
        
        
        # -------------------------------------

        result = StringVar()
        resultLabel = Label(root, textvariable=result, font=('arial', 12, 'bold'),bg="#a1dbcd")
        resultLabel.place(x=500, y=600)

        errorText = StringVar()
        errorMsg = Message(root, textvariable=errorText, bg="#a1dbcd")
        errorMsg.place(x=850, y=100)

        Editor = Text(root, width=35, height=10)
        Editor.place(x=450, y=230)

        # exect for first problem
        def exect():
            with open("source1.1.cpp") as f:  # Take the first part of the code from source
                with open("runfile.cpp", 'w') as f1:
                    for line in f:
                        f1.write(line)
            f.close()  # Second part from user
            f1.close()
            entry = Editor.get("1.0", "end-1c")
            second = open("runfile.cpp", 'a')
            second.write(entry)
            second.close()

            with open("source1.2.cpp") as f:  # third part from source2
                with open("runfile.cpp", 'a') as f1:
                    for line in f:
                        f1.write(line)
            f.close()
            f1.close()

            with open('errorfile', 'w') as infile:  # If Errors found,Written in INFILE
                t1 = subprocess.call(["g++", "runfile.cpp"], stderr=infile)

            if t1 == 0:  # THE CONDITION THAT TELLS THAT IT's Compiled fine and get be executed
                with open('output', 'w') as outfile:  # Output Written on outfile
                    # subprocess.call(["./a.out"],stdout=outfile)
                    subprocess.call(["./a.out", "3", "1", "5", "0", "6", "2", "8", "1", "1"], stdout=outfile)

                succ1 = open('output', 'r')
                cool = succ1.read()
                if int(cool) == 568:
                    submit.destroy()
                    point()
                    resultLabel.config(fg='green', bg="#a1dbcd")
                    result.set("Result: Correct answer")
                    errorText.set("")
                else:
                    point_minus()
                    resultLabel.config(fg='red', bg="#a1dbcd")
                    result.set("Result: Incorrect answer")
                    errorText.set("")

            else:
                point_minus()
                err1 = open('errorfile', 'r')
                prob = err1.read()
                errorText.set(prob)
                resultLabel.config(fg='red', bg="#a1dbcd")
                result.set("Result: Errors in code")

        title = Message(root, font=("Comic Sans", 13),
                        text="Complete The Program\n so as to Find The Maximum\n Of the the three numbers:\n\n Example:\n\n""Input: 3\n5\n6\n\n Output:6 ",
                        fg="blue", bg="#a1dbcd")
        title.place(x=180, y=130)

        code1 = Message(root,
                        text="\n#include <iostream> \nusing namespace std; \n\nint max3(int x, int y, int z) {\n    "
                             "if(x >= y) { \n        if(x >= z) {  \n            return x; \n ", fg="black",
                        justify="left", bg="#a1dbcd")
        code1.place(x=450, y=100)

        code2 = Message(root,
                        text="} \n\nint main() {\n    int x, y, z;\n    cin >> x;\n    cin >> y;\n    cin >> z;\n    "
                             "cout << max3(x, y, z) << endl;\n    return 0;\n}", justify="left", bg="#a1dbcd")
        code2.place(x=450, y=380)

        submit = Button(root, text="Submit", bg="white", font="bold", command=exect)
        submit.place(x=550, y=550)

        error_head = Label(root, text="Errors:", fg="red", font="bold", bg="#a1dbcd")
        error_head.place(x=850, y=70)

        def second_problem():

            root.title('Second Problem')

            # clearing first problem
            resultLabel.destroy()
            errorMsg.destroy()
            title.destroy()
            Editor.destroy()
            code1.destroy()
            code2.destroy()
            submit.destroy()
            error_head.destroy()
            next1.destroy()

            # start second problem
            result2 = StringVar()
            resultLabel2 = Label(root, textvariable=result2, font=('roman', 12, 'bold'),bg="#a1dbcd")
            resultLabel2.place(x=400, y=630)

            title2 = Message(root, font="bold",
                             text="The Following Code Finds whether the given two digits number is divisible by "
                                  "both of it's Digits. \nThe code will return 1 if the number is divisible by both"
                                  " of it's digits and will return 0 otherwise.",
                             bg="#a1dbcd")
            title2.place(x=180, y=70)

            constraint = Message(root, font="italic",
                                 text="Input Range: x is an input where 11<=x<=100 \n x is strictly integer",
                                 bg="#a1dbcd")
            constraint.place(x=180, y=250)

            example = Message(root, fg="brown",
                              text="e.g.:\nLet's say x=12\nNow, 12 consists of digits 1 and 2. 12 is divisible by "
                                   "1 as well as 2 so it will return 1 for 12.\nWhereas for x=75, it's not true "
                                   "since 75 is not divisible by 7.", justify="left", bg="#a1dbcd")
            example.place(x=180, y=350)

            statement = Message(root,
                                text="Observe the following code and Write the smallest test case for this problem which would"
                                     " not give required results for the following code.", bg="#a1dbcd")
            statement.place(x=180, y=500)

            code = Label(root, bg="#a1dbcd", font="bold", justify="left",
                         text="int check(int n) {\n    int m = n; \n    int digit; \n    "
                              "int count = 0; \n    while(m > 0) { \n        digit = m % 10; "
                              "\n        m = m / 10;\n        if(n % digit == 0) {\n            "
                              "count++;\n        }\n    }\n    if(count >= 2) {\n        "
                              "return 1;\n    } else {\n        return 0;\n    }\n}\n")
            code.place(x=500, y=90)

            getinput = Label(root, font="bold", fg="brown", text="Enter Your value: ", bg="#a1dbcd")
            getinput.place(x=500, y=500)

            e = Text(root, width=10, height=1)
            e.place(x=500, y=530)

            # exect for second problem
            def exect2():
                entry = e.get("1.0", "end-1c")
                f = open('output.txt', 'w')
                f.write(entry)
                f.close()

                f = open('output.txt', 'r')
                val = 0
                try:
                    val = int(f.read())
                except:
                    pass

                if val % 10 == 0 and 10 < val <= 100:  # Make changes here when integrating
                    run.destroy()
                    point()
                    resultLabel2.config(fg='green', bg="#a1dbcd")
                    result2.set('Result: Correct answer')

                else:
                    point_minus()
                    resultLabel2.config(fg='red', bg="#a1dbcd")
                    result2.set('Result: Incorrect answer')

            run = Button(root, width=10, fg="red", text="RUN", command=exect2)
            run.place(x=580, y=525)

            def third_problem():

                root.title('Third Problem')

                # clearing second problem
                resultLabel2.destroy()
                title2.destroy()
                constraint.destroy()
                example.destroy()
                statement.destroy()
                code.destroy()
                getinput.destroy()
                e.destroy()
                run.destroy()
                next2.destroy()

                # start third problem
                result3 = StringVar()
                resultLabel3 = Label(root, textvariable=result3, font=('roman', 12, 'bold'),bg="#a1dbcd")
                resultLabel3.place(x=500, y=580)

                global first, second, third

                first = Text(root, width=10, height=2)
                first.place(x=500, y=480)

                second = Text(root, width=10, height=2)
                second.place(x=600, y=480)

                third = Text(root, width=10, height=2)
                third.place(x=700, y=480)

                def exece():
                    val1 = 0
                    val2 = 0
                    val3 = 0
                    try:
                        val1 = int(first.get("1.0", "end-1c"))
                        val2 = int(second.get("1.0", "end-1c"))
                        val3 = int(third.get("1.0", "end-1c"))
                    except:
                        pass

                    if val1 > 0 and val2 > 0 and val3 > 0 and val1 == val3 != val2:
                        run3.destroy()
                        point()
                        resultLabel3.config(fg='green', bg="#a1dbcd")
                        result3.set('Result: Correct answer')
                    else:
                        point_minus()
                        resultLabel3.config(fg='red', bg="#a1dbcd")
                        result3.set('Result: Incorrect answer')

                title3 = Message(root, fg="blue", font="bold",
                                 text="The Following Code is expected to tell which type of triangle is "
                                      "formed.\n Let us know any such testcase where the code would not "
                                      "work", justify="center", bg="#a1dbcd")
                title3.place(x=180, y=150)

                question = Message(root, font="italic", justify="left",
                                   text="Question: For a triangle having sides a,b,c, the following "
                                        "function will return: \n3 if it's a equilateral triangle\n"
                                        "2 if it's a isosceles triangle \n1 if it's a Scalene triangle", bg="#a1dbcd")
                question.place(x=180, y=300)

                code3 = Message(root, justify="left", font=(None, 10), fg="blue",
                                text="int triangleType(int a, int b, int c) {\n    if(a != b && b != c)\n"
                                     "        return 1;\n    else if(a == b && a == c)\n        return 3;"
                                     "\n    else\n        return 2;\n}", bg="#a1dbcd")
                code3.place(x=500, y=200)

                order3 = Message(root, text="Enter values of a,b,c for which the code won't work", bg="#a1dbcd")
                order3.place(x=500, y=400)

                run3 = Button(root, text="Submit", command=exece)
                run3.place(x=600, y=550)

                def fourth_problem():

                    root.title('Fourth Problem')

                    # clearing third problem
                    resultLabel3.destroy()
                    first.destroy()
                    second.destroy()
                    third.destroy()
                    title3.destroy()
                    code3.destroy()
                    question.destroy()
                    order3.destroy()
                    run3.destroy()
                    next3.destroy()

                    # start fourth problem
                    result4 = StringVar()
                    resultLabel4 = Label(root, textvariable=result4, font=('arial', 12, 'bold'),bg="#a1dbcd")
                    resultLabel4.place(x=550, y=640)

                    errorText4 = StringVar()
                    errorMsg4 = Message(root, textvariable=errorText4, bg="#a1dbcd")
                    errorMsg4.place(x=800, y=130)

                    head = Message(root, bg="#a1dbcd", font="bold", fg="red", justify="center",
                                   text="This is a reverse Coding Question.\nContestants are expected to find the pattern and write the function so as to we get the output from the given input.")
                    head.place(x=180, y=100)

                    table = Message(root, fg="purple", font="italic",
                                    text="Input	|      Output\n	|\n10	|	385\n20	|	287\n0	|	0\n2	|	5",
                                    justify="left", bg="#a1dbcd")
                    table.place(x=180, y=280)

                    code1 = Message(root,
                                    text="#include <iostream>\n\nusing namespace std;\nint pattern(int n) {\n    //Enter your Code",
                                    justify="left", font=('arial', 10, 'italic'), bg="#a1dbcd")
                    code1.place(x=450, y=150)

                    inp = Text(root, height=12, width=45)
                    inp.place(x=450, y=250)

                    code2 = Message(root, bg="#a1dbcd", font=('arial', 10, 'italic'),
                                    text="}\nint main()\n{\n    int x,y;\n    cin>>x;\n    y=pattern(x);\n    cout<<y;\n}\n",
                                    justify="left")
                    code2.place(x=450, y=450)

                    def exect4():
                        with open("part4.1.cpp") as f:  # Take the first part of the code from source
                            with open("runfile.cpp", 'w') as f1:
                                for line in f:
                                    f1.write(line)
                        f.close()
                        f1.close()
                        entry = inp.get("1.0", "end-1c")
                        second = open("runfile.cpp", 'a')
                        second.write(entry)
                        second.close()

                        with open("part4.3.cpp") as f:  # third part from source2
                            with open("runfile.cpp", 'a') as f1:
                                for line in f:
                                    f1.write(line)
                        f.close()
                        f1.close()

                        with open('errorfile', 'w') as infile:  # If Errors found,Written in INFILE
                            t1 = subprocess.call(["g++", "runfile.cpp"], stderr=infile)

                        if t1 == 0:  # THE CONDITION THAT TELLS THAT IT's Compiled fine and get be executed
                            with open('output', 'w') as outfile:  # Output Written on outfile
                                # subprocess.call(["./a.out"],stdout=outfile)
                                subprocess.call(["./a.out", "0", "20", "7"], stdout=outfile)

                            succ1 = open('output', 'r')
                            answer = succ1.read()
                            if answer == '02870140':
                                point()
                                submit4.destroy()
                                resultLabel4.config(fg='green', bg="#a1dbcd")
                                result4.set("Result: Correct answer")
                                errorText4.set("")
                            else:
                                point_minus()
                                resultLabel4.config(fg='red', bg="#a1dbcd")
                                result4.set("Result: Incorrect answer")
                                errorText4.set("")

                        else:
                            point_minus()
                            err4 = open('errorfile', 'r')
                            prob = err4.read()
                            errorText4.set(prob)
                            resultLabel4.config(fg='red', bg="#a1dbcd")
                            result4.set("Result: Errors in code")

                    submit4 = Button(root, text="Submit", bg="white", font="bold", command=exect4)
                    submit4.place(x=540, y=590)

                    error_head4 = Label(root, text="Errors:", fg="red", font="bold", bg="#a1dbcd")
                    error_head4.place(x=900, y=80)

                    def fifth_problem():

                        root.title('Fifth Problem')

                        # clearing fourth problem
                        resultLabel4.destroy()
                        errorMsg4.destroy()
                        error_head4.destroy()
                        submit4.destroy()
                        head.destroy()
                        table.destroy()
                        code1.destroy()
                        code2.destroy()
                        inp.destroy()
                        next4.destroy()

                        # start fifth problem

                        result = StringVar()
                        resultLabel = Label(root, textvariable=result, font=('arial', 12, 'bold'),bg="#a1dbcd")
                        resultLabel.place(x=500, y=620)

                        errorText = StringVar()
                        errorMsg = Message(root, textvariable=errorText, bg="#a1dbcd")
                        errorMsg.place(x=890, y=150)

                        title = Message(root, font="bold",
                                      text="Complete The Program so as to get the following ouput for the input ",
                                      justify="center",bg="#a1dbcd")
                        title.place(x=180, y=150)
                        pattern = Message(root,font=('bold',15), text="Input	output\n23545	23632\n999	1001\n1234	1331\n",bg="#a1dbcd")
                        pattern.place(x=180, y=300)

                        code11 = Message(root,
                                        text="#include<iostream>\nusing namespace std;\nint pattern(int n)\n{\n//code ",
                                        fg="blue", justify="left",bg="#a1dbcd")
                        code11.place(x=500, y=150)

                        Editor = Text(root, width=35, height=10)
                        Editor.place(x=500, y=250)

                        error_head = Label(root, text="Errors:", fg="red", font="bold",bg="#a1dbcd")
                        error_head.place(x=900, y=100)

                        code22 = Message(root, text="}\nint main()\n{\n int k,l;\n cin>>k;\n l=pattern(k);\n cout<<l;\n }",
                                         fg="blue", justify="left",bg="#a1dbcd")
                        code22.place(x=500, y=410)

                        def exect5():
                            with open("source5.1.cpp") as f:  # Take the first part of the code from source
                                with open("runfile.cpp", 'w') as f1:
                                    for line in f:
                                        f1.write(line)
                            f.close()
                            f1.close()
                            entry = Editor.get("1.0", "end-1c")
                            second = open("runfile.cpp", 'a')
                            second.write(entry)
                            second.close()

                            with open("source5.2.cpp") as f:  # third part from source2
                                with open("runfile.cpp", 'a') as f1:
                                    for line in f:
                                        f1.write(line)
                            f.close()
                            f1.close()

                            with open('errorfile', 'w') as infile:  # If Errors found,Written in INFILE
                                t1 = subprocess.call(["g++", "runfile.cpp"], stderr=infile)
                            if (t1 == 0):  # THE CONDITION THAT TELLS THAT IT's Compiled fine and get be executed
                                with open('output', 'w') as outfile:  # Output Written on outfile
                                    # subprocess.call(["./a.out"],stdout=outfile)
                                    subprocess.call(["./a.out", "23545"], stdout=outfile)

                                succ1 = open('output', 'r')
                                cool = 0
                                try:
                                    cool = int(succ1.read())
                                except:
                                    pass

                                if (int(cool) == 23632):
                                    point()
                                    submit.destroy()
                                    resultLabel.config(fg='green', bg="#a1dbcd")
                                    result.set("Result: Correct answer")
                                    errorText.set("")
                                else:
                                    point_minus()
                                    resultLabel.config(fg='red', bg="#a1dbcd")
                                    result.set("Result: Incorrect answer")
                                    errorText.set("")
                            else:
                                point_minus()
                                err5 = open('errorfile', 'r')
                                prob = err5.read()
                                errorText.set(prob)
                                resultLabel.config(fg='red', bg="#a1dbcd")
                                result.set("Result: Errors in code")

                        submit = Button(root, text="submit", fg="red", bg="white", font="bold", command=exect5)
                        submit.place(x=550, y=540)

                        next5 = Button(root, text='Finish', font='bold', command=game_over)
                        next5.place(x=560, y=680)

                    next4 = Button(root, text='Next problem', font='bold', command=fifth_problem)
                    next4.place(x=530, y=680)

                next3 = Button(root, text='Next problem', font='bold', command=fourth_problem)
                next3.place(x=530, y=680)

            next2 = Button(root, text='Next problem', font='bold', command=third_problem)
            next2.place(x=530, y=680)

        next1 = Button(root, text='Next problem', font='bold', command=second_problem)
        next1.place(x=530, y=680)

        # timer will run for 45mins = 2700secs
        countdown(2700)

    start_button = Button(root, text='START', font='bold', command=first_problem)
    start_button.place(x=620, y=450)


root.title('Login page')
# code for login page below
# call function 'instructions_page' after successfull login
JAM=Label(root,text='Just A Minute',font=('bold',30),justify='center',bg="#a1dbcd")
JAM.place(x=550,y=220)
user=Label(root,text='Username:',bg="#a1dbcd",font=('bold',13))
user.place(x=580,y=310)
username=Entry(root)
username.place(x=580,y=330)
passw=Label(root,text='Password:',font=('bold',13),bg="#a1dbcd")
passw.place(x=580,y=350)
password=Entry(root,show='*')
password.place(x=580,y=370)

login_button = Button(root, text='LOGIN', font='bold', command=instructions_page)
login_button.place(x=620, y=450)


root.config(bg="#a1dbcd")

root.mainloop()
