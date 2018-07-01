using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BoostScript : MonoBehaviour {

    [SerializeField] private string findBooster;
    private bool player = false;
    


    void OnTriggerEnter2D(Collider2D theCollider)
    {
        if (theCollider.CompareTag("Player") && !player)
        {
            GameObject thePlayer = GameObject.Find("PennyPixel");
            PlayerPlatformerController playerScript = thePlayer.GetComponent<PlayerPlatformerController>();
            player = true; // this stops OnCollision.... from running again
            playerScript.maxSpeed += 30;
            StartCoroutine(speedTime());
        }
    }

     IEnumerator speedTime()
     {
        yield return new WaitForSeconds(4);
        revertSpeed();
     }
  
     void revertSpeed()
     {
        GameObject thePlayer = GameObject.Find("PennyPixel");
        GameObject boosterFound = GameObject.Find(findBooster);
        PlayerPlatformerController playerScript = thePlayer.GetComponent<PlayerPlatformerController>();
        playerScript.maxSpeed = 7;
        Destroy(boosterFound);
     }
}
