1. Installed the 'gym' package using the terminal.
2. Imported the 'gym' and the 'pygame' packages.
3. Set up an environment using the gym.make() command.
4. Start the simulation using the env.reset() command.
5. Then, initialised the coefficients for the PID controller.
6. After that I initialised the force and the error to zero.
7. Then started the iterations with 200 episodes.
8. Used the reinforcement technique to get the error using the current state of the cart-pole.
9. Set the force to 0 and if the error was positive, change the force to 1.
10. This shows that we apply a force in the direction in which the pole is bending.
11. If the operation if done, we reset the environment and exit.