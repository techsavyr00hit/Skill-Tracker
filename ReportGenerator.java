import java.util.*;

public class ReportGenerator {

    public void generateReport(List<SkillEntry> entries) {
        Map<String, Integer> skillHours = new HashMap<>();

        for (SkillEntry entry : entries) {
            skillHours.put(
                entry.getSkillName(),
                skillHours.getOrDefault(entry.getSkillName(), 0) + entry.getHoursSpent()
            );
        }

        System.out.println("\n===== Weekly Skill Report =====");
        for (String skill : skillHours.keySet()) {
            System.out.println(skill + " -> " + skillHours.get(skill) + " hours");
        }

        System.out.println("================================");
    }
}