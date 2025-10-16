# Include your imports here, if any are used.
import math
import copy
from os import confstr_names

student_name = "John Coleman"


# 1. Value Iteration
class ValueIterationAgent:
    """Implement Value Iteration Agent using Bellman Equations."""

    def __init__(self, game, discount):
        """Store game object and discount value into the agent object,
        initialize values if needed.
        """
        self.game = game
        self.discount = discount
        values = {}
        for state in game.states:
            values[state] = 0
        self.values = values

    def get_value(self, state):
        """Return value V*(s) correspond to state.
        State values should be stored directly for quick retrieval.
        """
        return self.values[state]

    def is_terminal_state(self, state):
        return self.game.get_actions(state) == set()

    def get_q_value(self, state, action):
        """Return Q*(s,a) correspond to state and action.
        Q-state values should be computed using Bellman equation:
        Q*(s,a) = Σ_s' T(s,a,s') [R(s,a,s') + γ V*(s')]
        """
        expected_utility = 0
        transitions = self.game.get_transitions(state, action).items()
        for (next_state, chance) in transitions:
            reward = self.game.get_reward(state, action, next_state)
            next_value = self.get_value(
                next_state) if not self.is_terminal_state(next_state) else 0
            expected_utility += chance * (reward + self.discount * next_value)
        return expected_utility

    def get_best_policy(self, state):
        """Return policy π*(s) correspond to state.
        Policy should be extracted from Q-state values using policy extraction:
        π*(s) = argmax_a Q*(s,a)
        """
        max_action = None
        max_value = -math.inf
        for action in self.game.get_actions(state):
            value = self.get_q_value(state, action)
            if value > max_value:
                max_value = value
                max_action = action
        return max_action

    def iterate(self):
        """Run single value iteration using Bellman equation:
        V_{k+1}(s) = max_a Q*(s,a)
        Then update values: V*(s) = V_{k+1}(s)
        """
        new_values = {}
        for state in self.game.states:
            q_values = [self.get_q_value(state, action)
                        for action in self.game.get_actions(state)]
            new_values[state] = max(q_values)
        self.values = new_values


# 2. Policy Iteration
class PolicyIterationAgent(ValueIterationAgent):
    """Implement Policy Iteration Agent.

    The only difference between policy iteration and value iteration is at
    their iteration method. However, if you need to implement helper function
    or override ValueIterationAgent's methods, you can add them as well.
    """

    def get_best_policies(self):
        policies = {}
        for state in self.game.states:
            policies[state] = self.get_best_policy(state)
        return policies

    def iterate(self):
        """Run single policy iteration.
        Fix current policy, iterate state values V(s) until
        |V_{k+1}(s) - V_k(s)| < ε
        """
        epsilon = 1e-6
        policy_values = {}
        polices = self.get_best_policies()
        converged = {state: False for state in self.values.keys()}
        while not all(converged.values()):
            for state in self.values.keys():
                policy_values[state] = self.get_q_value(state, polices[state])
                new_policy = self.get_best_policy(state)
                new_q = self.get_q_value(state, new_policy)
                if new_q > policy_values[state]:
                    polices[state] = new_policy
                    policy_values[state] = new_q
                if abs(policy_values[state] - self.values[state]) < epsilon:
                    converged[state] = True
            self.values = policy_values

        ...  # TODO


# 3. Bridge Crossing Analysis
def question_3():
    discount = ...
    noise = ...
    return discount, noise


# 4. Policies
def question_4a():
    discount = ...
    noise = ...
    living_reward = ...
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4b():
    discount = ...
    noise = ...
    living_reward = ...
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4c():
    discount = ...
    noise = ...
    living_reward = ...
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4d():
    discount = ...
    noise = ...
    living_reward = ...
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4e():
    discount = ...
    noise = ...
    living_reward = ...
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


# 5. Feedback
# Just an approximation is fine.
feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
