from ple.games.flappybird import FlappyBird
from ple import PLE


game = FlappyBird()
p = PLE(game, fps=30, display_screen=True)
#agent = myAgentHere(allowed_actions=p.getActionSet())

p.init()
reward = 0.0
nb_frames=1000
for i in range(nb_frames):
   if p.game_over():
           p.reset_game()

   observation = p.getScreenRGB()
   #action = agent.pickAction(reward, observation)
   action=0
   reward = p.act(action)


