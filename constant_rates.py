import random
import sys

# assign arguments arrival rate, departure rate, and buffer size
arrival_rate = sys.argv[1]
departure_rate = sys.argv[2]
buffer_size = sys.argv[3]

def constant_rates():
    # Packet in queue and packet dropped
    pkt_in_q = 0
    pkt_dropped = 0

    # counter
    counter = 1
    # file will execute in the same folder
    file_name = "constant_rates.txt"
    

    with open(file_name, "w") as file:
        # this will run for the 1 million events.
        for _ in range(1000000):
                
            # generate random number from 0-1 
            y = random.random()
            #  probabilities 
            Parrival = float(arrival_rate) / (float(departure_rate) + float(arrival_rate))
            if y < Parrival:
                if pkt_in_q < int(sys.argv[3]):
                    pkt_in_q += 1
                else:
                    pkt_dropped += 1
            else:
                if pkt_in_q > 0:
                    pkt_in_q -= 1
            
            file.write(f"{int(counter)}\t{int(pkt_in_q)}\t{int(pkt_dropped)}\n")
            counter = counter + 1

    


constant_rates()