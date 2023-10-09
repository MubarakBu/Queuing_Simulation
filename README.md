# 1- Constant Rates Simulation
This Python code simulates a simple packet arrival and departure process with constant rates and a limited buffer size. The simulation records the number of packets in the queue and the number of packets dropped due to buffer overflow over a series of events.

## Steps to Run the Code:

- Install Python on your machain
- Open a termianl or command prompt.
- Navigate to the directory where the "constant_rate.py" file is located.
- Run the script with the following command:
```
python constant.py <arrival_rate> <departure_rate> <buffer_size> 
```

` Replace <arrival_rate>, <departure_rate>, and <buffer_size> with the desired values for your simulation.
`
The script will execute the simulation for a specified number of events and save the results to a file named constant_rates.txt in the same directory.
----
# 2- Variable Rates Simulation
This Python code simulates a simple packet arrival and departure process with variable rates of arrival. The simulation records the number of packets in the queue and the number of packets dropped due to buffer overflow over a series of events. The arrival rates are customized to change based on specific event percentiles.

## Steps to Run the Code:

- Install Python on your machain
- Open a termianl or command prompt.
- Navigate to the directory where the "variable_rate.py" file is located.
- Run the script with the following command:
```
python variable_rates.py  
```

The script will execute the simulation for a specified number of events and save the results to a file named constant_rates.txt in the same directory.

### - Simulation Logic
- The first 10 percent of events have an arrival rate of 70.
- The next 60 percent of events have an arrival rate of 200.
- The next 10 percent of events have an arrival rate of 130.
- The next 10 percent of events have an arrival rate of 120.
- The remaining events have an arrival rate of 70.r