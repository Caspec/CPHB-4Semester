using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class KeyScript : MonoBehaviour {

    [SerializeField] private string findWall;
    [SerializeField] private string findKey;

    void OnTriggerEnter2D(Collider2D theCollider)
    {
        if (theCollider.CompareTag("Player"))
        {
            GameObject wallFound = GameObject.Find(findWall);
            GameObject keyFound = GameObject.Find(findKey);
            Destroy(wallFound);
            Destroy(keyFound);
        }
    }
}
