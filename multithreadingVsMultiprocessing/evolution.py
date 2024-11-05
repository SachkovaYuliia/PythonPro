# Задача 6: моделювання еволюції в паралельних середовищах
# Створіть симуляцію еволюції популяції організмів, де кожен організм обробляється окремо в різних процесах або потоках. Популяція повинна змінюватися залежно від певних параметрів (наприклад, харчування, розмноження тощо).

import random
from concurrent.futures import ProcessPoolExecutor
import time

POPULATION_SIZE = 100     
ENERGY_GAIN = 10             
ENERGY_COST = 5              
REPRODUCTION_ENERGY = 20     
MAX_AGE = 10                 


class Organism:
    def __init__(self, energy=10):
        self.energy = energy
        self.age = 0
        self.alive = True


    def update(self):
        """
        Функція оновлення стану організму
        """
        if not self.alive:
            return None

        self.energy += ENERGY_GAIN * random.random()
        
        self.energy -= ENERGY_COST
        self.age += 1
        
        if self.energy <= 0 or self.age > MAX_AGE:
            self.alive = False
            return None

        if self.energy >= REPRODUCTION_ENERGY:
            self.energy /= 2  
            return Organism(energy=self.energy)
        
        return None


def simulate_organism(organism):
    """
    Функція для моделювання еволюції одного організму в окремому процесі
    """
    offspring = organism.update()
    return organism, offspring


def run_simulation():
    """
    Основна функція для запуску симуляції
    """
    population = [Organism(energy=random.randint(5, 15)) for _ in range(POPULATION_SIZE)]

    generation = 0
    while population:
        print(f"\n Покоління {generation}: Популяція {len(population)}")
        
        with ProcessPoolExecutor() as executor:
            results = list(executor.map(simulate_organism, population))


        new_population = []
        for organism, offspring in results:
            if organism.alive:
                new_population.append(organism)
            if offspring:
                new_population.append(offspring)
        
        population = new_population
        generation += 1
        time.sleep(1)  

if __name__ == "__main__":
    run_simulation()
