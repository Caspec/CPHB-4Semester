using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BossJump : MonoBehaviour {

    private float min = 2f;
    private float max = 3f;

    // Use this for initialization
    void Start()
    {
        min = transform.position.y;
        max = transform.position.y + 8;
    }

    // Update is called once per frame
    void Update()
    {
        transform.position = new Vector3(transform.position.x, Mathf.PingPong(Time.time * 8, max - min) + min, transform.position.z);
    }
}
