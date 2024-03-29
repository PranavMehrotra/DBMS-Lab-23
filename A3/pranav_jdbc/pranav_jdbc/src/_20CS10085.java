import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;
import java.util.ArrayList;

public class _20CS10085 {
    // JDBC driver name and database URL
    private static String MYSQL_JDBC_DRIVER_CLASS = "com.mysql.cj.jdbc.Driver";
    private static String MYSQL_DB_URL = "jdbc:mysql://10.5.18.70:3306/20CS10085";
    private static String MYSQL_DB_USER = "20CS10085";
    private static String MYSQL_DB_USER_PASSWORD = "20CS10085";
    // Function to print table in a formatted way
    public static void printTable(ArrayList<ArrayList<String>> table) {
        int[] columnWidths = new int[table.get(0).size()];
        for (ArrayList<String> row : table) {
            for (int i = 0; i < row.size(); i++) {
                columnWidths[i] = Math.max(columnWidths[i], row.get(i).length());
            }
        }
        for (int i = 0; i < table.get(0).size(); i++) {
            columnWidths[i] += 2;
        }
        StringBuilder divider = new StringBuilder();
        divider.append("|");
        for (int width : columnWidths) {
            for (int i = 0; i <= width; i++) {
                divider.append("-");
            }
            divider.append("|");
        }
        System.out.println(divider.toString());
        for (ArrayList<String> row : table) {
            System.out.print("|");
            for (int i = 0; i < row.size(); i++) {
                System.out.print(" " + row.get(i));
                int padding = columnWidths[i] - row.get(i).length() - 1;
                for (int j = 0; j < padding; j++) {
                    System.out.print(" ");
                }
                System.out.print(" |");
            }
            System.out.println();
            System.out.println(divider.toString());
        }
    }



    public static void main(String[] args) {
        // Connection to the database
        try(Connection connection = DriverManager.getConnection(MYSQL_DB_URL,MYSQL_DB_USER,MYSQL_DB_USER_PASSWORD)) {

            Class.forName(MYSQL_JDBC_DRIVER_CLASS); 
            Statement statement =connection.createStatement();  
            // Scanner to take input from user
            Scanner sc= new Scanner(System.in);
            // Query to be executed
            String SQL_QUERY;
            // Result set to store the result of the query
            ResultSet resultSet;
            // Arraylist to store the result of the query in tabular form
            ArrayList<ArrayList<String>> arr = new ArrayList<>();
            // Arraylist to store the row of the table
            ArrayList<String> row = new ArrayList<>();
            // Loop to take input from user and execute the query
            while(true){
            System.out.print("Enter query number(Enter -1 to exit): ");  
            int a= sc.nextInt(); 
            // Switch case to execute the corresponding query
            switch(a) {
                case 1:
                SQL_QUERY = "SELECT Name \"Physician Name\" "+
                "FROM Physician "+
                "WHERE EmployeeID IN (SELECT Physician "+
                                     "FROM Trained_In "+
                                     "WHERE Treatment = (SELECT Code "+
                                                        "FROM Procedures "+
                                                        "WHERE Name = \"Bypass Surgery\"));";
                
                // Executing the query
                resultSet = statement.executeQuery(SQL_QUERY); 
                arr.clear();
                row.clear();
                // Adding the column names to the table
                row.add("Physician Name");
                arr.add(new ArrayList<>(row));
                // Adding the data rows to the table
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    arr.add(new ArrayList<>(row));
                }
                // Printing the table in a formatted way
                printTable(arr);
                  break;
                case 2:
                SQL_QUERY = "SELECT Name \"Physician Name\" "+
                "FROM Physician "+
                "WHERE EmployeeID IN (SELECT Physician "+
                                     "FROM Trained_In "+
                                     "WHERE Treatment = (SELECT Code "+
                                                        "FROM Procedures "+
                                                        "WHERE Name = \"Bypass Surgery\") AND Physician IN (SELECT Physician "+
                                                                                                          "FROM Affiliated_With "+
                                                                                                          "WHERE Department = (SELECT DepartmentID "+
                                                                                                                               "FROM Department "+
                                                                                                                               "WHERE Name = \"Cardiology\")));";
                resultSet = statement.executeQuery(SQL_QUERY); 

                arr.clear();
                row.clear();
                row.add("Physician Name");
                arr.add(new ArrayList<>(row));
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    arr.add(new ArrayList<>(row));
                }
                printTable(arr);     
                break;
                case 3:
                SQL_QUERY ="SELECT Name \"Nurse Name\" "+
                "FROM Nurse "+
                "WHERE EmployeeID IN (SELECT Nurse "+
                                    "FROM On_Call "+
                                    "WHERE (BlockFloor,BlockCode) IN (SELECT BlockFloor,BlockCode "+
                                                                    "FROM Room "+
                                                                    "WHERE Number = 123));"; 
                resultSet = statement.executeQuery(SQL_QUERY); 

                arr.clear();
                row.clear();
                row.add("Nurse Name");
                arr.add(new ArrayList<>(row));
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    arr.add(new ArrayList<>(row));
                }
                printTable(arr);   
                break;
                case 4:
                SQL_QUERY ="SELECT Name \"Patient Name\",Address \"Patient Address\" "+
                "FROM Patient "+
                "WHERE SSN IN (SELECT Patient "+
                                    "FROM Prescribes "+
                                    "WHERE Medication IN (SELECT Code "+
                                                    "FROM Medication "+
                                                    "WHERE Name = 'Remdesivir'));";
                resultSet = statement.executeQuery(SQL_QUERY); 

                arr.clear();
                row.clear();
                row.add("Patient Name");
                row.add("Patient Address");
                arr.add(new ArrayList<>(row));
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    row.add(resultSet.getString(2));
                    arr.add(new ArrayList<>(row));
                }
                printTable(arr);    
                break;
                case 5:

                SQL_QUERY ="SELECT Name \"Patient Name\",InsuranceID \"Patient Insurance ID\" "+
                "FROM Patient "+
                "WHERE SSN IN (SELECT Patient "+
                                    "FROM Stay "+
                                    "WHERE Room IN (SELECT Number "+
                                                    "FROM Room "+
                                                    "WHERE Type = 'ICU') AND DATEDIFF(`End`,Start)>15);";
                resultSet = statement.executeQuery(SQL_QUERY); 

                arr.clear();
                row.clear();
                row.add("Patient Name");
                row.add("Patient InsuranceID");
                arr.add(new ArrayList<>(row));
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    row.add(resultSet.getString(2));
                    arr.add(new ArrayList<>(row));
                }
                printTable(arr);  
                break;
                
                case 6:

                SQL_QUERY ="SELECT Name \"Nurse Name\" "+
                "FROM Nurse "+
                "WHERE EmployeeID IN (SELECT AssistingNurse "+
                                    "FROM Undergoes U "+
                                    "WHERE U.Procedure = (SELECT Code "+
                                                    "FROM Procedures "+
                                                    "WHERE Name = \"Bypass Surgery\"));";
                resultSet = statement.executeQuery(SQL_QUERY); 

                arr.clear();
                row.clear();
                row.add("Nurse Name");
                arr.add(new ArrayList<>(row));
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    arr.add(new ArrayList<>(row));
                }
                printTable(arr);      
                break;
                
                case 7:

                SQL_QUERY ="SELECT N.Name 'Nurse Name',N.Position 'Nurse Position',P.Name 'Physician Name' "+
                "FROM Physician P,Nurse N "+
                "WHERE (P.EmployeeID,N.EmployeeID) IN (SELECT Physician,AssistingNurse "+
                                    "FROM Undergoes "+
                                    "WHERE Undergoes.Procedure = (SELECT Code "+
                                                    "FROM Procedures "+
                                                    "WHERE Name = \"Bypass Surgery\"));";
                resultSet = statement.executeQuery(SQL_QUERY); 

                arr.clear();
                row.clear();
                row.add("Nurse Name");
                row.add("Nurse Position");
                row.add("Physician Name");
                arr.add(new ArrayList<>(row));
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    row.add(resultSet.getString(2));
                    row.add(resultSet.getString(3));
                    arr.add(new ArrayList<>(row));
                }
                printTable(arr);     
                break;
                
                case 8:

                SQL_QUERY ="SELECT Name \"Physician Name\" "+
                "FROM Physician "+
                "WHERE EmployeeID IN (SELECT Physician "+
                        "FROM Undergoes U "+
                        "WHERE (Physician,U.Procedure) NOT IN (SELECT Physician,Treatment "+
                                                    "FROM Trained_In));";
      
                resultSet = statement.executeQuery(SQL_QUERY); 

                arr.clear();
                row.clear();
                row.add("Physician Name");
                arr.add(new ArrayList<>(row));
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    arr.add(new ArrayList<>(row));
                }
                printTable(arr);     
                break;

                case 9:

                SQL_QUERY ="SELECT P.Name \"Physician Name\" "+
                "FROM ((Undergoes U "+
                "INNER JOIN Trained_In T "+
                "ON U.Physician = T.Physician AND U.Procedure = T.Treatment AND DATEDIFF(U.Date,T.CertificationExpires)>0) "+
                "INNER JOIN Physician P ON U.Physician = P.EmployeeID);";
    
                resultSet = statement.executeQuery(SQL_QUERY); 

                arr.clear();
                row.clear();
                row.add("Physician Name");
                arr.add(new ArrayList<>(row));
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    arr.add(new ArrayList<>(row));
                }
                printTable(arr);    
                break;

                case 10:

                SQL_QUERY ="SELECT P.Name \"Physician Name\",PR.Name \"Procedure Name\",U.Date \"Procedure Date\",PA.Name \"Patient Name\" "+
                "FROM ((((Undergoes U "+
                "INNER JOIN Trained_In T "+
                "ON U.Physician = T.Physician AND U.Procedure = T.Treatment AND DATEDIFF(U.Date,T.CertificationExpires)>0) "+
                "INNER JOIN Procedures PR ON U.Procedure = PR.Code) "+
                "INNER JOIN Patient PA ON U.Patient = PA.SSN) "+
                "INNER JOIN Physician P ON U.Physician = P.EmployeeID);";
                resultSet = statement.executeQuery(SQL_QUERY); 

                arr.clear();
                row.clear();
                row.add("Physician Name");
                row.add("Procedure Name");
                row.add("Procedure Date");
                row.add("Patient Name");
                arr.add(new ArrayList<>(row));
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    row.add(resultSet.getString(2));
                    row.add(resultSet.getString(3));
                    row.add(resultSet.getString(4));
                    arr.add(new ArrayList<>(row));
                }
                printTable(arr);     
                break;

                case 11:

                SQL_QUERY ="SELECT PA.Name \"Patient's Name\",P.Name \"Physician's Name\" "+
                "FROM (((SELECT Patient,Physician "+
                        "FROM Undergoes "+
                        "WHERE (Patient,Physician) IN (SELECT Patient,Physician "+
                                                        "FROM Prescribes "+
                                                        "WHERE (Patient,Physician) IN (SELECT Patient,Physician "+
                                                                                    "FROM Appointment "+
                                                                                    "WHERE Physician IN (SELECT Physician "+
                                                                                                        "FROM Affiliated_With "+
                                                                                                        "WHERE Department = (SELECT DepartmentID "+
                                                                                                                            "FROM Department "+
                                                                                                                            "WHERE Name = \"Cardiology\") AND Physician NOT IN (SELECT Head "+
                                                                                                                                                                            "FROM Department) "+
                                                                                                        ") "+
                                                                                    "GROUP BY Patient,Physician "+
                                                                                    "HAVING COUNT(*)>=2 "+
                                                                                    ") "+
                                                        "GROUP BY Patient,Physician "+
                                                        "HAVING COUNT(*)>=1 "+
                                                        ") AND `Procedure` IN (SELECT Code "+
                                                                            "FROM Procedures "+
                                                                            "WHERE Cost>5000) "+
                        "GROUP BY Patient,Physician "+
                        "HAVING COUNT(*)>=1) AS A "+
                "INNER JOIN Physician P ON A.Physician = P.EmployeeID) "+
                "INNER JOIN Patient PA ON A.Patient = PA.SSN);";
                resultSet = statement.executeQuery(SQL_QUERY); 

                arr.clear();
                row.clear();
                row.add("Patient Name");
                row.add("Physician Name");
                arr.add(new ArrayList<>(row));
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    row.add(resultSet.getString(2));
                    arr.add(new ArrayList<>(row));
                }
                printTable(arr); 
                break;

                case 12:

                SQL_QUERY ="SELECT Name \"Medication Name\",Brand \"Medication Brand\" "+
                "FROM Medication "+
                "WHERE Code = (SELECT Medication "+
                                "FROM Prescribes "+
                                "GROUP BY Medication "+
                                "ORDER BY COUNT(*) DESC "+
                                "LIMIT 1);";
      
                resultSet = statement.executeQuery(SQL_QUERY); 

                arr.clear();
                row.clear();
                row.add("Medicine Name");
                row.add("Medicine Brand");
                arr.add(new ArrayList<>(row));
                while(resultSet.next())  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    row.add(resultSet.getString(2));
                    arr.add(new ArrayList<>(row));
                }
                printTable(arr); 
                break;
                
                case 13:
                sc.nextLine();
                // Take procedure name from user
                System.out.print("Enter a Procedure: "); 
                String b= sc.nextLine(); 
                
                
                SQL_QUERY = "SELECT Name \"Physician Name\" "+
                "FROM Physician "+
                "WHERE EmployeeID IN (SELECT Physician "+
                                     "FROM Trained_In "+
                                     "WHERE Treatment = (SELECT Code "+
                                                        "FROM Procedures "+
                                                        "WHERE Name = '" + b + "'));";
                
                // Execute the query
                resultSet = statement.executeQuery(SQL_QUERY); 
                if(resultSet.next()==false)
                {
                    // If no physician is trained in the procedure
                    System.out.println("No Physician Trained in this Procedure");
                    break;
                }
                // If physician is trained in the procedure
                arr.clear();
                row.clear();
                row.add("Physician Name");
                arr.add(new ArrayList<>(row));
                // Add the result to the table
                while(true)  {
                    row.clear();
                    row.add(resultSet.getString(1));
                    arr.add(new ArrayList<>(row));
                    if(resultSet.next()==false) break;
                }
                // Print the table
                printTable(arr);  
                break;
                // If user enters -1, exit the program
                case -1:
                System.out.println("Bye!");
                break;
                // If user enters an invalid query number
                default:
                System.out.println("Invalid Query Number"); 
              }
              if(a==-1) break;
            }
               
            sc.close();
        } catch (Exception e) {
            System.out.println(e);
        }
       
    }

}
