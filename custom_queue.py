import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add item to the end of the queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue"""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        """Return the item at the front of the queue without removing it"""
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner and dequeues up to and including that customer.
        Returns the winner’s name.
        """
        if self.is_empty():
            return None

        winner_index = random.randint(0, len(self.items) - 1)
        winner = self.items[winner_index]

        # Dequeue up to and including the winner
        for _ in range(winner_index + 1):
            self.dequeue()

        return winner
