import numpy as np

KIDS = 12
GROUPS = 3
DAYS = 6

def score(count, groups):
    score = 0
    for group in groups:
        if (len(group) == 1):
            score += count[group[0], group[0]]**2
            continue

        for i in range(len(group) - 1):
            for j in range(i + 1, len(group)):
                score += count[group[i], group[j]]**2

    return score

def get_groups(assignment):
    groups = [[] for _ in range(GROUPS)]

    for i, group in enumerate(assignment):
        groups[group].append(i)

    return groups

def swap(assignment, i, j):
    new_assignment = np.array(assignment)
    new_assignment[i] = assignment[j]
    new_assignment[j] = assignment[i]
    return new_assignment

def update_count(count, groups):
    for group in groups:
        if (len(group) == 1):
            count[group[0], group[0]] += 1

        for i in range(len(group) - 1):
            for j in range(i + 1, len(group)):
                count[group[i], group[j]] += 1
                count[group[j], group[i]] += 1
    

if __name__ == '__main__':
    # An entry at (i,j) is the number of times the kid i was in the same group as the kid j.
    # An entry on the main diagonal at (i,i) is the number of times the kid i was alone in a one-person-group.
    count = np.zeros((KIDS, KIDS), dtype=np.int)

    for day in range(DAYS): 
        # At the index i is the index of the group assigned to the kid i.
        assignment = np.array([int(i / KIDS * GROUPS) for i in range(KIDS)])

        while True:
            current_score = score(count, get_groups(assignment))

            old_current_score = current_score

            for i in range(KIDS):
                for j in range(i, KIDS):
                    if (assignment[i] != assignment[j]):
                        new_assignment = swap(assignment, i, j)
                        new_score = score(count, get_groups(new_assignment))
                        if (new_score < current_score):
                            assignment = new_assignment
                            current_score = new_score

            if old_current_score == current_score:
                break


        update_count(count, get_groups(assignment))

        print(f'Day {day + 1}:')
        print(get_groups(assignment))
        print(count)
        print()


            

    # for kids in range(KIDS):

