header = ["color", "diameter", "label"]

training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

class Node:
    def __init__(self, 
                splitting_condition, 
                true, false):
        self.splitting_condition = splitting_condition
        self.true = true
        self.false = false

class Leaf:
    def __init__(self, data):
        self.predictions = get_class_freq(data)

# boolean function to check splitting condition

def check_split(training_point, split_condition):

    colour_feature = 0
    numerical_feature = 1

    if(isinstance(split_condition, int)):
        if(training_point[numerical_feature] >= split_condition):
            return True
        return False
    else:
        if(training_point[colour_feature] == split_condition):
            return True
        return False

# function to split dataset based on boolean result

def partition(training_data, split_condition):
    
    true = [] # data points that satisfy splitting condition
    false = [] # data points that do NOT satisfy splitting condition

    for example in training_data:
        if check_split(example, split_condition):
            true.append(example)
        else:
            false.append(example)

    return true, false

# This can either be the whole training set or just a subset

def get_class_freq(training_data):

    class_freq = {}

    for example in training_data:
        label = example[-1]

        if (label not in class_freq):
            class_freq[label] = 0
        class_freq[label] += 1

    return class_freq

# function for impurity
# training_data is going to be a list of examples formed from a split...

def gini(training_data):

    class_freq = get_class_freq(training_data)
    impurity = 1
    for label in class_freq:
        prob_of_labels = class_freq[label] / len(training_data)
        impurity -= prob_of_labels**2
    return float(impurity)


def information_gain(left, right, current_uncertainty):
    """Information Gain.

    The uncertainty of the starting node, minus the weighted impurity of
    two child nodes.
    """
    p = len(left) / (len(left) + len(right))

    p = float(p)

    gl = gini(left)
    gr = gini(right)

    current_uncertainty = float(current_uncertainty)

    return current_uncertainty - p * gl - (1 - p) * gr


def select_split(training_data):

    best_gain = 0
    best_condition = None
    gini_impurity = gini(training_data)

    colour_feature = 0
    numerical_feature = 1
    
    feature_set = []
    for example in training_data:
        feature_set.append(example[colour_feature])
        feature_set.append(example[numerical_feature])
    feature_set = set(feature_set)

    for feature in feature_set:
        condition = feature # this what we split on
        left_node, right_node = partition(training_data, condition)
        gain = information_gain(left_node, right_node, gini_impurity)
        
        if(gain > best_gain):
            best_gain = gain
            best_condition = condition

    return best_gain, best_condition

def train_tree(training_data):
    
    gain, optimum_split = select_split(training_data)
    
    # check the base case
    if(gain == 0):
        return Leaf(training_data)
    
    true_examples, false_examples = partition(training_data, optimum_split)

    true_branch = train_tree(true_examples)
    false_branch = train_tree(false_examples)

    return Node(optimum_split, true_branch, false_branch)


def classify(row, node):
    """See the 'rules of recursion' above."""

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions

    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node,
    # to the example we're considering.
    
    if check_split(training_data, node.splitting_condition):
        return classify(training_data, node.true)
    else:
        return classify(training_data, node.false)


def print_tree(node, spacing=""):

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print (spacing + "Predict", node.predictions)
        return

    # Print the question at this node
    print(spacing + str(node.splitting_condition))

    # Call this function recursively on the true branch
    print (spacing + '--> True:')
    print_tree(node.true, spacing + "  ")

    # Call this function recursively on the false branch
    print (spacing + '--> False:')
    print_tree(node.false, spacing + "  ")





def main():
    my_tree = train_tree(training_data)
    print_tree(my_tree)

    print(classify(training_data[0], my_tree))

    

if __name__ == "__main__":
    main()
    pass
     
