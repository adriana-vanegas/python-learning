# While Loops + If Statement

command = ""
started = False

while True:
  command = input('> ').lower()
  if command == 'help':
    print('start - to start the car \nstop - to stop car \nquit - to exit')
  elif command == 'start':
    if started:
      print('Car was already started.')
    else: 
      started = True
      print('Car started... ready to go!')
    
  elif command == 'stop':
    if not started:
      print('Car is already stopped.')
    else: 
      print('Car stopped')
      started = False
  elif command == "quit":
    quit()
  else:
    print("I don't understand")

  