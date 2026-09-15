hi guys

first time doing this whole coding stuff

i uh
made this in coding class

it works

im probably gonna share this amongst my friends

this things kinda useless since 47.124 speed is and always will be the best speed but i made it for funs sake.

other motor demean settings because YOU GUYS are goobers and dont know these yet

and i will explain WHY theyre so good!

motor 1

backward: key you will always use to activate motor               forward: deadkey(if youre on computer use something like delete or keypad minus)

you do this because demean only really works when the motor is spinning backward, but for whatever reason spinning your blade backwards at about 45 degrees per game tick is great for damage and clipping
(a game tick is when the game does all its calculations 60 times a second.)
anyways lets continue

speed: 47.124

maxtorque: 0.63(prevents blade from flinging around and "rodding")

powered: ON   reset: OFF

lock: ON      toggle: ON

velocity: OFF     collision: OFF

powered and toggle are self explanatory, but lock will FAR increase your blade power and especially your clipping, because it allows your blade to be massless.

Massless is caused when you have THIS configuration

[anchored block]-[motor 2 with AT LEAST 100 torque, ideally 1000]-[rest of your creation]

most shredder tuts nowadays have a pretty good massless that uses a balljoint for better deployment, use one of those.

a basic 5x3 gyrocore has this, and that's why they are so fast and need an anchored block.

HOWEVER!!!!!!!!

if you have a "constraint" part in your creation(motors are a constraint), then any part only attached to the massless area via a motor (like a blade attached to your massless core),
massless will NOT be applied to it!

This is why some tutorials connect the blade with disconnectors, springs, or zeroed out tnt.

However, simply turning on the "lock" setting for your motor will do the same thing more efficiently.

Now your blade should be able to clip through tnt armor, blacklists, and the ground!
(assuming you have a good blade, nghiehuy12 has great tuts on how to make your blades better and flatblades are the best overall due to their very high clipping while still having good damage and density.)

have fun!

-bagel, creator of the michealwave
