import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class solution {
  public static void main(String[] args) throws IOException {
    List<List<Integer>> inputList = new ArrayList<>();
    try (BufferedReader br = new BufferedReader(new FileReader("data.txt"))) {
      String line;
      while ((line = br.readLine()) != null) {
        List<Integer> report = Arrays.stream(line.trim().split("\\s+"))
                       .map(Integer::parseInt)
                       .collect(Collectors.toList());
        inputList.add(report);
      }
    }

    // Part 1
    int safe = 0;
    for (List<Integer> report : inputList) {
      if (isSafe(report)) {
        safe++;
      }
    }
    System.out.println(safe);

    // Part 2
    safe = 0;
    for (List<Integer> report : inputList) {
      if (isMonotonicAndInRange(report)) {
        safe++;
      } else {
        for (int i = 0; i < report.size(); i++) {
          List<Integer> toleratedLevels = new ArrayList<>(report);
          toleratedLevels.remove(i);
          if (isMonotonicAndInRange(toleratedLevels)) {
            safe++;
            break;
          }
        }
      }
    }
    System.out.println(safe);
  }

  private static boolean isIncreasing(List<Integer> report) {
    for (int i = 0; i < report.size() - 1; i++) {
      if (report.get(i) >= report.get(i + 1)) {
        return false;
      }
    }
    return true;
  }

  private static boolean isDecreasing(List<Integer> report) {
    for (int i = 0; i < report.size() - 1; i++) {
      if (report.get(i) <= report.get(i + 1)) {
        return false;
      }
    }
    return true;
  }

  private static boolean isBetween1And3(List<Integer> report) {
    for (int i = 0; i < report.size() - 1; i++) {
      int diff = Math.abs(report.get(i + 1) - report.get(i));
      if (diff < 1 || diff > 3) {
        return false;
      }
    }
    return true;
  }

  private static boolean isSafe(List<Integer> report) {
    return (isIncreasing(report) || isDecreasing(report)) && isBetween1And3(report);
  }

  private static boolean isMonotonicAndInRange(List<Integer> levels) {
    List<Integer> diffs = new ArrayList<>();
    for (int i = 0; i < levels.size() - 1; i++) {
      diffs.add(levels.get(i) - levels.get(i + 1));
    }

    boolean isMonotonic = true;
    for (int diff : diffs) {
      if (diff <= 0) {
        isMonotonic = false;
        break;
      }
    }
    if (!isMonotonic) {
      isMonotonic = true;
      for (int diff : diffs) {
        if (diff >= 0) {
          isMonotonic = false;
          break;
        }
      }
    }

    boolean isInRange = true;
    for (int diff : diffs) {
      if (Math.abs(diff) < 1 || Math.abs(diff) > 3) {
        isInRange = false;
        break;
      }
    }

    return isMonotonic && isInRange;
  }
}