using System;

namespace Application
{
	class rocketga
	{
		/* 
		 * population size should be 5 
		 * if 5 then that will give us 36 
		 * generations
		 */
		static int[] init_population(int size){
			Random rand = new Random ();
			int[] population = new int[size];
			for (int i = 0; i < population.Length; i++) {
				int init_chrome = rand.Next (0, 32767);
				population [i] = init_chrome;
			}
			return population;
		}
		static string[] decode(int chromosome){
			/* 000 000 000 000 111 */
			int first_direction = (chromosome & 7);
			/* 000 000 000 111 000 */
			int second_direction = (chromosome & 56 >> 3);
			/* 000 000 111 000 000 */
			int third_direction = (chromosome & 448 >> 6);
			/* 000 111 000 000 000 */
			int fourth_direction = (chromosome & 3584 >> 9);
			/* 111 000 000 000 000 */
			int fifth_direction = (chromosome & 28672 >> 12);
			string[] possible_moves = {"N", "S", "E", "W", "NE", "NW", "SE", "SW"};
			string[] move_sequence = new string[8];
			move_sequence [0] = possible_moves [first_direction];
			move_sequence [1] = possible_moves [second_direction];
			move_sequence [2] = possible_moves [third_direction];
			move_sequence [3] = possible_moves [fourth_direction];
			move_sequence [4] = possible_moves [fifth_direction];
			return move_sequence;
		}
		static int fitness_score(int chrome) {
			// this is where car makes its moves
			// execute move sequence
			// if ball touched return 10 else 0
			// (take into consideration the distance from ball?)
			return score;
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
		static void Main(){
			/* init pop
			 * new_pop = []
			 * scores = []
 			 * for p in pop do
			 *     fitness = fitness_score(decode(p)) # run move sequence
			 *     scores.append(fitness)
			 * for i whichis 0 - 4 do
			 *     first_best = max(scores) # index with best score
			 *     second_best = second_best(scores) # index with second best score
			 *     third_best = third_best(scores) # index with third best score
			 *     fourth_best = fourth_best(scores) # index with fourth best score
			 *     worst_score = min(scores) # index with worst score
			 * 	   parents1 = [first_best, second_best]
			 *     new_pop.append(mutate(crossover(parents1)))
			 *     parents2 = [third_best, fourth_best]
			 *     new_pop.append(mutate(crossover(parents2)))
			 *     new_pop.append(mutate(first_best))
			 * pop = new_pop
			 * repeat 36 times
			 */
		}

	}
}

