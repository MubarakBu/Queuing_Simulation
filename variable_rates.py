import random

def variable_rates():
    # Packet in queue and packet dropped
    pkt_in_q = 0
    pkt_dropped = 0

    # Buffer size
    buffer_size = 100

    # Departure rate
    departure_rate = 120.00

    # counter
    counter = 1

    # File name will excuted in the same floder
    file_name = "variable_rates.txt"


    with open(file_name, "w") as file:
        
        # number of event to simulate
        for i in range(1000000):
            
            #arrival and departure packet per second 
            arrival_rate = 0
            
            # generate random number from 0-1 
            y = random.random()

            # specify the percentage of each rate 
            if i <= 100000:
                arrival_rate = 70.00
            elif i >= 100001 and i <= 700000:
                arrival_rate = 200.00
            elif i >= 700001 and i <= 800000:
                arrival_rate = 130.00
            elif i >= 800001 and i <= 900000:
                arrival_rate = 120.00
            elif i >= 900001 and i <= 1000000:
                arrival_rate = 70.00

            #  probabilities arrival rate
            Parrival = arrival_rate / (departure_rate + arrival_rate)

            if y < Parrival:
                if pkt_in_q < buffer_size:
                    pkt_in_q += 1
                else:
                    pkt_dropped += 1
            else:
                if pkt_in_q > 0:
                    pkt_in_q -= 1
                    
            file.write(f"{int(counter)}\t{int(pkt_in_q)}\t{int(pkt_dropped)}\n")
            counter = counter + 1

variable_rates()