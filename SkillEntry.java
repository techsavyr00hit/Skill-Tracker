import java.time.LocalDate;

public class SkillEntry {
    private String skillName;
    private int hoursSpent;
    private LocalDate date;

    public SkillEntry(String skillName, int hoursSpent) {
        this.skillName = skillName;
        this.hoursSpent = hoursSpent;
        this.date = LocalDate.now();
    }

    public String getSkillName() {
        return skillName;
    }

    public int getHoursSpent() {
        return hoursSpent;
    }

    public LocalDate getDate() {
        return date;
    }

    @Override
    public String toString() {
        return skillName + "," + hoursSpent + "," + date;
    }
}