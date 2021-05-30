

b = 2
while b > 1000:  # runs ONLY if it's TRUE
    # it's called While Loop as it loops until it gets a false
    # working: check the condition(if true) run the code then go back to top to check the condition again and continue
    # sometimes you might not know how many times it will loop(run) through it (maybe finite or infinite)
    # it like 'if' function but as long as it gets true it continues
    if b > 555:
        pass  # it's a null operation(when it is executed, nothing happens), a function that does nothing (yet)
    elif b > 444:
        break  # break is to stop and get out of ANY function
    elif b > 777:
        continue  # continue is to start again ANY function

    for i in range(b):  # as it loop(runs) to a finite value(which is given by coder) it's called FOR Loop
        # for i(iterator) in X(iterable) -> here iterable = which can be loop through(like list,dic,tuple,array)
        # iteration variables - which change each time as they go through the loop(iteration - repetition of process)
        # working: check the condition run the code then go back to top to check the condition again and continue
        # for example: for i in range(3) == i going through each value of [0, 1, 2] == i will 0, 1 and 2
        # range(n, m) = starting from n and ending at (m-1) => [n, n+1,......, m-1]......type => range class
        # [range(n, m)] = a list from n to (m-1) terms .......type => list
        pass

print("Done")

