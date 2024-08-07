from itertools import count as c

customers1 = [[5, 2], [5, 4], [10, 3], [20, 1]] # [[arriving_time, time_required], ...]
customers2 = [[3, 4], [4, 9], [11, 6], [13, 7]] # [[arriving_time, time_required], ...]
customers = customers1 + customers2 # [[arriving_time, time_required], ...]

customers.sort(key=lambda customer: customer[0]) # sorting customers based on customer[arriving_time]
print(customers)

arrivedCustomers = [] # [[arriving_time, time_required, current_waiting_time], ...]
leftCustomers = [] # [[arriving_time, time_required, total_waiting_time], ...]

for t in c(start=customers[0][0]):
    for customer in customers: # for all customers
        if customer[0] == t: # if customer[arriving_time] = t then
            arrivedCustomers.append(customer + [0]) # add that customer to arrivedCustomers
    if arrivedCustomers: # if a customer is present in arrived customers then
        arrivedCustomers[0][1] -= 1 # for 1st customer in arrivedCustomers decrease the time_required by 1
    for customer in arrivedCustomers: # for all customer in arrivedCustomers
        customer[2] += 1 # increase the customer[current_waiting_time] by 1
    if arrivedCustomers: # if a customer is present in arrivedCustomers then
        if not arrivedCustomers[0][1]: # if 1st customer of arrivedCustomers required_time = 0 then
            leftCustomers.append(arrivedCustomers[0]) # add the 1st customer to leftCustomers
            arrivedCustomers.pop(0) # remove the first cumtomer from arrivedCustomers
    if len(customers) == len(leftCustomers): # if length of customers = length of leftCustomers then
        break # get out of the loop

print(f"Final Left Customers: {leftCustomers}") # leftCustomers => [[arriving_time, time_required, total_waiting_time], ...]

totalWaitingTime = 0 # to calculate totalWaitingTime

for customer in leftCustomers: # for all customer in leftCustomers
    totalWaitingTime += customer[2]  # add final_waiting_time to totalWaitingTime

print(f"Total waiting time: {totalWaitingTime}")

avgWaitingTime = totalWaitingTime/len(customers) # calculating average waiting time

print(avgWaitingTime)