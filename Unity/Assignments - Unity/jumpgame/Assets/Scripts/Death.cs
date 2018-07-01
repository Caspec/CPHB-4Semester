using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Death : MonoBehaviour {

    [SerializeField] private string loadLevel;

    void OnTriggerEnter2D(Collider2D theCollider)
    {
        if (theCollider.CompareTag("Player"))
        {
            ScoreScript.scoreValue = 0;
            SceneManager.LoadScene(loadLevel);
        }
    }
}
