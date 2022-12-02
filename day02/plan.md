### Part One
We can compute the score for the shape we selected for each round separately from the score for the outcome of the round and then sum the two totals to obtain a final total. 

To get the score for the shape, we can use the formula:
yourShape mod 87.

To compute the score for the outcome, we can take the difference of each player's codepoints and then do some modular arithmetic. 

Consider:

Score(Opponent, Myself) = codePoint(Myself) - codePoint(Opponent)
Score(A, X) = codePoint(X) - codePoint(A) 

ASCII Table

A 65 
B 66 
C 67

X 88 
Y 89 
Z 90

Opponent Myself Score(Opponent, Myself) Outcome
A X 23  draw
B X 22  loss
C X 21	win

A Y 24	win
B Y 23 	draw
C Y 22  loss

A Z 25  loss
B Z 24	win
C Z 23  draw

We win if Score(opponent, myself) mod 3 == 0
We lose if Score(opponent, myself) mod 3 == 1
We draw if Score(opponent, myself) mod 3 == 2

draw -> 23    -> 23    mod 3 = 2  
loss -> 22/25 -> 22/25 mod 3 = 1  
win  -> 21/24 -> 21/24 mod 3 = 0  

We can then do some pattern matching:

0 -> win  -> 6
1 -> lose -> 0
2 -> draw -> 3

### Part Two 

This time round, we need to compute the shape rather than the outcome. 

The outcome of each round can be summed up by the following formula:

strategy mod 3

Then we perform the mappings, where 0 is a win, 1 is a loss and 2 is a draw:
0 -> 6
1 -> 0
2 -> 3

The shape is then determined by the equation: 

(myShape - opponentShape) mod 3 == outcome

We can then try each shape out of {X, Y, Z} to satisfy the equation. 


### Alternative solution

```java
public static int partOneRefactored(List<List<Integer>> rounds) {
    int[] shapeScores = {1, 2, 3};
    int totalShapeScore = 0;
    int totalOutcomeScore = 0;
    for (List<Integer> round : rounds) {
        int opponentShape = round.get(0) % 65;
        int myShape = round.get(1) % 88;
        totalShapeScore += shapeScores[myShape];
        if (myShape == opponentShape) {
            totalOutcomeScore += 3;
        } else if (myShape == (opponentShape + 1) % 3) {
            totalOutcomeScore += 6;
        } else {
            totalOutcomeScore += 0;
        }
    }
    return totalShapeScore + totalOutcomeScore;
}

public static int partTwoRefactored(List<List<Integer>> rounds) {
    // 0 -> Lose / Rock
    // 1 -> Draw / Paper
    // 2 -> Win  / Scissors
    int[] shapeToScore = {1, 2, 3};
    int[] outcomeToScore = {0, 3, 6};

    int totalShapeScore = 0;
    int totalOutcomeScore = 0;
    for (List<Integer> round : rounds) {
        int opponentShape = round.get(0) % 65;
        int outcome = round.get(1) % 88;
        int outcomeScore = outcomeToScore[outcome];
        totalOutcomeScore += outcomeScore;
        int myShape;
        if (outcome == 0) {
            myShape = (((opponentShape - 1) % 3) + 3) % 3;
        } else if (outcome == 1) {
            myShape = opponentShape;
        } else {
            myShape = (opponentShape + 1) % 3;
        }
        totalShapeScore += shapeToScore[myShape];
    }
    return totalShapeScore + totalOutcomeScore;
}
```