using System;
using System.Collections.Generic;

namespace GAS
{
	class GA
	{

		/* Path to Int.
		 *
		 * My first take on genetic algorithms.
		 * Inspiration and idea for problem space
		 * came from (http://www.ai-junkie.com/ga/intro/gat1.html).
		 *
		 * Summary:
		 * Finds a path to integer `GOAL` ranging from 0 - 81.
		 * Using  the following tools:
		 *     - x = 0 - 9
		 *     - y = 0 - 9
		 *     - i = `possible operators`
		 *
		 *
		 */

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

		/* Encoding
		 *
		 * The following are methods that perform
		 * Bit Masking and Bit Shifting.
		 * extracting the problem from bits
		 * creates a way for the computer to
		 * find a solution faster.
		*/

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

		/*
		 * Decoding
		*/

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
			/* :returns: true if is solution
			 *           else false
			*/
			int goal = GOAL;
			int value = decode (chromosome);
			if (value == goal) {
				return true;
			} else {
				return false;
			}
		}

		static int fitness_score(int chrome) {
			/* evaluates a chromosome and outputs its fitness score.
			 * highly dependant on GOAL
			*/
			int goal = GOAL;
			int score = Math.Abs (goal - decode(chrome));
			return score;
		}

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
			 * in: parents[2];
			 * out: children[2];
			 */
			Random rand = new Random ();
			int choice = rand.Next (0, 100);
			int[] children = new int[2];
			if (choice > 50) {
				/* crossover
				 * p0 = 0000011111
				 * p1 = 1111100000
				 * c0 = 1111111111
				 * c1 = 0000000000
				 */
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
			 * and XOR it with a one.
			 * 0 xor 1 = 1
			 * 1 xor 1 = 0
			 *
			 * *note*
			 * must shift bit to desired allel
			 *
			 */
			Random rand = new Random ();
			int bit_to_flip = rand.Next (0, 10);
			int mutated_chrome = chromosome ^ (1 << bit_to_flip);
			return mutated_chrome;
		}


		static void Main(string[] args)
		{	/* def PATHTOINT ( GOAL ) do
		     *     initialize pop whichis population
		     *     int generations
		     *     for (gen whichis 0 to generations) do
		     *         new_pop = []
		     *         if is_empty(pop) do
		     *             pop = new_pop
		     *         for (pop_index whichis 0 to pop.length) do
		     *             if is_solution(pop[pop_index]) do
		     *                 return pop[pop_index]
		     *             parents = [pop[pop_index], select_partner(pop)]
		     * 			   children = [mutate(crossover(parents))]
		     * 		       child = best(children)
		     * 			   new_pop.append(child)
		     *		   	   pop.remove(pop_index)
		     *     return best_answer(pop)
		     */
			int population_size = 100;
			int[] population = initialize_population (population_size);
			int num_of_generations = 100;

			for (int generations = 0; generations <= num_of_generations; generations++) {
				List<int> new_pop = new List<int>();
				for (int x = 0; x < 100; x++) {

					// select parents
					int[] parents = new int[2];
					parents[0] = population [x];
					parents[1] = select_partner (population);

					// crossover parents into children
					int[] children = crossover(parents);

					// mutate children
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
