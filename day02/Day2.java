package aoc2022.day02;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day2 {
    public static List<List<Integer>> readInputFile(String filename) throws FileNotFoundException {
        Scanner fs = new Scanner(new File(filename));

        List<List<Integer>> rounds = new ArrayList<>();
        while (fs.hasNextLine()) {
            String line = fs.nextLine();
            List<Integer> currentRound = new ArrayList<>();

            String[] letters = line.split(" ");
            for (String s : letters) {
                int charCode = Character.codePointAt(s, 0);
                currentRound.add(charCode);
            }
            rounds.add(currentRound);
        }
        return rounds;
    }

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

    public static int partOne(List<List<Integer>> rounds) {
        int[] outcomeToScore = {6, 0, 3};
        int totalShapeScore = 0;
        for (List<Integer> round : rounds) {
            int shapeScore = round.get(1) % 87;
            totalShapeScore += shapeScore;
        }
        int totalOutcomeScore = 0;
        for (List<Integer> round : rounds) {
            int outcome = (round.get(1) - round.get(0)) % 3;
            totalOutcomeScore += outcomeToScore[outcome];
        }
        return totalShapeScore + totalOutcomeScore;
    }

    public static int partTwo(List<List<Integer>> rounds) {
        int[] outcomeToScore = {6, 0, 3};
        int[] shapes = {88, 89, 90};

        int totalOutcomeScore = 0;
        int totalShapeScore = 0;
        for (List<Integer> round : rounds) {
            int opponentShape = round.get(0);
            int strategy = round.get(1);
            int desiredOutcome = strategy % 3;
            totalOutcomeScore += outcomeToScore[desiredOutcome];
            for (int shape : shapes) {
                boolean isCorrectShape =
                        (shape - opponentShape) % 3 == desiredOutcome;
               if (isCorrectShape) {
                  totalShapeScore += shape % 87;
               }
            }
        }
        return totalOutcomeScore + totalShapeScore;
    }

    public static void main(String[] args) throws FileNotFoundException {
        List<List<Integer>> rounds = readInputFile(args[0]);
        int partOneAnswer = partOne(rounds);
        System.out.printf("Part One: %s\n", partOneAnswer);

        int partTwoAnswer = partTwo(rounds);
        System.out.printf("Part Two: %s\n", partTwoAnswer);
    }
}
