"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.  May 2018.

"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# TODO: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------
    pig = Pig(200)
    print('Pigs weight = ', pig.get_weight())
    print('Weight after slop = ',pig.eat(0))
    print('Weight after a year = ',pig.eat_for_a_year(365))
    print('Heavier pig= ', pig.heavier_pig(67000))
    print('New Pig= ', pig.new_pig(67000))


class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        # DONE: Implement and test this method.
        self.weight = weight

    def get_weight(self):
        """ Returns this Pig's weight. """
        # DONE: Implement and test this method.
        return self.weight

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        # DONE: Implement and test this method.

        self.weight = self.weight + pounds_of_slop
        return self.weight

    def eat_for_a_year(self,n):
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        # DONE: Implement and test this method.
        for k in range(1,n):
            x = self.eat(k)
        return x


    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        # DONE: Implement and test this method.
        self.other_pig = other_pig
        if self.other_pig > self.weight:
            return self.other_pig
        else:
            return self.weight


    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        # DONE: Implement and test this method.
        self.other_pig = other_pig
        return self.other_pig

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
