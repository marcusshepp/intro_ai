using System;
using System.Collections.Generic;

namespace GAS
{
	class GA
	{

		static string [] possible_operators = {"+", "-", "/", "*"};
		static int GOAL = 10;

		static int[] initialize_population(int size){
			/* Create first population. */
			Random rand = new Random ();
			int[] population = new int[size];
			for (int i = 0; i < population.Length; i++) {
				int init_chrome = rand.Next (0, 1024);
				population [i] = init_chrome;
			}
			return population;
		}

		static string get_operator(int chrome){
			/* 0000 0000 11 */
			int the_num = chrome & 3;
			string op = possible_operators [the_num];
			return op;
		}

		static int get_first_number(int chrome){
			/* 0000 1111 00 */
			return (chrome & 60) >> 2;
		}

		static int get_second_number(int chrome){
			/* 1111 0000 00 */
			return (chrome & 960) >> 6;
		}

		static int get_second_half(int chrome){
			/* 11111 00000 */
			return (chrome & 992);
		}

		static int get_first_half(int chrome){
			/* 00000 11111 */
			return (chrome & 31);
		}

		static int decode(int chrome){
			/* decodes the chromosome and returns its functions result. */
			int first_number = get_first_number (chrome);
			string op = get_operator (chrome);
			int second_number = get_second_number (chrome);
			int value = new int();
			if (op == "+"){
				value = first_number + second_number;
			}
			else if (op == "-"){
				value = first_number - second_number;
			}
			else if (op == "*"){
				value = first_number * second_number;
			}
			else if (op == "/"){
				try{
					value = first_number / second_number;
				} catch (System.DivideByZeroException) {
					// ????
					value = 0;
				}
			}
			return value;
		}

		static bool is_solution(int chromosome){
			int goal = GOAL;
			int value = decode (chromosome);
			if (value == goal) {
				return true;
			} else {
				return false;
			}
		}

		static int fitness_score(int chrome) {
			/* evaluates the chromosomes and outputs their fitness score. */
			int goal = GOAL;
			int score = Math.Abs (goal - decode(chrome));
			return score;
		}

			/* select two chromosomes based on fitness score. 
			 * decode the chromosomes. the two parent chromos
			 * have a .5 chance of being crossed over at there
			 * center most digit. if they dont crossover their
			 * children will be exact copies.
			*/

		static int select_partner(int[] population){
			/* 
			 * select two random contestants 
			 * compare fitness.
			 * lower fitness (closer to 0)
			 * gets to breed.
			 * 
			*/ 
			Random rand = new Random ();
			int a = rand.Next (0, 100);
			int b = rand.Next (0, 100);
			// if a has a better fitness score
			if (fitness_score (population[a]) < fitness_score (population[b])) {
				return population [a];
			} else{
				/// if b has a better fitness score
				return population [b];
			}
		}

		static int[] crossover(int[] parents){
			/*
			 * in: parents;
			 * out: childone, childtwo;
			*/
			Random rand = new Random ();
			int choice = rand.Next (0, 100);
			int[] children = new int[2];
			if (choice > 50) {
				// crossover
				int male_first_half = get_first_half (parents [0]);
				int male_second_half = get_second_half (parents [0]);
				int female_first_half = get_first_half (parents [1]);
				int female_second_half = get_second_half (parents [1]);
				int child_one = male_first_half | female_second_half;
				int child_two = female_first_half | male_second_half;
				children [0] = child_one;
				children [1] = child_two;
			} else {
				children [0] = parents [0];
				children [1] = parents [1];
			}
			return children;
		}

		static int mutate(int chromosome){
			/* 
			 * mutate the given decimal
			 * by randomly choosing a bit
			 * and XOR it with its opposite.
			 * 0 xor 1 = 1
			 * 1 xor 1 = 0
			 */
			Random rand = new Random ();
			int bit_to_flip = rand.Next (0, 10);
			int mutated_chrome = chromosome ^ (1 << bit_to_flip);
			return mutated_chrome;
		}


		static void Main(string[] args)
		{	
			int population_size = 100;
			int[] population = initialize_population (population_size);
			int num_of_generations = 100;
		
			for (int generations = 0; generations <= num_of_generations; generations++) {
				List<int> new_pop = new List<int>();
				for (int x = 0; x < 100; x++) {
					int[] parents = new int[2];
					parents[0] = population [x];
					parents[1] = select_partner (population);
					int[] children = crossover(parents);
					int child_one = mutate (children [0]);
					int child_two = mutate (children [1]);
					// only add the child with the best fitness score
					// this way the population size remains the same
					if (fitness_score (child_one) < fitness_score (child_two)) {
						new_pop.Add (child_one);
					} else {
						new_pop.Add (child_two);
					}
				}
				for (int x = 0; x < 100; x++) {
					if (is_solution (new_pop [x])) {
						Console.WriteLine (new_pop[x]);
						Console.WriteLine (get_first_number(new_pop [x]));
						Console.WriteLine (get_operator(new_pop [x]));
						Console.WriteLine (get_second_number(new_pop [x]));
						Console.WriteLine ("=");
						Console.WriteLine (decode(new_pop [x]));
					} else {
						continue;
					}
				}
				int[] new_pop_list = new_pop.ToArray();
				population = new_pop_list;
			}
		}
	}
}