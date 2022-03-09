

a = 1  # as 'a' is variable chosen by ous, we can change it any time we want to
print(type(a))  # knowing the TYPE is every important (sometimes we may use str instead of int)
print()  # without writing print it won't show and this can be use to add spaces in result(what we see)

if a > 555:
    print("colon(:) followed by indent is the basic form to run ANY function")
    print("indent is importance for being a part of functions")
    print("as 'a' is reserved word, it won't run until the function is true or the condition is satisfies")
    print(66, 88, 99)  # comma (,) adds the blank space by default

    if a == 6000:
        print("*** function in function is called nesting ***")
        print("it's false so its never gonna read it, python will skip or ignores it")
        if a > 7:
            pass  # null operation - when it's executed, nothing happens (a function that does nothing (yet))
        else:  # it's two way decision so either 'if' OR 'else' function will run and one of them is sure to run.
            print("else makes it two way decision")
            print("it's not compulsory to use it, 'if' function is false then else(no other chose)")
            print("it choose ONLY one not both, like this or that, you have only TWO options")

            print("this is also possible" if a > 7 else "not again")  # simpler way to use 'if' AND 'else' function
    elif a > 10:  # instead of using many if for same function we use elif (which is followed by if)
        print("elif is basically the combo of else and if, it's Always followed by 'if'")  # doesn't matter if you use else or not
        print("if, elif, else are conditional and ONLY one of them runs NOT more than one")
        print("you can use elif n number of times but remember it goes in order and once find 'True' ignore the rest")
        print("if you ignore 'Else' then loop may choose either one or None")


