from argparse import Action
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


def test_ValueITerationAgent_get_q_values():
    grid = PRESET_GRIDS["book"]
    discount = 0.0
    living_reward = 0
    game = Gridworld(noise=0.2, living_reward=living_reward, grid=grid)
    agent = ValueIterationAgent(game, discount)
    assert agent.get_q_value((2, 3), Gridworld.Action.Up) == -1


def test_is_terminal():
    grid = PRESET_GRIDS["book"]
    discount = 0.0
    living_reward = 0
    game = Gridworld(discount, living_reward, grid)
    agent = ValueIterationAgent(game, discount)
    assert agent.is_terminal_state((1, 3))
    assert agent.is_terminal_state((0, 3))
    assert not agent.is_terminal_state((0, 0))


def test_value_iterate():
    grid = PRESET_GRIDS["book"]
    discount = 0.0
    living_reward = 0
    game = Gridworld(discount, living_reward, grid)
    agent = ValueIterationAgent(game, discount)
    assert agent.iterate()


test_ValueITerationAgent_get_q_values()
