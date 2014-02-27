import pymorse

with pymorse.Morse() as morse:
    while True:
        pose = morse.robot.pose.get()
        morse.ghost.teleport.publish(pose)
        morse.sleep(.1)
