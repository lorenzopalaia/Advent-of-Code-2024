import java.io.*;
import java.util.*;
import java.nio.file.*;
import java.util.stream.Collectors;

public class solution {
  public static void main(String[] args) throws IOException {
    List<List<Integer>> inputList = Files.lines(Paths.get("data.txt"))
      .map(line -> Arrays.stream(line.trim().split("\\s+"))
      .map(Integer::parseInt)
      .collect(Collectors.toList()))
      .collect(Collectors.toList());

    List<Integer> leftList = new ArrayList<>();
    List<Integer> rightList = new ArrayList<>();

    for (List<Integer> pair : inputList) {
      leftList.add(pair.get(0));
      rightList.add(pair.get(1));
    }

    // Part 1
    Collections.sort(leftList);
    Collections.sort(rightList);

    int distance = 0;
    for (int i = 0; i < leftList.size(); i++) {
      distance += Math.abs(leftList.get(i) - rightList.get(i));
    }

    System.out.println(distance);

    // Part 2
    Map<Integer, Long> rightCounter = rightList.stream()
      .collect(Collectors.groupingBy(e -> e, Collectors.counting()));

    long similarityScore = 0;
    for (int leftNumber : leftList) {
      similarityScore += leftNumber * rightCounter.getOrDefault(leftNumber, 0L);
    }

    System.out.println(similarityScore);
  }
}