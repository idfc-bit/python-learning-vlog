message = "likhith is gay ! "
print(message)
print(message.upper())
print(message.lower())
print(message.strip("   ")*2)
print(message.replace("gay","man"))
print(len(message))

next = "warning"
print(next[2:4])
print(next[2:-2])
print(message[2:6]) #[start:end]
print(message[::3]) #[start:end:skip]
print(next[::]) #even if you dont mention fucking position it u let it blank it will give entire 
print(f" {message},   {next} ")
