/*
		 * Goal is to find a pattern
		 * of moves that corrdinate
		 * a constant scoring and/or
		 * touching the ball.
		 *
		 * Sequence of moves lasts 2.5 seconds.
		 * with this I can get 36 generations
		 * of patterns. I know the best technique isn't
         * to start from scratch every game but I
         * still wanted to try.
		 */
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System;

public class AdamsCarController : CarController {
	static float hor;
	static float vert;
	static bool start = true;
	static bool chrome_start = true;
	static bool chrome_end = false;
	static bool gen_start = true;
	static bool gen_end = false;
	static int generation = 0;
	static string current_direction;
	static int resulting_team_score;
	static int origin_team_score;
	static int chromosome_index;
	static int move_index;
	static int fit_index;
	static int[] population = new int[5];
	static int[] new_population = new int[5];
	static float[] fitness_scores = new float[5];
	static string[] current_chromosome_sequence = new string[5];

	// Use this for initialization
	void Start () {
		playerName = "Adams";
		Init ();
		StartCoroutine(UpdateControls());
	}

	static void move(string cmd) {
		/*
		 * Controller
		 * updates hor and vert
		 * which is the direction the car is facing.
		 */
		if (cmd == "N"){
			hor = 0f;
			vert = 1f;
		}else if (cmd == "NE"){
			hor = 1f;
			vert = 1f;
		}else if (cmd == "NW"){
			hor = -1f;
			vert = 1f;
		}else if (cmd == "S"){
			hor = 0f;
			vert = -1f;
		}else if (cmd == "SW"){
			hor = -1f;
			vert = -1f;
		}else if (cmd == "SE"){
			hor = 1f;
			vert = 1f;
		}else if (cmd == "W"){
			hor = -1f;
			vert = 0f;
		}else if (cmd == "E"){
			hor = 1f;
			vert = 0f;
		}
	}

	/*
	 * population size should be 5
	 * if 5 then that will give us 36
	 * generations
	 */
	static int[] init_population(int size){
		System.Random rand = new System.Random ();
		int[] population = new int[size];
		for (int i = 0; i < population.Length; i++) {
			int init_chrome = rand.Next (12, 32767);
            Debug.Log("init chrome " + init_chrome);
            Debug.Log("init chrome " + (init_chrome & 28672 >> 12));
			population [i] = init_chrome;
		}
		return population;
	}

	static string[] decode(int chromosome){


		/*
		 * in: chromosome
		 * out: move sequense[0...4;
		 *
		 *      |
		 *   \     /
		 *  -       -
		 *   /  |  \
		 */
		/* 000 000 000 000 111 */
		int first_direction = (chromosome & 7);

		/* 000 000 000 111 000 */
		int second_direction = (chromosome & 56 >> 3);
        Debug.Log("first_direction " + first_direction + " second_direction " + second_direction);
		/* 000 000 111 000 000 */
		int third_direction = (chromosome & 448 >> 6);
        Debug.Log("third_direction " + third_direction);
		/* 000 111 000 000 000 */
		int fourth_direction = (chromosome & 3584 >> 9);
        Debug.Log("fourth_direction " + fourth_direction);
		/* 111 000 000 000 000 */
		int fifth_direction = (chromosome & 28672 >> 12);
        Debug.Log("fifth_direction " + fifth_direction);
		string[] possible_moves = {"N", "S", "E", "W", "NE", "NW", "SE", "SW"};
		string[] move_sequence = new string[5];
		move_sequence [0] = possible_moves [first_direction];
		move_sequence [1] = possible_moves [second_direction];
		move_sequence [2] = possible_moves [third_direction];
		move_sequence [3] = possible_moves [fourth_direction];
		move_sequence [4] = possible_moves [fifth_direction];
		return move_sequence;
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
		System.Random rand = new System.Random ();
		int bit_to_flip_one = rand.Next (0, 14);
		int bit_to_flip_two = rand.Next (0, 14);
		int mutated_chrome = chromosome ^ (1 << bit_to_flip_one);
		mutated_chrome = chromosome ^ (1 << bit_to_flip_two);
		return mutated_chrome;
	}

	static int[] crossover(int parent_one, int parent_two){
		    /*
			 * in: parents[2];
			 * out: children[2];
			 */
		System.Random rand = new System.Random ();
		int choice = rand.Next (0, 100);
		int[] children = new int[2];
		if (choice > 50) {
			/* crossover
				 * p0 = 000000001111111
				 * p1 = 111111110000000
				 * c0 = 111111111111111
				 * c1 = 000000000000000
				 */
			int male_first_half = (parent_one & 127);
			int male_second_half = (parent_one & 32640);
			int female_first_half = (parent_two & 127);
			int female_second_half = (parent_two & 32640);
			int child_one = (male_first_half | female_second_half);
			int child_two = (female_first_half | male_second_half);
			children [0] = child_one;
			children [1] = child_two;
		} else {
			children [0] = parent_one;
			children [1] = parent_one;
		}
		return children;
	}

	static float fitness_score(float origindfb, float resultingdfb, float origints, float resultingts) {
		// distance traveled toward ball - difference in score
		float score;
		float d = origindfb - resultingdfb;
		float s = origints - resultingts;
		score = d - s;
		return score;
	}

	static int[] create_new_population(int[] pop, float[] fitness_scores){
		int[] children = new int[2];
		for (int i = 0; i < 5; i++){
			if (i < 3 && fitness_scores[i + 1] > fitness_scores[i + 2]){
				int[] crossed_parents = crossover(population[i + 1], population[i]);
				children[0] = mutate (crossed_parents[0]);
				children[1] = mutate (crossed_parents[1]);
				new_population[i] = children[0];
				new_population[i + 1] = children[1];
			} else if(i < 3 &&  fitness_scores[i + 1] < fitness_scores[i + 2]){
				int[] crossed_parents = crossover(population[i + 2], population[i]);
				children[0] = mutate (crossed_parents[0]);
				children[1] = mutate (crossed_parents[1]);
				new_population[i] = children[0];
				new_population[i + 1] = children[1];
			}
            if(i == 4){
				if(fitness_scores[0] > fitness_scores[1]){
					int[] crossed_parents = crossover(population[0], population[i]);
					children[0] = mutate (crossed_parents[0]);
					children[1] = mutate (crossed_parents[1]);
					new_population[i] = children[0];
				}else if(fitness_scores[0] < fitness_scores[1]){
					int[] crossed_parents = crossover(population[1], population[i]);
					children[0] = mutate (crossed_parents[0]);
					children[1] = mutate (crossed_parents[1]);
					new_population[i] = children[0];
				}
			}
		}
		return new_population;
	}
	static void update_move_sequence(int chromosome){
		string[] sequence = decode (chromosome);
		for (int i = 0; i < 5; i++){
			current_chromosome_sequence[i] = sequence[i];
		}
	}
	IEnumerator UpdateControls(){
		// init pop
		int[] origin_population = init_population (5);
		update_move_sequence(origin_population[chromosome_index]);
		start = false;
		// record initial values
		Vector3 my_resulting_vector = controller.transform.position;
		Vector3 my_origin_vector = controller.transform.position;
		float origin_distance_from_ball = Vector3.Distance (
			ball.transform.position, my_origin_vector);

		// set indexes to zero
		chromosome_index = 0;
		fit_index = 0;
		move_index = 0;

		while (1==1){
			Debug.Log ("chrome_start "+chrome_start);
			Debug.Log ("chromosome_index "+chromosome_index);
			Debug.Log ("fit_index "+fit_index);
			Debug.Log ("move_index "+move_index);
			if(chromosome_index == 0) {
				// get dist from ball
				origin_distance_from_ball = Vector3.Distance (
					ball.transform.position, my_origin_vector);
				// renew sequence
				string[] sequence = decode (new_population[chromosome_index]);
				for (int i = 0; i < 5; i++){
					current_chromosome_sequence[i] = sequence[i];
				}
			}
			Debug.Log(current_chromosome_sequence);
			current_direction = current_chromosome_sequence[move_index];
			if (move_index != 4){
				move_index += 1;
			} else {
				move_index = 0;
			}
			Debug.Log(current_direction);

			move (current_direction);
			controller.horizontalSetting = hor;
			controller.verticalSetting = vert;
			yield return new WaitForSeconds(.5f);
			float resulting_distance_from_ball = Vector3.Distance (
				ball.transform.position, my_resulting_vector);
			Debug.Log(new_population.Length);
			if(fit_index == 4){
				// new gen
				population = create_new_population(population, fitness_scores);
				fit_index = 0;
			} else if (chromosome_index == 4){
				fitness_scores[fit_index] = fitness_score(
					origin_distance_from_ball, resulting_distance_from_ball, origin_team_score, resulting_team_score);
				chrome_start = true;
				chromosome_index = 0;
			} else {
				chrome_end = false;
				chrome_start = false;
				chromosome_index += 1;
			}
            fit_index += 1;
		}
	}
}
