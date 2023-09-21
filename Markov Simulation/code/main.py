from classes.supermarket import Supermarket
import pandas as pd

tp = pd.read_csv(
    "../data/tp.csv", sep=";")
tp.set_index("Before", inplace=True)


def supermarket_sim(number_of_iter: int, supermarket_name: str, transition_prob: pd.DataFrame) -> None:
    s = Supermarket(supermarket_name, transition_prob)
    
    s.add_new_customers()
    s.add_new_customers()

    #print(s, "\n")
    
    for i in range(number_of_iter):
        #if i % 10 == 0:
        #    print(s)
        s.print_customers()
        
        s.remove_churned_customers()
    
        s.next_minute()


if __name__ == "__main__":
    supermarket_sim(900, "Rewe", tp)
