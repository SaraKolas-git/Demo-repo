import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class VulnerableApp {

    // Hardcoded credentials (Security issue)
    private static final String DB_URL = "jdbc:mysql://localhost:3306/testdb";
    private static final String USER = "root";
    private static final String PASS = "password123";

    public static void main(String[] args) {
        VulnerableApp app = new VulnerableApp();

        String username = args.length > 0 ? args[0] : null;

        // Null pointer risk
        if (username.equals("admin")) {
            System.out.println("Welcome admin!");
        }

        app.getUserData(username);

        // Infinite loop (performance issue)
        while (true) {
            System.out.println("Running...");
        }
    }

    public void getUserData(String username) {
        Connection conn = null;
        Statement stmt = null;

        try {
            // No proper resource handling
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            stmt = conn.createStatement();

            // SQL Injection vulnerability
            String query = "SELECT * FROM users WHERE username = '" + username + "'";
            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                System.out.println("User: " + rs.getString("username"));
            }

        } catch (Exception e) {
            // Bad practice: printing stack trace
            e.printStackTrace();
        } finally {
            // Resource leak: not closing properly
            try {
                conn.close();
            } catch (Exception e) {
                // Swallowed exception
            }
        }
    }

    // Dead code
    public void unusedMethod() {
        int x = 10;
        int y = 0;
        int result = x / y; // Divide by zero
    }

    // Hardcoded password comparison (bad practice)
    public boolean login(String password) {
        if (password == "admin123") { // Wrong string comparison
            return true;
        }
        return false;
    }
}