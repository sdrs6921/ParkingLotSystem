package parkserver.dbconnection;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class MySqlConnector {
	
	public static MySqlConnector mysqldb = null;
	private MySqlConnector() {}
	
	public static MySqlConnector getInstance() {
		if( mysqldb == null  ) {
			mysqldb= new MySqlConnector();
		}
		return mysqldb;
	}
	
	public Connection getConnection() {
		String driver = "com.mysql.cj.jdbc.Driver";
		String url = "jdbc:mysql://localhost:3306/parkingdb?characterEncoding=UTF-8&serverTimezone=UTC";
		String id = "root";
		String pw = "****";
		Connection conn = null;
		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url , id , pw);
		}catch (Exception e) {
			e.printStackTrace();
		}
		
		return conn;
	}
}
