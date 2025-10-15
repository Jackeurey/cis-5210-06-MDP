from gridworld import *
from agents import *


def test_ValueIterationAgentCreation():
    grid = PRESET_GRIDS["book"]
    discount = 0.0
    living_reward = 0
    game = Gridworld(discount, living_reward, grid)
    agent = ValueIterationAgent(game, discount)
    assert len(agent.values) == len(game.states)
    for (key, value) in agent.values.items():
        assert key in game.states
        assert value == 0


def test_ValueITerationAgentGetValues():
    grid = PRESET_GRIDS["book"]
    discount = 0.0
    living_reward = 0
    game = Gridworld(discount, living_reward, grid)
    agent = ValueIterationAgent(game, discount)
    agent.values[(0, 1)] = 4
    agent.get_value((0, 1))
