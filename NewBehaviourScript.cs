using UnityEngine;
using System.Collections;

public class NewBehaviourScript : MonoBehaviour {

	// Use this for initialization
	void Start () {
		Debug.Log("This GameObject's name is: " + gameObject.name);
	
	}
	
	public float moveSpeed = 10f;
	public float turnSpeed = 50f;


	void Update ()
	{
		if(Input.GetKey(KeyCode.UpArrow))
			transform.Translate(Vector3.forward * moveSpeed * Time.deltaTime);

		if(Input.GetKey(KeyCode.DownArrow))
			transform.Translate(-Vector3.forward * moveSpeed * Time.deltaTime);

		if(Input.GetKey(KeyCode.LeftArrow))
			transform.Rotate(Vector3.up, -turnSpeed * Time.deltaTime);

		if(Input.GetKey(KeyCode.RightArrow))
			transform.Rotate(Vector3.up, turnSpeed * Time.deltaTime);

	}
}
