# 365 days of Repos

## Day 1

This will be an interesting project, I will document my days in the MD for all the days in 2025, and maybe even do some coding, who knows
I have no idea how this will go, nor do i know if I will keep it up

<h3>FUN!!!</h3>

(No Code for day 1)

## Day 2

Today I want to talk about a cool coding trick I learned while coding pong for the... uh... 5th? no 4th time
I always used exact angles for the balls direction which seemed like the most obvious solution to me
It want until I was explaining to my friend the issue I was having with translating the game to vanilla minecraft did I realize a new solution
A solution that not only solved my issue making the game with commandblocks, it also gets rid of all the bugs my previous iterations had

So I would like to share it today because I find it interesting, I do not know what solution the original pong used and it would be good to research it. but finding solutions to my problems myself is fun to me.
The code is in [Cool](Cool/1.2.25-Move_A_Ball.py)

## Day 3

Ok I don't have any cool thing to share today, all I added to the folders was some basic functions in C and Java
These are functions that I keep remaking every time I make a new engine, so i just decided to keep it in a folder here for reference.
I have more of them in different languages but I cant find the python one.
I'm pretty sure yesterday I had something planned to talk about but I forgot it, So I am adding a [Future Topics Text Document](FutureTopics.md) to write down any ideas to talk about.

Tomorrow I am going to be very busy so i may miss that day or day 4 might be short

## Day 4

Today I did screamed into a mic for a sound test... not knowing i was live...
besides that today is too stressful to write anything.

## Day 6

And just like that... I missed day 5 lol

Today I will like to talk about old Operating Systems, Like DOS and Windows 3.1
Years ago I started using old OSs like DOS 5.0 for coding and I think it stuck with me because im still worried about 32bit filename errors lol.
Besides that I think the limitations help me become a better programmer and help me get better at CMD.
Also I miss GOTO command in languages, yes it can lead to confusions and messy code, but sometimes I want to just hop back to the top of the code without having all my lines check for a condition.

GOTO aside, I think working under limitation is a great skill teacher that helps you improve your skills, You'll see more often during this ReadMe that I love working under limitations.
A couple things to look forward to:

- Wordle in excel
- A screensaver for the TI84 Calculator
- A 3d render engine for the console with Ascii

## Day 8

Missed another day...

I can see that I am going to miss a lot of days and tracking the days is going to get a whole lot harder past january. So I've made a [Python script](Testing/WhatDay.py) to track the days for me

For todays interesting iota, I set up obsidian because I wanted to take notes in MD format.<br>
Im going to try get the cloud synchronization up and working when I get back from work.

## Day 9

Today I had to help rush pack a bunch of kids for a trip tomorrow (Im not going lol)<br>
didn't do anything too interesting today, Uh... I got a fax machine to work on linux after like 4 months of it not working. All I did was download HP drivers lol <br>
`sudo apt install hplip-gui` then `hp-setup`

## Day 11

Pain and suffering

## Day 15

So... My computer exploded 💀 <br>
Yea so I could have continued this on a different PC, but I was so focused on getting my laptop fixed I forgot this existed

Anywho, Today I will be trying to write a particle engine, but first I am going to write a basic static collision system, update on that tomorrow (If I get the chance to work on it today)

## Day 20

Ok I have no excuse this time, I simply forgot.

I did finish the collision system yesterday thou so if I did a day 16 I wouldn't have much to say. <br>
The collision system works quite simply, theres 3 components

- Map collision
- Object collision
- Particle collision

The Map collision was the simplest as it just detects if a 16x16 square chunk is filled ot not (Or any size you set it to)
(Its a 2d pixel engine btw) <br>
The Particle collision was interesting, it doesn't effect Objects but it is effected by objects, also its basically the same as the map but for 1 pixel <br>
The Object collision is alot more difficult and I am not fully finished with it. But essentially there are 2 types of collisions shapes: -Square & -Circle
And then theres 4 functions to describe how to know if they collided<br>
I will but in a system that checks every frame but also, only checks if the distance is close, otherwise to save recourses it wont check

Here's a sample code:

```C++
bool CheckCollisionCircleCircle(CollisionObject* other) {
	float distance = sqrt(pow(Position.x - other->Position.x, 2) + pow(Position.y - other->Position.y, 2));
	if (distance < Size.x + other->Size.x) {
		return true;
	}
	return false;
}
```

Thats all for today, I'll try not forget tomorrow :P

## Day 23

Quite simply... I hate dealing with Threads

## Day 42

Welp... I forgeot this existed oh well not going to quit just because I missed a few days <br>
Lets see how how much I can remember from the past 20 days

### I moved over to Linux
Specifically Ubuntu 20.04, I got sick and tired of windows so I finally made the switch, I still have a windows partition for... job reasons but If I need need to run a windows program and wine doesn't work I have a VM

### I Published a game (demo)
After 3 years of making games under my indie group and just, not publishing anything, I finally published a finished game!!!<br>
Its a demo cuz we plan on expanding the game (We made it for a Jam)
Check it out: [Bubblexity on Itch.io](https://bchaotic.itch.io/bubblexity)

### Minor updates
- Added a new function to [Basic.h](Saving/BasicLibs/Basic.h) , Just a way to check if something is a prime number
- Relized while uploading I dont have git on my linux PC, will download now lol

Besides that, I can't remember much else <br>
For the future: Imma try convert my game engine to linux and see how that goes, probably gunna pull my hair out, but oh well...

Anywho check out the game 🫵 <br>
See you in another month lol

## Day 52
How did I forget for EXACTLY 10 days... oh well 

Today I bring to you a line of code to get ur IP on bash
```bash
ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'
```
Nothing too intresting tbh, I just needed it and wanted to save it somewhere
Anywho, I do want to talk about something cool from linux
### NETCAT!!
Netcat is so cool!! You can use it to send commands over the network and because of unix piping u can use it for files too!! <br>
On the recieving end you use `nc -l  [port]` and on the sending end you can use `nc [ip] [port]` <br>
Ofc we cant forget the piping `cat [file] | nc [ip] [port]` <br>
And BOOM! the output of the file gets sent over the network <br>
You can use that to send files by piping the file in and out <br>
recieving end: `nc -l [port] > [file]` <br>
sending end: `nc [ip] [port] < [file]` <br>
And there you go, you can send files over the network with netcat <br>

idk... I find it cool lol <br>
anywho Imma def forget tmmr so hopefully I remember in less than 10 days this time

## Day 100!!
Ok I HAD to post one on day 100 <br>
Not much to say... I forgot this existed again until I saw it was day 100 <br>
uh... Ive been working on a wifilogger program for the past few days, I can talk about it more in the future <br>
For now... I added a new Basic lib to the [Basic Libs](Saving/BasicLibs) folder (This time for python) <br>
[Basic.py](Saving/BasicLibs/Basic.py) <br>

See you in another 100 days lol (Hopefully not)
