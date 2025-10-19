# Dungeon Game

An experiment synthesizing LLM text generation with traditional procedural generation techniques.


## What?

This is a (currently text-based) RPG game that utilizes LLM text generation for certain descriptions and character interactions. Think of it as a computer RPG with an AI Dungeon Master.


## Why?

I believe that recent AI technologies allow for a whole new world of design space for procedurally generated video games, and that the tech is not currently being utilized to its full potential.

It's also a fun project to work on and a nice portfolio piece.


## How?

### Startup

This program requires you to connect to an LLM server. Specify the server you wish to connect to with the command line arguement ```-url=<http://someurl.com:1234>```. If the program fails to connect to that URL or if no URL is specified, the program will attempt to connect to a local ollama server.

Several ollama modelfiles designed to  are included in the /dm folder. DungeonDM is the recommended model to use. Though I personally like DreamDM a lot. You can specify the model you wish to use with the arguement ```-model=<model_name>```.


### Gameplay

Select commands by entering the corresponding integer.
Enter 0 to exit the program.


## License

This program is distributed under a GPLv2 license.


## Credits

Program by Kyle MacFarland


## Warning

This game utilizes generative artificial intelligence. Who knows what kind of crazy nonsense it will spit out? Be careful and stay safe.
