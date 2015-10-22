using UnityEngine;
using System.Collections;

public class JonesCarController : CarController {
	int vDirection = 1;
	float hDirection = 1;
	float direction = -1;
	// Use this for initialization
	void Start () {
		playerName = "Jones";
		Init ();
		StartCoroutine(UpdateControls());
	}

	/* Controller */
	public void control(float hor, float vert) {
		this.controller.horizontalSetting = hor;
		this.controller.verticalSetting = vert;
	}

	IEnumerator UpdateControls(){
		while (1==1){
			yield return new WaitForSeconds(1f);
			//Vector3 ballPos = ball.transform.position;
			//if (ballPos.z < transform.position.z){

			float a = UnityEngine.Random.Range(-1.0f, 1.0f);
			float b = UnityEngine.Random.Range(-1.0f, 1.0f);


			control (a, b);


		}

	}

}
