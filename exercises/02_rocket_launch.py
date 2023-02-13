import os
import time

__doc__ = """

Write a program that simulates a rocket launch by displaying:

    - countdown
    - lift-off

Next steps:

    - the countdown is really essential now, can you do better ?
      for example like this https://www.youtube.com/watch?v=bRPQmaFQiwM
    - add launchpad
    - add sounds

"""

rocket = """
                                        /
                                      *///(
                                    . ....,,
                                    .......,,
                                   . %(/,(((,,
                                   ..%/,((#/,,
                                  . .......,,,,
                                 ,. .......,,,*/
                                /// .......,,,(//
                               ////  ......,,,(///
                              ,///// ......,,((///
                               ////// ....,,((////
                               ////  .(%%%%   ///(
                                /     /..,/    ,(
                                     */,,,/.
                                     //,,,/,
                                     //,,,/.
                                     .//,//
                                      /////
                                      *///.
                                       ///
                                        /
"""

print("Countdown started !!!")

for second in range(10, 0, -1):
    print(second)
    time.sleep(1)

print("Lift-off !!!")
time.sleep(1)

n_lines = os.get_terminal_size().lines

for l in range(1, n_lines + 1):
    os.system("clear") # windows: "cls"
    frame = "\n" * (n_lines - 21 - l) + rocket + "\n" * l
    print(frame)
    time.sleep(1 / l)
