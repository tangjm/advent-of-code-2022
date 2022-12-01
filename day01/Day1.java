package aoc2022.day01;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Day1 {
    private static String DELIMITER = "";
    public static List<List<String>> to2DArrayList(String filename) throws
            IOException {
        File inputFile = new File(filename);
        String inputFilePath = inputFile.getAbsolutePath();
        BufferedReader fileReader =
                new BufferedReader(new FileReader(inputFilePath));

        String line;
        List<List<String>> lines = new ArrayList<>();
        List<String> tempList = new ArrayList<>();
        while ((line = fileReader.readLine()) != null) {
            if (DELIMITER.equals(line)) {
                lines.add(tempList);
                tempList = new ArrayList<>();
            } else {
                tempList.add(line);
            }
        }
        lines.add(tempList);
        return lines;
    }

    public static void main(String[] args) throws IOException {
        List<List<String>> elves = to2DArrayList(args[0]);
        List<Integer> elvesSorted = elves.stream()
                .map(arr -> arr.stream()
                        .map(Integer::parseInt)
                        .reduce(Integer::sum)
                        .orElse(null))
                .filter(Objects::nonNull)
                .sorted((x, y) -> y - x)
                .collect(Collectors.toList());

        int partOne = elvesSorted.get(0);
        int partTwo = elvesSorted.get(0)
                    + elvesSorted.get(1)
                    + elvesSorted.get(2);

        System.out.println("Part One:\t" + partOne);
        System.out.println("Part Two:\t" + partTwo);
    }
}
