'''This is a project to practice recursion using python.  Program is written
to display the precise sequence of peg to peg transfer for the tower of
Hanoi puzzle given a stack of n rings.
'''

#displays and formats each move
def display_solution_line(myHanoiSolution):
    for move in myHanoiSolution:
        print(move[0], '-->', move[1])

#determines the move based on the starting peg (s), the final peg(f), and the
#temporary peg (t)
def hanoi_solution(n, s, f, t):
    if n == 1:   #base case, move the single ring from the start to final peg
        return([(s, f)])
    else:  #recursion step, each tower n, requires you to first move n-1 pegs to temp peg (first call below)
           #then call base case to move largest ring to peg 3
            #then call function again to move n-1 rings to final peg.
        return(hanoi_solution(n - 1, s, t, f) + hanoi_solution(1, s, f, t) + hanoi_solution(n - 1, t, f, s))

#user inputs number of rings
n = int(input('Enter the starting number of rings: '))
print("Number of rings: ", n)
print()

myHanoiSolution = hanoi_solution(n, 1, 3, 2)

display_solution_line(myHanoiSolution)