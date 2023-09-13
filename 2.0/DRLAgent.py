class DRLAgent:
    
    def __init__(self) -> None:
        pass
    
# Build architecture of the model and compile
    def buildModel(self):
        pass

# Choosing an appropriate action based on the policy
    def chooseAction(self):
        pass

    def train(self):
        pass

# To save the weights of the agent
    def saveWeights(self, filename):
        self.model.save_weights(filename)

# To load the weights of the agent
    def loadWeights(self, filename):
        self.model.load_weights(filename)