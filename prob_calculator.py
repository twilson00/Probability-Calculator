import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **kwargs):
        #Keep copy of args
        self._originalContents = kwargs
        
        #Used for accessing/deleting 
        self.contents = self.set_up_contents(kwargs)
        
    def set_up_contents(self, kwargs):
        self.contents = []
        
        for arg in kwargs:
            self.contents.extend([arg for i in range(kwargs[arg])])
        return self.contents
    
    def draw(self, numberToDraw):
        selectedBalls = []
        
        if numberToDraw > len(self.contents):
            return self.contents
        else:
            for i in range(0, numberToDraw):
                randomNumber = random.randint(0, len(self.contents) - 1)
                selectedBalls.append(self.contents[randomNumber])
                self.contents.pop(randomNumber)
        
        return selectedBalls
    
    def selected_balls_to_dictionary(self, selectedBalls):
        selectedBallsDictionary = {}
        
        x = len(selectedBalls)
        
        for i in range(len(selectedBalls)):
            if selectedBalls[i] in selectedBallsDictionary:
                selectedBallsDictionary[selectedBalls[i]] += 1
            else: 
                 selectedBallsDictionary[selectedBalls[i]] = 1
        
        return selectedBallsDictionary

    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successCount = 0
    
    for i in range(num_experiments):
        hat.contents = hat.set_up_contents(hat._originalContents)
        
        selectedBalls = hat.draw(num_balls_drawn)
        selectedBallsDictionary = hat.selected_balls_to_dictionary(selectedBalls)
        
        matchingBalls = 0
        for k,v in selectedBallsDictionary.items():
            if k in expected_balls:
                if expected_balls[k] <= v:
                    matchingBalls += 1
            
        if matchingBalls == len(expected_balls):
            successCount += 1

    probability = successCount / num_experiments
    
    return probability

