# AI_Lyricist 
Created an AI that automatically generates new song lyrics AND a spoken.mp3 file for the new song! 
Resources and tools used: [song lyrics file (Kaggle)](https://www.kaggle.com/mousehead/songlyrics),  [pandas](https://pandas.pydata.org/pandas-docs/version/0.18/index.html), [Markovify](https://github.com/jsvine/markovify), [IBM Watson Text-To-Speech API](https://console.bluemix.net/catalog/services/text-to-speech), [TextBlob](https://textblob.readthedocs.io/en/dev/)

## Examples:

 <details>
  <summary>Drake</summary><p>
  
  The Drake AI learned from 117 songs.

    To pick a lane. That's all I have fun girl
    You can run an tell my city I'd be for you
    Just to show myself what I got, let's be logical, yeah
    Oh, you just landed in that deep snow
    This could be the only sound you should choose where we can relive it
    I get it, I get high as fuck and the music

    Shit is hot up in this b-tch wasup
    And who told you that time will heal that
    You and whoever the fuck are y'all?
    Don't compensate for the dogs dem, you know it, I get it over and read it.
    It aint about the times we had dreams of getting bigger man

    Who you with? What you really fail to exist
    Let's celebrate with a heart that I ain't never been a cheapskate
    Cause this truly is some sh-t I don't know why they been lying but yo shit is hot up in your New York condo
    And some charges, how the champagne diamonds flow
    This shit is new to this

    I wish I had someone tell me what you do, I do what I gave your nickname to someone else
    I'll be getting back to my room and ask me what I lands on
    This just might get it
    Please don't be a cheater but that's what happens
    They look up to my face

    Sold a couple other people that I see is fireworks, all I see it in the Bay
    Better yet where your bed at
    I turn and your fucking Mama Mia
    Eyes hurting from the city, cause you got adjusted
    I can't really make me call my bros, for assistance

    And I'll start hatin', only if you had it all
    It's coherent, I can tell all of my patience
    I got my eyes and see I start work now, aye
    Doesn't matter where I'm is
  </p></details>
  
  <details>
  <summary>Ed Sheeran</summary><p>
  
  The Ed Sheeran AI learned from 53 songs.
    
    This love's too overrated, see what's going on, on stage, mics on, song plays, nice one
    And the want of width
    It hurts when it's late
    But she don't want to take a walk on the treadmill
    I haven't changed since our last kiss it was painful
    Place your head to toe

    I can be like you are the color of red like the way you want me to come home.
    If you feel so right
    She's in the nude
    We used each other's air just for tonight I wanna feel your touch
    When you're on my heart to stop me bleeding now, now,

    I guess we'll have to take me away, away.
    If you're horny, let's do it for a couple grams
    Go ahead and just pretend
    And surely you'll never love me like you do
    Stick the promise man that you remember me

    What I do it all away
    And will you recognise me, when I'm missing you, I'll stop eating food
    When I see fire burn auburn on the last twenty of my family
    When I'm away, I will stand upon
    Rise from the skin to my sleeve

    How? I was just like glue
    I made all my friends have gone to waste
    So we'll learn to love you better now
    This is how it ends, I feel inspired, at quarter to three A.M.
  </p></details>

## How to use:
Download the project and open a command line/terminal. To create the AI for an artist, type:
```bash
$ python song_scrape.py "{Artist Name}"
```
This will compile a .txt file of all the artist's songs in `./artists/` and create an AI model for the artist in `./models/`.
To generate new song lyrics and .mp3 file, decide whether the voice should be `"f"` for female or `"m"` for male. Then (if `"f"` for example), run:
```bash
$ python song_gen.py "{Artist Name}" "{New Song Name}" "{f|m}"
```
This will generate the new song in .txt file in `./new_lyrics/` and create a .mp3 for the song in `./mp3_files/`.

## Ideas for improvement:
* Host all this on a website
* Train models on sentiment-analyzed lyrics to generate happier/angstier lyrics





