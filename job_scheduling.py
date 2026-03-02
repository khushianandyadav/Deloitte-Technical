def print_job_scheduling(arr, n):
    # Step 1: sort jobs by profit in descending order
    arr.sort(key=lambda x: x[2], reverse=True)

    # Step 2: find maximum deadline
    max_deadline = max(job[1] for job in arr)

    # Step 3: create slots for deadlines
    slots = [-1] * max_deadline
    result = [''] * max_deadline

    total_profit = 0

    # Step 4: assign jobs to slots
    for job in arr:
        job_id, deadline, profit = job

        # find a free slot from deadline-1 backwards
        for j in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[j] == -1:
                slots[j] = job_id
                result[j] = job_id
                total_profit += profit
                break

    # Step 5: print result
    print("Scheduled Jobs:", end=" ")
    for job in result:
        if job != '':
            print(job, end=" ")
    print("\nTotal Profit:", total_profit)


def main():
    # job_id, deadline, profit
    arr = [
        ('a', 2, 100),
        ('b', 1, 19),
        ('c', 2, 27),
        ('d', 1, 25),
        ('e', 3, 15)
    ]

    n = len(arr)
    print_job_scheduling(arr, n)


if __name__ == "__main__":
    main()
