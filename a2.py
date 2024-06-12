""" Write a program where 10 members will form a circle, the first person will kill the next person and then the next existing person wull kill the person next to it
The last peron remain will be the winner"""

def josephus(n,k):

    """This function returns the position of the last member left standing after eliminating every k-th person in a circle of n members
    
    :param n: The number of people in the circle
    :param k: The step rate (every k-th person will be eliminated)
    :return: The position of the last person left standing"""

    #List Comprehension
    person = [(x+1) for x in range(1,n+1)] #or person = list(range(1,n+1))

    index = 0

    while len(person)>1:

        index = (index + k - 1) % len(person)
        eliminated = person.pop(index)
        print(f"Eliminated: {eliminated}")
    
    return person[0]

winner = josephus(10,1)

print(f"The is winner is standing at the position: {winner}")


