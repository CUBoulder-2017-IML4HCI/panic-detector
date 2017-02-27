# panic-detector
Detects the panic

By Urban Martin & Arcadia(Xiaozhe) Zhang

##Goal
Our goal is to build a system capable of detecting the onset of a panic attack.  An early alert could allow the user to change their behavior or remove themself from a hostile or dangerous situation.  Another potential use would be to alert a trusted friend or service animal.

##Hardware:
Our current system is prototyped as a wearable bracelet using the BBC Micro:Bit, with an external thermistor measuring skin temperature.  We use an internal accelerometer to detect small jittery hand motions.  Both hand tremors and sudden rise in skin temperature have been identified as symptoms of a panic attack.  We are working on adding more sensors that produce relevant data according to current research, including heart rate, galvanic skin response, and blood oxygen level.

##Algorithms:
A dynamic time warping method is used to track relative values of each feature evaluated over time.  Sudden, simultaneous changes in multiple features trigger a panic attack warning.
