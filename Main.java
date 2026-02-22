import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        SkillManager manager = new SkillManager();
        ReportGenerator report = new ReportGenerator();

        manager.loadData();

        while (true) {
            System.out.println("\n1. Add Skill Entry");
            System.out.println("2. Generate Report");
            System.out.println("3. Exit");
            System.out.print("Choose option: ");

            int choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Enter skill name: ");
                    String skill = sc.nextLine();

                    System.out.print("Hours spent: ");
                    int hours = sc.nextInt();

                    manager.addSkill(skill, hours);
                    System.out.println("Entry Added!");
                    break;

                case 2:
                    report.generateReport(manager.getEntries());
                    break;

                case 3:
                    System.out.println("Goodbye!");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}
