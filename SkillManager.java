import java.io.*;
import java.util.*;

public class SkillManager {

    private List<SkillEntry> entries = new ArrayList<>();
    private final String FILE_NAME = "data.txt";

    public void addSkill(String skill, int hours) {
        SkillEntry entry = new SkillEntry(skill, hours);
        entries.add(entry);
        saveToFile(entry);
    }

    private void saveToFile(SkillEntry entry) {
        try (FileWriter fw = new FileWriter(FILE_NAME, true)) {
            fw.write(entry.toString() + "\n");
        } catch (IOException e) {
            System.out.println("Error saving data!");
        }
    }

    public void loadData() {
        try (BufferedReader br = new BufferedReader(new FileReader(FILE_NAME))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                entries.add(new SkillEntry(parts[0], Integer.parseInt(parts[1])));
            }
        } catch (IOException e) {
            System.out.println("No previous data found.");
        }
    }

    public List<SkillEntry> getEntries() {
        return entries;
    }
}